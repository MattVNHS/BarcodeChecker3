from barcodecheck.forms import *
from barcodecheck.models import *
from django.views.generic.edit import FormView
from django.forms import formset_factory
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse


class BarcodecheckFormView(SuccessMessageMixin, FormView):
    template_name = 'barcodecheck/barcodecheck.html'
    model = Barcode
    success_url = '/'
    success_message = "Check passed"

    # BarcodecheckFormView defines the FormView class, to create the appropriate number of barcode check forms I
    # edited the get_form_class() method.
    # I used formset_factory to create a formset from the BarcodeCheckForm and passed the extra parameter to create the
    # required number of BarcodeCheckForm forms. self.kwargs['barcode_count'] is passed in the url.
    # This way the required number of barcodes to be checked can be passed in the url.
    # https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_class
    # Accessed kwargs following this: https://stackoverflow.com/questions/34462739/use-url-parameter-in-class-based-view-django

    def get_form_class(self, **kwargs):
        form_class = formset_factory(BarcodeCheckForm, extra=self.kwargs['barcode_count'])
        return form_class

    def form_valid(self, form):
        total_forms = int(self.request.POST['form-TOTAL_FORMS'])
        barcode_list = [self.request.POST[f"form-{x}-barcode"] for x in range(total_forms)]

        # need to add validation for actual worksheets (can enter anything atm)
        if self.request.POST['worksheet'] =='':
            messages.warning(self.request, f"No worksheet")
            return redirect(self.request.META['HTTP_REFERER'])

        # validate >1 barcodes added, barcodes in order without gaps and allowing empty values at the end of the list
        for x in range(1, len(barcode_list)):
            if barcode_list[x-1] == '' and barcode_list[x] != '':
                messages.warning(self.request, f"cannot have a gap in the barcodes entered")
                return redirect(self.request.META['HTTP_REFERER'])
        if '' in barcode_list:
            barcode_list = barcode_list[0:barcode_list.index('')]

        if len(barcode_list) <= 1:
            messages.warning(self.request, f"Must enter more than one barcode")
            return redirect(self.request.META['HTTP_REFERER'])

        if len(barcode_list) != total_forms:
            messages.warning(self.request, f"only {len(barcode_list)} of {total_forms} barcodes added")
            return redirect(self.request.META['HTTP_REFERER'])

        # Create a check instance
        check_user = self.request.user
        check_instance = Check.objects.create(user=check_user,
                                              worksheet=self.request.POST['worksheet'], barcode_count=total_forms)

        # validate all barcodes match e.g. check_pass True or False?
        if all(x == barcode_list[0] for x in barcode_list):
            check_instance.check_pass = True
            check_instance.save()
        else:
            messages.warning(self.request, f"Check failed")
            check_instance.save()
            return redirect(self.request.META['HTTP_REFERER'])

        # assign check_instance to Barcodes
        for form_instance in form:
            barcode_instance = form_instance.save(commit=False)
            barcode_instance.Check = check_instance
            barcode_instance.save()

        return super().form_valid(form)


def check_modal(request):
    return render(request, 'barcodecheck/checkmodal.html')