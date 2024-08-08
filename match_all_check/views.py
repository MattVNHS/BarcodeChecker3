from django.urls import reverse

from match_all_check.forms import *
from match_all_check.models import *
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# For checks with a worksheet we add 'worksheet' to the fields attribute.


@method_decorator(login_required, name='dispatch')
class MatchAllCheckView(CreateView):
    model = MatchAllCheck
    fields = []
    template_name = 'match_all_check/match_all_check.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['barcodes'] = postFormset(self.request.POST)
        else:
            data["barcodes"] = getFormset(self.kwargs['barcode_count'])
        return data

    def form_invalid(self, form):
        barcodes = self.get_context_data()['barcodes']
        messages.warning(self.request, form.errors)
        for error in barcodes.errors:
            messages.warning(self.request, error)
        return self.render_to_response(self.get_context_data(form=form, formset=barcodes))

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
class MatchAllCheckWorksheetView(CreateView):
    model = MatchAllCheck
    fields = []
    template_name = 'match_all_check/match_all_check.html'

    def get_success_url(self, **kwargs):
        #worksheet_number, check_number, barcode_count = self.kwargs['worksheet_number'], self.kwargs['check_number'], self.kwargs['barcode_count']
        url = reverse('MatchAllCheckWorksheetView', kwargs={'worksheet_number': self.kwargs['worksheet_number'],
                                                      'check_number': self.kwargs['check_number'],
                                                      'barcode_count':  self.kwargs['barcode_count']})

        return url

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['total_forms'] = int(self.request.POST['matchallbarcode_set-TOTAL_FORMS'])
            data['barcodes'] = postFormset(self.request.POST)
            data["worksheet_number"], data["check_number"], data["check_description"] = (
                self.kwargs['worksheet_number'], self.kwargs['check_number'], self.kwargs['check_description'])
            data["check_record"] = MatchAllCheck.objects.filter(worksheet=data["worksheet_number"])
        else:
            data["barcodes"] = getFormset(self.kwargs['barcode_count'])
            data["worksheet_number"], data["check_number"], data["check_description"] = (
                self.kwargs['worksheet_number'], self.kwargs['check_number'], self.kwargs['check_description'])
            data["check_record"] = MatchAllCheck.objects.filter(worksheet=data["worksheet_number"])
        return data

    def form_invalid(self, form):
        barcodes = self.get_context_data()['barcodes']
        messages.warning(self.request, form.errors)
        for error in barcodes.errors:
            messages.warning(self.request, error)
        return self.render_to_response(self.get_context_data(form=form, formset=barcodes))

    def form_valid(self, form):
        context = self.get_context_data()
        barcodes = context['barcodes']
        worksheet_number = context["worksheet_number"]
        print(worksheet_number)
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.worksheet, created = Worksheet.objects.get_or_create(worksheet_number=worksheet_number)
        self.object.check_number =context["check_number"]
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

