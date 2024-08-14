from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib import messages
from base_check.forms import *
from base_check.models import *

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
    fields = ['worksheet', 'check_number', 'check_description']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        if self.request.POST:
            post = self.request.POST
            data['barcodes'] = post_formset(post, self.model, self.barcode_model, self.barcode_form)
            data["check_number"], data["check_description"] = post['check_number'], post['check_description']
            data["worksheet_number"], data['total_forms'] = post['worksheet'], data['barcodes'].total_form_count()
            data["check_record"] = self.model.objects.filter(worksheet=data["worksheet_number"], check_number=data["check_number"])
        else:
            data["barcodes"] = get_formset(self.kwargs['barcode_count'], self.model, self.barcode_model, self.barcode_form)
        return data

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
            data["check_record"] = self.model.objects.filter(worksheet=data["worksheet_number"], check_number=data["check_number"])
        else:
            data["worksheet_number"], data["check_number"], data["check_description"] = (
                self.kwargs['worksheet_number'], self.kwargs['check_number'], self.kwargs['check_description'])
            data["barcodes"] = get_formset(self.kwargs['barcode_count'], self.model, self.barcode_model, self.barcode_form)
            if "worksheet_number" in data:
                data["check_record"] = self.model.objects.filter(worksheet=data["worksheet_number"], check_number=data["check_number"])
        return data

    def form_invalid(self, form):
        barcodes = self.get_context_data()['barcodes']
        messages.warning(self.request, form.errors)
        for error in barcodes.errors:
            messages.warning(self.request, error)
        return self.render_to_response(self.get_context_data(form=form, formset=barcodes))


from django.db.models import Q
from match_all_check.models import MatchAllCheck


class AuditView(ListView):
    model = MatchAllCheck
    template_name = 'base_check/base_audit.html'
    #paginate_by = 10  # if pagination is desired

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = self.model.objects.filter(
            Q(worksheet__worksheet_number__icontains=query) | Q(user__username__icontains=query)
        )
        return object_list

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

