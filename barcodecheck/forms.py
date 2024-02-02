from django import forms
from barcodecheck.models import BarcodeCheck
from django.contrib.auth import authenticate
from datetime import datetime


class BarcodeCheck2Form(forms.ModelForm):
    worksheet = forms.CharField(required=True, help_text='Required')
    barcode1 = forms.CharField(required=True, help_text='Required')
    barcode2 = forms.CharField(required=True, help_text='Required')
    barcodecheck_result = forms.CharField()

    class Meta:
        model = BarcodeCheck
        fields = ('barcodecheckid', 'worksheet', 'barcode1', 'barcode2', 'barcodecheck_result')
