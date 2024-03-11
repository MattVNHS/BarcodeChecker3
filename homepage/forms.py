from django import forms

class BarcodeForm(forms.Form):
    url_name = forms.CharField(widget=forms.HiddenInput(), initial="barcodecheck")
    barcode_count = forms.ChoiceField(required=True, label='Barcodes to check',
                                           choices={i: i for i in range(2,11,2)})

class QiasymphonyForm(forms.Form):
    url_name = forms.CharField(widget=forms.HiddenInput(), initial="Qiasymphony")
    barcode_count = forms.ChoiceField(required=True, label='Barcodes to check',
                                           choices={i: i for i in range(8,25,8)})

