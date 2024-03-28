from django import forms
from barcodecheck.models import *
from django.forms.models import inlineformset_factory


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


CheckFormset = inlineformset_factory(
    Check, Barcode, fields=('barcode',), can_delete_extra=False, form=BarcodeCheckForm,)






