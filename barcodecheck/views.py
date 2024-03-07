from barcodecheck.forms import *
from barcodecheck.models import *
from django.views.generic.edit import FormView
from django.forms import formset_factory


class BarcodecheckFormView(FormView):
    template_name = 'barcodecheck/barcodecheck.html'
    model = Barcode
    success_url = '/'

    ''' BarcodecheckFormView defines the FormView class, to create the appropriate number of barcode check forms I
    edited the get_form_class() method. 
    I used formset_factory to create a formset from the BarcodeCheckForm and passed the extra parameter to create the 
    required number of BarcodeCheckForm forms. self.kwargs['barcode_count'] is passed in the url. 
    This way the required number of barcodes to be checked can be passed in the url.
    https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_class
    Accessed kwargs following this: https://stackoverflow.com/questions/34462739/use-url-parameter-in-class-based-view-django'''

    def get_form_class(self, **kwargs):
        form_class = formset_factory(BarcodeCheckForm, extra=self.kwargs['barcode_count'])
        return form_class

    def form_valid(self, form):
        ''' Create a check instance '''
        check_user = self.request.user
        check_instance = Check.objects.create(user=check_user,
            worksheet=self.request.POST['worksheet'],
            barcode_count=self.request.POST['form-TOTAL_FORMS'])

        ''' validate all barcodes match e.g. check_pass True or False? '''
        barcode_list = [x.cleaned_data['barcode'] for x in form]
        if all(x == barcode_list[0] for x in barcode_list):
            check_instance.check_pass = True

        ''' assign check_instance to Barcodes  '''
        for form_instance in form:
            barcode_instance = form_instance.save(commit=False)
            barcode_instance.Check = check_instance
            barcode_instance.save()

        return super().form_valid(form)

