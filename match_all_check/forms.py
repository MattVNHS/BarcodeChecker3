from django import forms
from match_all_check.models import *
from django.forms.models import inlineformset_factory
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError


class CheckForm(forms.ModelForm):
    worksheet = forms.CharField()
    class Meta:
        model = Check
        fields = ('worksheet',)


class BarcodeCheckForm(forms.ModelForm):
    barcode = forms.CharField()
    class Meta:
        model = Barcode
        fields = ('barcode',)


class BaseInlineCheckFormSet(BaseInlineFormSet):
    def clean(self):
        if any(self.errors):
            # if any errors at the individual form level
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
            self.errors.append(f"only {len(barcodes_entered)} of {len(self.forms)} barcodes added")
        # validate all barcodes match e.g. check_pass True or False?
        if not all(x == barcodes_entered[0] for x in barcodes_entered):
            self.errors.append("Check Failed - Barcodes do not match")


CheckFormset = inlineformset_factory(
    Check, Barcode, fields=('barcode',), can_delete_extra=False, form=BarcodeCheckForm, formset=BaseInlineCheckFormSet)





