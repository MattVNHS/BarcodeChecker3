from django import forms

class QiasymphonyCheckForm(forms.Form):
    sample_barcode = forms.CharField(required=True, help_text='Required', label='sample')
    elution_barcode = forms.CharField(required=True, help_text='Required', label='elution')


