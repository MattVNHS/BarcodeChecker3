from django import forms
from culturemethods.models import CultureCheck
from django.contrib.auth import authenticate
from datetime import datetime


class CultureCheck3Form(forms.ModelForm):
    culturecheck_method = forms.CharField(required=True, help_text='Required')
    culturecheckbarcode1 = forms.CharField(required=True, help_text='Required')
    culturecheckbarcode2 = forms.CharField(required=True, help_text='Required')
    culturecheckbarcode3 = forms.CharField(required=True, help_text='Required')
    culturecheck_result = forms.BooleanField(required=False)

    def culturecheck_method(self):
        data = self.cleaned_data['culturecheck_method']
        return data

    def culturecheckbarcode1(self):
        data = self.cleaned_data['culturecheckbarcode1']
        return data

    def culturecheckbarcode2(self):
        data = self.cleaned_data['culturecheckbarcode2']
        return data

    def culturecheckbarcode3(self):
        data = self.cleaned_data['culturecheckbarcode3']
        return data

    def culturecheck_result(self):
        data = self.cleaned_data['slidemaking_result']
        return data


    class Meta:
        model = CultureCheck
        fields = ('culturecheck_method', 'culturecheckbarcode1', 'culturecheckbarcode2', 'culturecheckbarcode3',
                  'culturecheck_result')
