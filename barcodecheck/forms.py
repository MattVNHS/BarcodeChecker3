from django import forms
from barcodecheck.models import *
import re
from django.core.exceptions import ValidationError


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

    def clean_barcode(self):
        data = self.cleaned_data['barcode']
        if not re.match(r'^[A-Z]\d{2}[.]\d{5,6}$', data):
            raise ValidationError('invalid lab number entered')
        return data


