from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib import messages
from base_check.forms import *
from base_check.models import Worksheet
from django.db import transaction

# Base views for using in specific check apps

class BarcodeFormsetMixin:

    def get_barcode_formset(self):
        if hasattr(self, 'barcode_formset'):
            return self.barcode_formset

        if self.request.POST:
            formset = post_formset(self.request.POST, self.model, self.barcode_model, self.barcode_form)
        else:
            formset = get_formset(self.kwargs['barcode_count'], self.model, self.barcode_model, self.barcode_form)
        self.barcode_formset = formset
        return formset

    def form_invalid(self, form):
        barcodes = self.get_barcode_formset()
        messages.warning(self.request, form.errors)
        for error in barcodes.errors:
            messages.warning(self.request, error)
        return self.render_to_response(self.get_context_data(form=form, formset=barcodes))

class CheckView(BarcodeFormsetMixin, CreateView):
    template_name = 'base_check/base_check.html'
    #fields = []
    barcode_model = None
    barcode_form = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["barcodes"] = self.get_barcode_formset()
        return data

    def form_valid(self, form):
        barcodes = self.get_barcode_formset()
        if not barcodes.is_valid():
            return self.form_invalid(form)
        with transaction.atomic():
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
            barcodes.instance = self.object
            barcodes.save()
        if self.object.checkPassFail():
            messages.success(self.request, 'Check Passed')
        else:
            messages.warning(self.request, 'Check Failed - Barcodes do not match')

        return super().form_valid(form)


class WorksheetCheckView(CheckView):
    template_name = 'base_check/base_check.html'

    def get_worksheet_data(self):
        if self.request.POST:
            post = self.request.POST
            return {"check_number":post['check_number'],
             "check_description":post['check_description'],
             "worksheet_number":post['worksheet_number'],
             "check_record":self.model.objects.filter(worksheet=post["worksheet_number"],
                                                             check_number=post["check_number"]).order_by('-dateTime_check')}
        return {}

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data.update(self.get_worksheet_data())
        return data

    def form_valid(self, form):
        data = self.get_worksheet_data()
        barcodes = self.get_barcode_formset()

        # Hook for validation
        validation_error = self.validate_barcodes(barcodes)
        if validation_error:
            messages.warning(self.request, validation_error)
            return self.form_invalid(form)

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.worksheet, created = Worksheet.objects.get_or_create(worksheet_number=data["worksheet_number"])
        self.object.check_number = data["check_number"]
        self.object.check_description = data["check_description"]

        if barcodes.is_valid():
            self.object.save()
            barcodes.instance = self.object
            barcodes.save()

            # Hook for post-save processing of barcodes.
            self.process_saved_barcodes(barcodes)

            for error in barcodes.errors:
                messages.warning(self.request, error)
            if self.object.checkPassFail():
                messages.success(self.request, 'Check Passed')
            else:
                messages.warning(self.request, 'Check Failed - Barcodes do not match')

        else:
            return self.form_invalid(form)
        return super().form_valid(form)

    def validate_barcodes(self, barcodes):
        """Override to add custom validation. Return error message or None. e.g. for matchpaircheck need to check
        there is an even number of barcodes entered."""
        return None

    def process_saved_barcodes(self, barcodes):
        """Override to add post-save barcode processing.e.g. matchpaircheck assign comparisonId's to barcode instances."""
        pass


class AssignedWorksheetCheck(WorksheetCheckView):
    model = None
    barcode_model = None
    barcode_form = None
    view_name = None
    template_name = 'base_check/base_check.html'

    # AssignedWorksheetCheck.get_worksheet_data gets data from kwargs for get- and post-requests.
    def get_worksheet_data(self):
        return {"check_number": self.kwargs['check_number'],
                "check_description": self.kwargs['check_description'],
                "worksheet_number": self.kwargs['worksheet_number'],
                "check_record": self.model.objects.filter(worksheet=self.kwargs["worksheet_number"],
                                                          check_number=self.kwargs["check_number"]).order_by('-dateTime_check')}

    def get_success_url(self, **kwargs):
        url = reverse(self.view_name,
                      kwargs={'worksheet_number': self.kwargs['worksheet_number'],
                              'check_number': self.kwargs['check_number'],
                              'check_description': self.kwargs['check_description'],
                              'barcode_count':  self.kwargs['barcode_count']})
        return url