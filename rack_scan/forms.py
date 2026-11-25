from django import forms
from django.core.validators import MinLengthValidator
from shire.models import DNA_EXTRACTSHEET_DET

class ExtractSheetForm(forms.Form):
    ExtractSheet = forms.CharField(max_length=10, label="Extraction Sheet Number",
                                   validators=[MinLengthValidator(6)])

    def clean_ExtractSheet(self):
        sheet = self.cleaned_data["ExtractSheet"]
        if not DNA_EXTRACTSHEET_DET.objects.filter(EXTRACTSHEET=sheet).exists():
            raise forms.ValidationError("No extract sheet with that number.")
        return sheet