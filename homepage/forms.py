from django import forms

# the hidden url_name field in each form has the initial parameter set to the url name for the intended view.
# submitting the form takes the user to the view with the barcode_count parameter.

class Match_all_Form(forms.Form):
    url_name = forms.CharField(widget=forms.HiddenInput(), initial="MatchAllCheckView")
    barcode_count = forms.ChoiceField(required=True, label='Barcodes to check',
                                           choices={i: i for i in range(2,11,2)})


class Match_all_worksheet_Form(forms.Form):
    url_name = forms.CharField(widget=forms.HiddenInput(), initial="MatchAllCheckWorksheetView")
    barcode_count = forms.ChoiceField(required=True, label='Barcodes to check',
                                           choices={i: i for i in range(2,11,2)})


class Match_pair_Form(forms.Form):
    url_name = forms.CharField(widget=forms.HiddenInput(), initial="MatchPairCheckView")
    barcode_count = forms.ChoiceField(required=True, label='Barcodes to check',
                                           choices={i: i for i in range(8,25,8)})

