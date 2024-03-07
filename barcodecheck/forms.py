from django import forms
from barcodecheck.models import *


class CheckForm(forms.ModelForm):
    worksheet = forms.CharField(required=True, help_text='Required')
    class Meta:
        model = Check
        fields = ('worksheet',)


class BarcodeCheckForm(forms.ModelForm):
    barcode = forms.CharField(required=True, help_text='Required')
    class Meta:
        model = Barcode
        fields = ('barcode',)


