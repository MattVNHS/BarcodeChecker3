from django import forms
from match_all_check.models import *

# BarcodeForm defines the basic barcode form for use in our formset factories

# Why isnt this in base check?
class BarcodeForm(forms.ModelForm):
    barcode = forms.CharField()
    form_index = None

    class Meta:
        model = MatchAllBarcode
        fields = ('barcode',)


class MatchAllForm(forms.ModelForm):
    worksheet_number = forms.CharField(max_length=12, label="Worksheet Number")

    class Meta:
        model = MatchAllCheck
        fields = ['worksheet_number', 'check_number', 'check_description']

    def save(self, commit=True):
        worksheet_number = self.cleaned_data['worksheet_number']
        worksheet, created = Worksheet.objects.get_or_create(worksheet_number=worksheet_number)
        check = super().save(commit=False)
        check.worksheet = worksheet
        if commit:
            check.save()
        return check
