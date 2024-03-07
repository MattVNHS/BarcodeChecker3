from django import forms

class QiasymphonyForm(forms.Form):
    barcode_count = forms.ChoiceField(required=True, label='Barcode to check',
                                           choices=[(8, "8"), (16, "16"),
                                                   (24, "24"), ("Other", "Other")])
