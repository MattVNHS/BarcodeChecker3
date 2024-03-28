from django import forms

class Match_all_Form(forms.Form):
    url_name = forms.CharField(widget=forms.HiddenInput(), initial="match_all_check")
    barcode_count = forms.ChoiceField(required=True, label='Barcodes to check',
                                           choices={i: i for i in range(2,11,2)})

class Match_pair_Form(forms.Form):
    url_name = forms.CharField(widget=forms.HiddenInput(), initial="match_pair_check")
    barcode_count = forms.ChoiceField(required=True, label='Barcodes to check',
                                           choices={i: i for i in range(8,25,8)})

