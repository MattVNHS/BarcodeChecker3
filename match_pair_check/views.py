from match_pair_check.forms import *
from match_all_check.models import *
from match_all_check.forms import *
from django.views.generic.edit import FormView
from django.forms import formset_factory



class QiasymphonyFormView(FormView):
    template_name = 'match_pair_check/QiasymphonyCheck.html'
    model = Barcode
    success_url = '/'

    def get_form_class(self, **kwargs):
        form_class = formset_factory(QiasymphonyCheckForm, extra=self.kwargs['barcode_count'])
        return form_class

    def form_valid(self, form):
        ''' Create a check instance '''
        check_user = self.request.user
        check_instance = Check.objects.create(user=check_user,
            worksheet=self.request.POST['worksheet'],
            barcode_count=self.request.POST['form-TOTAL_FORMS'])

        ''' create sample_barcodes and elution_barcodes 
          then validate check_pass '''
        barcode_check_list = []
        for form_instance in form:
                sample = Barcode.objects.create(
                    barcode=form_instance.cleaned_data['sample_barcode'],
                    Check=check_instance)
                elution = Barcode.objects.create(
                    barcode=form_instance.cleaned_data['elution_barcode'],
                    Check=check_instance, comparisonId=sample.id)
                sample.comparisonId=elution.id
                sample.save()

                if form_instance.cleaned_data['sample_barcode'] == form_instance.cleaned_data['elution_barcode']:
                    barcode_check_list.append(True)
                else:
                    barcode_check_list.append(False)

        if all(barcode_check_list):
            check_instance.check_pass = True
            check_instance.save()

        return super().form_valid(form)




from match_all_check.forms import *
from match_all_check.models import *
from django.views.generic.edit import CreateView
from django.forms.models import inlineformset_factory
from django.contrib import messages

class Match_pair_checkCreateView(CreateView):
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
            # need to create the form with pairs of forms linked by comparisonId
             data["barcodes"] = inlineformset_factory(Check, Barcode, formset=BaseInlineCheckFormSet, can_delete_extra=False,
                                                      form=BarcodePairForm, extra=self.kwargs['barcode_count'])
             print(data["barcodes"])
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

