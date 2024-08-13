from django import forms
from match_all_check.models import *



class BarcodeForm(forms.ModelForm):
    barcode = forms.CharField()

    class Meta:
        model = MatchAllBarcode
        fields = ('barcode',)