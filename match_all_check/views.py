from match_all_check.forms import *
from match_all_check.models import *
from django.views.generic.edit import CreateView
from django.forms.models import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Used the CreateView CBV because we are creating new model instances. For checks without worksheet we remove 'worksheet'
# from the fields attribute. get_context_data if POST: pass the request.POST dictionary as a CheckFormSet stored as data
@method_decorator(login_required, name='dispatch')
class Match_all_checkCreateView(CreateView):
    model = Check
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
            if "Check Failed - Barcodes do not match" not in barcodes.errors:
                messages.success(self.request, 'Check Passed')
                self.object.check_pass = True
                self.object.save()
        else:
            return self.form_invalid(form)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class Match_all_check_worksheetCreateView(CreateView):
    model = Check
    fields = ["worksheet",]
    template_name = 'match_all_check/match_all_check.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['total_forms'] = int(self.request.POST['barcode_set-TOTAL_FORMS'])
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
            if "Check Failed - Barcodes do not match" not in barcodes.errors:
                messages.success(self.request, 'Check Passed')
                self.object.check_pass = True
                self.object.save()
        else:
            return self.form_invalid(form)
        return super().form_valid(form)

