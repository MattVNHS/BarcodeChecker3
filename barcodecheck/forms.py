from django import forms
from barcodecheck.models import *

class CheckForm(forms.ModelForm):
    worksheet = forms.CharField()
    class Meta:
        model = Check
        fields = ('worksheet',)


class BarcodeCheckForm(forms.ModelForm):
    barcode = forms.CharField()
    class Meta:
        model = Barcode
        fields = ('barcode',)




