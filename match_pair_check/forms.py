from django import forms
from django.forms import HiddenInput
from match_pair_check.models import *

# BarcodePairForm defines the basic barcode form for use in our formset factories

# Why isnt this in base check?
class BarcodePairForm(forms.ModelForm):
    barcode = forms.CharField()
    form_index = None

    class Meta:
        model = MatchPairBarcode
        fields = ('barcode', 'comparisonId')
        widgets = {
            'comparisonId': HiddenInput(),
        }

class MatchPairForm(forms.ModelForm):
    worksheet_number = forms.CharField(max_length=12, label="Worksheet Number")

    class Meta:
        model = MatchPairCheck
        fields = ['worksheet_number', 'check_number', 'check_description']

    def save(self, commit=True):
        worksheet_number = self.cleaned_data['worksheet_number']
        worksheet, created = Worksheet.objects.get_or_create(worksheet_number=worksheet_number)
        check = super().save(commit=False)
        check.worksheet = worksheet
        if commit:
            check.save()
        return check

