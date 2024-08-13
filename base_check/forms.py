from django import forms
from match_all_check.models import *
from django.forms.models import inlineformset_factory
from django.forms import BaseInlineFormSet
from django.forms import HiddenInput
from django.core.exceptions import ValidationError

# BarcodeForm defines the basic barcode form for use in our formset factories


class BarcodeForm(forms.ModelForm):
    barcode = forms.CharField()

    class Meta:
        model = MatchAllBarcode
        fields = ('barcode',)


class BarcodePairForm(forms.ModelForm):
    barcode = forms.CharField()

    class Meta:
        model = MatchPairBarcode
        fields = ('barcode', 'comparisonId')
        widgets = {
            'comparisonId': HiddenInput(),
        }


# BaseInlineCheckFormSet overwrites BaseInlineFormSet.clean() method to add validation at the formset level

class BaseInlineCheckFormSet(BaseInlineFormSet):
    def clean(self):
        if any(self.errors):
            # if any errors at the individual form level, stop, no need to do extra validation - e.g. invalid barcode entered.
            return
        barcode_list = []
        for form in self.forms:
            barcode = form.cleaned_data.get("barcode")
            barcode_list.append(barcode)
        barcodes_entered = [x for x in barcode_list if x is not None]

        # validate barcodes in order without gaps and allowing empty values at the end of the list
        for x in range(1, len(barcode_list)):
            if barcode_list[x - 1] is None and barcode_list[x] is not None:
                self.errors.append("Cannot have a gap in the barcodes entered")
                raise ValidationError("Cannot have a gap in the barcodes entered")
        # validate >1 barcodes added
        if len(barcodes_entered) <= 1:
            self.errors.append("Must enter more than one barcode")
            raise ValidationError("Must enter more than one barcode")
        if len(barcodes_entered) != len(self.forms):
            # error = ValidationError(f"only {len(barcodes_entered)} of {len(self.forms)} barcodes added")
            # self._non_form_errors.append(error)
            self.errors.append(f"only {len(barcodes_entered)} of {len(self.forms)} barcodes added")
            #self.forms[0].add_error(field=None, error=f"only {len(barcodes_entered)} of {len(self.forms)} barcodes added")


# define inlineformset_factories for GET and POST requests to be used in our views.


def getFormset(barcode_count, check_model, barcode_model, barcode_form):
    return inlineformset_factory(
        check_model, barcode_model, can_delete_extra=False, form=barcode_form, formset=BaseInlineCheckFormSet, extra=barcode_count)


def postFormset(request, check_model, barcode_model, barcode_form):
    formset = inlineformset_factory(
     check_model, barcode_model, can_delete_extra=False, form=barcode_form, formset=BaseInlineCheckFormSet, extra=0)
    return formset(request)



