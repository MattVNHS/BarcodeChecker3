from django import forms
from barcodecheck.models import BarcodeCheck
from django.contrib.auth import authenticate
from datetime import datetime


class BarcodeCheck2Form(forms.ModelForm):
    worksheet = forms.CharField(required=True, help_text='Required')
    barcode1 = forms.CharField(required=True, help_text='Required')
    barcode2 = forms.CharField(required=True, help_text='Required')
    barcode_check_function = forms.CharField(required=False)
    barcodecheck_result = forms.BooleanField(required=False)


    def clean_barcode1(self):
        data = self.cleaned_data['barcode1']
        return data

    def clean_barcode2(self):
        data = self.cleaned_data['barcode2']
        return data

    def clean_worksheet(self):
        data = self.cleaned_data['worksheet']
        return data

    class Meta:
        model = BarcodeCheck
        fields = ('barcodecheckid', 'worksheet', 'barcode1', 'barcode2', 'barcode_check_function', 'barcodecheck_result')

    # def clean(self):
    #     cleaned_data = super().clean()
    #     cleaned_data['barcode_check_function'] = '2 barcode check'
    #     cleaned_data['barcodecheck_result'] = True
    #     return cleaned_data
