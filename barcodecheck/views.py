from barcodecheck.forms import *
from barcodecheck.models import *
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from django.forms.models import inlineformset_factory
from django.forms import formset_factory
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, reverse
import re

# CreateView is the correct CBV to use when creating an object. inlineformset_factory used to create a nested form with
# one Check object displaying the worksheet field and multiple Barcode objects. form_valid also uses inlineformset_factory
# but references the CheckFormset already defined in forms.py, it can do this with the correct number of extra forms as
# the Check instance has already been created.

class BarcodecheckCreateView(CreateView):
    model = Check
    fields = ["worksheet",]
    template_name = 'barcodecheck/createbarcodecheck.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['total_forms'] = int(self.request.POST['barcode_set-TOTAL_FORMS'])
        else:
            data["barcodes"] = inlineformset_factory(Check, Barcode, fields=('barcode',), can_delete_extra=False,
                                                     form=BarcodeCheckForm, extra=self.kwargs['barcode_count'])
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        current_check = form.save(commit=False)
        current_check.user, current_check.barcode_count = self.request.user, context['total_forms']
        current_check.save()
        barcodes_formset = CheckFormset(self.request.POST, instance=current_check)
        print(barcodes_formset)
        if barcodes_formset.is_valid():
            for barcode in barcodes_formset:
                barcode.save(commit=False)
                barcode.Check = current_check
        barcodes_formset.save()
        return super().form_valid(form)



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

    #def get_context_data(self, **kwargs):
     #   pass

    def get_form_class(self, **kwargs):
        form_class = formset_factory(BarcodeCheckForm, extra=self.kwargs['barcode_count'])
        return form_class

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form, worksheet=self.request.POST['worksheet']))

    def form_valid(self, form):
        total_forms = int(self.request.POST['form-TOTAL_FORMS'])
        barcode_list = [self.request.POST[f"form-{x}-barcode"] for x in range(total_forms)]
        worksheet = self.request.POST['worksheet']

        # validation worksheets
       # if worksheet == '':
        #    messages.warning(self.request, f"No worksheet")
        #elif not re.match(r'^\d{6}$', worksheet):
        #    messages.warning(self.request, f"Invalid worksheet")
        #    return self.render_to_response(self.get_context_data(form=form, worksheet=worksheet))

        # Create a check instance
        check_user = self.request.user
        check_instance = Check.objects.create(user=check_user,
                                              worksheet=worksheet, barcode_count=total_forms)


        # validate barcodes in order without gaps and allowing empty values at the end of the list
        for x in range(1, len(barcode_list)):
            if barcode_list[x - 1] == '' and barcode_list[x] != '':
                messages.warning(self.request, f"cannot have a gap in the barcodes entered")
                return self.render_to_response(self.get_context_data(form=form, worksheet=worksheet))

        if '' in barcode_list:
            barcode_list = barcode_list[0:barcode_list.index('')]
            # validate >1 barcodes added
            if len(barcode_list) <= 1:
                messages.warning(self.request, f"Must enter more than one barcode")
                return self.render_to_response(self.get_context_data(form=form, worksheet=worksheet))

            if len(barcode_list) != total_forms:
                messages.warning(self.request, f"only {len(barcode_list)} of {total_forms} barcodes added")

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


