from django import forms
from account.models import BarcodeChecker

class Barcodecheck2Form(forms.ModelForm):
    barcodecheck2_value1 = forms.CharField(max_length=10)
    barcodecheck2_value2 = forms.CharField(max_length=10)

    class Meta:
        model = BarcodeChecker
        fields = (barcodecheckfunction, user, dateTime_check, worksheet, barcode1, barcode2)



