from django import forms
from django.forms import HiddenInput
from match_pair_check.models import *
class BarcodePairForm(forms.ModelForm):
    barcode = forms.CharField()

    class Meta:
        model = MatchPairBarcode
        fields = ('barcode', 'comparisonId')
        widgets = {
            'comparisonId': HiddenInput(),
        }