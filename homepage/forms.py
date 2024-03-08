from django import forms

class BarcodeForm(forms.Form):
    barcode_count = forms.ChoiceField(required=True, label='Barcodes to check',
                                           choices={i: i for i in range(0,11,2)})

class QiasymphonyForm(forms.Form):
    barcode_count = forms.ChoiceField(required=True, label='Barcodes to check',
                                           choices={i: i for i in range(8,25,8)})

