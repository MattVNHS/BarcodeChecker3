from extractionmethods.forms import *
from barcodecheck.models import *
from django.views.generic.edit import FormView
from django.forms import formset_factory



class QiasymphonyFormView(FormView):
    template_name = 'extractionmethods/QiasymphonyCheck.html'
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
