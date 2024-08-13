from django import forms

# the hidden url_name field in each form has the initial parameter set to the url name for the intended view.
# submitting the form takes the user to the view with the barcode_count parameter.


class MatchAllForm(forms.Form):
    url_name = forms.CharField(widget=forms.HiddenInput(), initial="MatchAllView")
    barcode_count = forms.ChoiceField(required=True, label='Barcodes to check',
                                           choices={i: i for i in range(2, 11, 2)})


class MatchAllWorksheetForm(forms.Form):
    url_name = forms.CharField(widget=forms.HiddenInput(), initial="WorksheetMatchAllView")
    barcode_count = forms.ChoiceField(required=True, label='Barcodes to check',
                                           choices={i: i for i in range(2, 11, 2)})


class MatchPairForm(forms.Form):
    url_name = forms.CharField(widget=forms.HiddenInput(), initial="WorksheetMatchPairView")
    barcode_count = forms.ChoiceField(required=True, label='Barcodes to check',
                                           choices={i: i for i in range(8, 25, 8)})

