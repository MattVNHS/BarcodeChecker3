from django import forms
from match_all_check.models import *

# BarcodeForm defines the basic barcode form for use in our formset factories


class BarcodeForm(forms.ModelForm):
    barcode = forms.CharField()

    class Meta:
        model = MatchAllBarcode
        fields = ('barcode',)