from match_all_check.forms import *
from match_all_check.models import *
from django.views.generic.edit import CreateView
from django.forms.models import inlineformset_factory
from django.contrib import messages

class Match_all_checkCreateView(CreateView):
    model = Check
    fields = ["worksheet",]
    template_name = 'match_all_check/match_all_check.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['total_forms'] = int(self.request.POST['barcode_set-TOTAL_FORMS'])
            data['barcodes'] = CheckFormset(self.request.POST)
        else:
             data["barcodes"] = inlineformset_factory(Check, Barcode, fields=('barcode',), formset=BaseInlineCheckFormSet, can_delete_extra=False,
                                                      form=BarcodeCheckForm, extra=self.kwargs['barcode_count'])
        return data

    def form_invalid(self, form, barcodes):
        for error in barcodes.errors:
            messages.warning(self.request, error)
        return self.render_to_response(self.get_context_data(form=form, formset=barcodes))

    def form_valid(self, form):
        context = self.get_context_data()
        barcodes = context['barcodes']
        self.object = form.save(commit=False)
        self.object.user, self.object.barcode_count = self.request.user, context['total_forms']
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
            return self.form_invalid(form, barcodes)
        return super().form_valid(form)


