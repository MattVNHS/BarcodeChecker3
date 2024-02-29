from django import forms
from barcodecheck.models import *


class CheckForm(forms.ModelForm):
    worksheet = forms.CharField(required=True, help_text='Required')
    class Meta:
        model = Check
        fields = ('worksheet',)


class SampleCheckForm(forms.ModelForm):
    barcode = forms.CharField(required=True, help_text='Required', label='sample')
    class Meta:
        model = Barcodes
        fields = ('barcode',)

class ElutionCheckForm(forms.ModelForm):
    barcode = forms.CharField(required=True, help_text='Required', label='elution')
    class Meta:
        model = Barcodes
        fields = ('barcode',)


class QiasymphonyCheckForm(forms.Form):
    sample_barcode = forms.CharField(required=True, help_text='Required', label='sample')
    elution_barcode = forms.CharField(required=True, help_text='Required', label='elution')


