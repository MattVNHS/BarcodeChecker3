from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib import messages
from base_check.forms import *
from base_check.models import Worksheet
from operator import attrgetter

# Base views for using in specific check apps


class CheckView(CreateView):
    template_name = 'base_check/base_check.html'
    fields = []
    barcode_model = None
    barcode_form = None

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['barcodes'] = post_formset(self.request.POST, self.model, self.barcode_model, self.barcode_form)
        else:
            data["barcodes"] = get_formset(self.kwargs['barcode_count'], self.model, self.barcode_model, self.barcode_form)
        return data

    def form_invalid(self, form):
        barcodes = self.get_context_data()['barcodes']
        messages.warning(self.request, form.errors)
        for error in barcodes.errors:
            messages.warning(self.request, error)
        return self.render_to_response(self.get_context_data(form=form, formset=barcodes))


class WorksheetCheckView(CreateView):
    template_name = 'base_check/base_check.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        if self.request.POST:
            post = self.request.POST
            data['barcodes'] = post_formset(post, self.model, self.barcode_model, self.barcode_form)
            data["check_number"], data["check_description"] = post['check_number'], post['check_description']
            data["worksheet_number"], data['total_forms'] = post['worksheet_number'], data['barcodes'].total_form_count()
            check_record = self.model.objects.filter(worksheet=data["worksheet_number"],
                                                     check_number=data["check_number"])
            data["check_record"] = sorted(check_record, key=attrgetter('dateTime_check'), reverse=True)
        else:
            data["barcodes"] = get_formset(self.kwargs['barcode_count'], self.model, self.barcode_model, self.barcode_form)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        barcodes = context['barcodes']
        worksheet_number = context["worksheet_number"]

        # Hook for validation
        validation_error = self.validate_barcodes(barcodes)
        if validation_error:
            messages.warning(self.request, validation_error)
            return self.form_invalid(form)

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.worksheet, created = Worksheet.objects.get_or_create(worksheet_number=worksheet_number)
        self.object.check_number = context["check_number"]
        self.object.check_description = context["check_description"]

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


    def form_invalid(self, form):
        barcodes = self.get_context_data()['barcodes']
        messages.warning(self.request, form.errors)
        for error in barcodes.errors:
            messages.warning(self.request, error)
        return self.render_to_response(self.get_context_data(form=form, formset=barcodes))


class AssignedMatchAllWorksheetCheck(CreateView):
    template_name = 'base_check/base_check.html'
    fields = []

    def get_success_url(self, **kwargs):
        url = reverse('WorksheetMatchAllView',
                      kwargs={'worksheet_number': self.kwargs['worksheet_number'],
                              'check_number': self.kwargs['check_number'],
                              'check_description': self.kwargs['check_description'],
                              'barcode_count':  self.kwargs['barcode_count']})
        return url

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        if self.request.POST:
            data["check_number"], data["check_description"] = self.kwargs['check_number'], self.kwargs[
                'check_description']
            data['barcodes'] = post_formset(self.request.POST, self.model, self.barcode_model, self.barcode_form)
            data["worksheet_number"], data['total_forms'] = self.kwargs['worksheet_number'], data['barcodes'].total_form_count()
            check_record = self.model.objects.filter(worksheet=data["worksheet_number"],
                                                     check_number=data["check_number"])
            data["check_record"] = sorted(check_record, key=attrgetter('dateTime_check'), reverse=True)
        else:
            data["worksheet_number"], data["check_number"], data["check_description"] = (
                self.kwargs['worksheet_number'], self.kwargs['check_number'], self.kwargs['check_description'])
            data["barcodes"] = get_formset(self.kwargs['barcode_count'], self.model, self.barcode_model, self.barcode_form)
            if "worksheet_number" in data:
                check_record = self.model.objects.filter(worksheet=data["worksheet_number"], check_number=data["check_number"])
                data["check_record"] = sorted(check_record, key=attrgetter('dateTime_check'), reverse=True)
        return data

    def form_invalid(self, form):
        barcodes = self.get_context_data()['barcodes']
        messages.warning(self.request, form.errors)
        for error in barcodes.errors:
            messages.warning(self.request, error)
        return self.render_to_response(self.get_context_data(form=form, formset=barcodes))




