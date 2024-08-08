from django.urls import reverse

from match_all_check.forms import *
from match_all_check.models import *
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Base views for using in specific check apps


class CheckView(CreateView):
    fields = []

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


class WorksheetCheckView(CreateView):
    fields = []

    def get_success_url(self, **kwargs):
        url = reverse('MatchAllCheckWorksheetView',
                      kwargs={'worksheet_number': self.kwargs['worksheet_number'],
                              'check_number': self.kwargs['check_number'],
                              'check_description': self.kwargs['check_description'],
                              'barcode_count':  self.kwargs['barcode_count']})
        return url

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["worksheet_number"], data["check_number"], data["check_description"] = (
                 self.kwargs['worksheet_number'], self.kwargs['check_number'], self.kwargs['check_description'])

        if self.request.POST:
            data['total_forms'] = int(self.request.POST['matchallbarcode_set-TOTAL_FORMS'])
            data['barcodes'] = postFormset(self.request.POST)
            data["check_record"] = MatchAllCheck.objects.filter(worksheet=data["worksheet_number"], check_number=data["check_number"])
        else:
            data["barcodes"] = getFormset(self.kwargs['barcode_count'])
            data["check_record"] = MatchAllCheck.objects.filter(worksheet=data["worksheet_number"], check_number=data["check_number"])
        return data

    def form_invalid(self, form):
        barcodes = self.get_context_data()['barcodes']
        messages.warning(self.request, form.errors)
        for error in barcodes.errors:
            messages.warning(self.request, error)
        return self.render_to_response(self.get_context_data(form=form, formset=barcodes))

class AuditView(ListView):
    template_name = 'match_all_check/match_all_check_audit.html'
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

