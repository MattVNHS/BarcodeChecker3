from django.forms import HiddenInput
from match_all_check.forms import *
from base_check.forms import *

# BarcodeForm defines the basic barcode form for use in our formset factories


class BarcodePairForm(forms.ModelForm):
    barcode = forms.CharField()

    class Meta:
        model = MatchPairBarcode
        fields = ('barcode', 'comparisonId')
        widgets = {
            'comparisonId': HiddenInput(),
        }

# BaseInlineCheckFormSet is defined in Match_all_check.forms
# define inlineformset_factories for GET and POST requests to be used in our views.


def getFormset(barcode_count):
    return inlineformset_factory(
        MatchPairCheck, MatchPairBarcode, formset=BaseInlineCheckFormSet, can_delete_extra=False, form=BarcodePairForm, extra=barcode_count)


postFormset = inlineformset_factory(
    MatchPairCheck, MatchPairBarcode, can_delete_extra=False, form=BarcodePairForm, formset=BaseInlineCheckFormSet, extra=0)



