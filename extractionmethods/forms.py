from django import forms
from barcodecheck.models import *

class QiasymphonyCheckForm(forms.Form):
    sample_barcode = forms.CharField(required=True, help_text='Required', label='sample')
    elution_barcode = forms.CharField(required=True, help_text='Required', label='elution')


