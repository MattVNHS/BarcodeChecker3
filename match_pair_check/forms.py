from django import forms
from django.forms import HiddenInput
from match_pair_check.models import *

# BarcodePairForm defines the basic barcode form for use in our formset factories


class BarcodePairForm(forms.ModelForm):
    barcode = forms.CharField()

    class Meta:
        model = MatchPairBarcode
        fields = ('barcode', 'comparisonId')
        widgets = {
            'comparisonId': HiddenInput(),
        }