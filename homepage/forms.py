from django import forms

# CheckForms are initialised using records from the CheckTable.
# Initial value for url_name and choices value for barcode_count fields are added in the homepage view.
# Submitting the form takes the user to the check view following url_name/barcode_count
class CheckForm(forms.Form):
    url_name = forms.CharField(widget=forms.HiddenInput(), initial="")
    barcode_count = forms.ChoiceField(required=True, label='Barcodes to check', choices={})
