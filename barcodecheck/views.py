from barcodecheck.forms import *
from barcodecheck.models import *
from django.views.generic.edit import FormView
from django.forms import formset_factory,  modelformset_factory


class BarcodecheckFormView(FormView):
    template_name = 'barcodecheck/barcodecheck.html'
    model = Barcodes
    success_url = '/'

    ''' BarcodecheckFormView defines the FormView class, to create the appropriate number of barcode check forms I
    edited the get_form_class() method. 
    I used formset_factory to create a formset from the BarcodeCheckForm and passed the extra parameter to create the 
    required number for BarcodeCheckForm forms. self.kwargs['barcode_count'] is passed in the url. 
    This way the required number of barcodes to be checked can be passed in the url.
    https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_class
    Accessed kwargs following this: https://stackoverflow.com/questions/34462739/use-url-parameter-in-class-based-view-django'''

    def get_form_class(self, **kwargs):
        form_class = formset_factory(BarcodeCheckForm, extra=self.kwargs['barcode_count'])
        return form_class

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        check_user = self.request.user
        check_instance = Check.objects.create(user=check_user,
            worksheet=self.request.POST['worksheet'],
            barcode_count=self.request.POST['form-TOTAL_FORMS'])

        barcode_list = [x.cleaned_data['barcode'] for x in form]
        if all(x == barcode_list[0] for x in barcode_list):
            check_instance.check_pass = True

        for form_instance in form:
            obj = form_instance.save(commit=False)
            obj.Check = check_instance
            obj.save()

        return super().form_valid(form)

