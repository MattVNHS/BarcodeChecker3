from django.urls import reverse

from match_all_check.forms import *
from match_all_check.models import *
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from base_check.views import *

# For checks with a worksheet we add 'worksheet' to the fields attribute.


@method_decorator(login_required, name='dispatch')
class MatchAllView(CheckView):
    model = MatchAllCheck
    success_url = '/'
    barcode_model = MatchAllBarcode
    barcode_form = BarcodeForm

    def form_valid(self, form):
        context = self.get_context_data()
        barcodes = context['barcodes']
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        if barcodes.is_valid():
            barcodes.instance = self.object
            barcodes.save()
            for error in barcodes.errors:
                messages.warning(self.request, error)
            if self.object.checkPassFail():
                messages.success(self.request, 'Check Passed')
            else:
                messages.warning(self.request, 'Check Failed - Barcodes do not match')
        else:
            return self.form_invalid(form)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class WorksheetMatchAllView(WorksheetCheckView):
    model = MatchAllCheck
    success_url = '/'
    barcode_model = MatchAllBarcode
    barcode_form = BarcodeForm

    def form_valid(self, form):
        context = self.get_context_data()
        barcodes = context['barcodes']
        worksheet_number = context["worksheet_number"]
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.worksheet, created = Worksheet.objects.get_or_create(worksheet_number=worksheet_number)
        self.object.check_number = context["check_number"]
        self.object.check_description = context["check_description"]
        if barcodes.is_valid():
            self.object.save()
            barcodes.instance = self.object
            barcodes.save()
            for error in barcodes.errors:
                messages.warning(self.request, error)
            if self.object.checkPassFail():
                messages.success(self.request, 'Check Passed')
            else:
                messages.warning(self.request, 'Check Failed - Barcodes do not match')
        else:
            return self.form_invalid(form)
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class AssignedMatchAllView(AssignedMatchAllWorksheetCheck):
    model = MatchAllCheck
    success_url = '/'
    barcode_model = MatchAllBarcode
    barcode_form = BarcodeForm

    def form_valid(self, form):
        context = self.get_context_data()
        barcodes = context['barcodes']
        worksheet_number = context["worksheet_number"]
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.worksheet, created = Worksheet.objects.get_or_create(worksheet_number=worksheet_number)
        self.object.check_number = context["check_number"]
        self.object.check_description = context["check_description"]
        if barcodes.is_valid():
            self.object.save()
            barcodes.instance = self.object
            barcodes.save()
            for error in barcodes.errors:
                messages.warning(self.request, error)
            if self.object.checkPassFail():
                messages.success(self.request, 'Check Passed')
            else:
                messages.warning(self.request, 'Check Failed - Barcodes do not match')
        else:
            return self.form_invalid(form)
        return super().form_valid(form)


class MatchAllCheckListView(AuditView):
    model = MatchAllCheck
    template_name = 'match_all_check/base_check_audit.html'
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
