from django import forms
from extractionmethods.models import Qiasymphony24Load
from django.contrib.auth import authenticate
from datetime import datetime


class Qiasymphony24Form(forms.ModelForm):
    Qiasymphony24Load_method = forms.CharField(required=True, help_text='Required')
    Qiasymphony24Load_worksheet = forms.CharField(required=True, help_text='Required')
    Qiasymphony24Check_result = forms.BooleanField(required=False)
    sampletube1 = forms.CharField(required=True, help_text='Required')
    sampletube2 = forms.CharField(required=True, help_text='Required')
    sampletube3 = forms.CharField(required=True, help_text='Required')
    sampletube4 = forms.CharField(required=True, help_text='Required')
    sampletube5 = forms.CharField(required=True, help_text='Required')
    sampletube6 = forms.CharField(required=True, help_text='Required')
    sampletube7 = forms.CharField(required=True, help_text='Required')
    sampletube8 = forms.CharField(required=True, help_text='Required')
    sampletube9 = forms.CharField(required=True, help_text='Required')
    sampletube10 = forms.CharField(required=True, help_text='Required')
    sampletube11 = forms.CharField(required=True, help_text='Required')
    sampletube12 = forms.CharField(required=True, help_text='Required')
    sampletube13 = forms.CharField(required=True, help_text='Required')
    sampletube14 = forms.CharField(required=True, help_text='Required')
    sampletube15 = forms.CharField(required=True, help_text='Required')
    sampletube16 = forms.CharField(required=True, help_text='Required')
    sampletube17 = forms.CharField(required=True, help_text='Required')
    sampletube18 = forms.CharField(required=True, help_text='Required')
    sampletube19 = forms.CharField(required=True, help_text='Required')
    sampletube20 = forms.CharField(required=True, help_text='Required')
    sampletube21 = forms.CharField(required=True, help_text='Required')
    sampletube22 = forms.CharField(required=True, help_text='Required')
    sampletube23 = forms.CharField(required=True, help_text='Required')
    sampletube24 = forms.CharField(required=True, help_text='Required')
    elutiontube1 = forms.CharField(required=True, help_text='Required')
    elutiontube2 = forms.CharField(required=True, help_text='Required')
    elutiontube3 = forms.CharField(required=True, help_text='Required')
    elutiontube4 = forms.CharField(required=True, help_text='Required')
    elutiontube5 = forms.CharField(required=True, help_text='Required')
    elutiontube6 = forms.CharField(required=True, help_text='Required')
    elutiontube7 = forms.CharField(required=True, help_text='Required')
    elutiontube8 = forms.CharField(required=True, help_text='Required')
    elutiontube9 = forms.CharField(required=True, help_text='Required')
    elutiontube10 = forms.CharField(required=True, help_text='Required')
    elutiontube11 = forms.CharField(required=True, help_text='Required')
    elutiontube12 = forms.CharField(required=True, help_text='Required')
    elutiontube13 = forms.CharField(required=True, help_text='Required')
    elutiontube14 = forms.CharField(required=True, help_text='Required')
    elutiontube15 = forms.CharField(required=True, help_text='Required')
    elutiontube16 = forms.CharField(required=True, help_text='Required')
    elutiontube17 = forms.CharField(required=True, help_text='Required')
    elutiontube18 = forms.CharField(required=True, help_text='Required')
    elutiontube19 = forms.CharField(required=True, help_text='Required')
    elutiontube20 = forms.CharField(required=True, help_text='Required')
    elutiontube21 = forms.CharField(required=True, help_text='Required')
    elutiontube22 = forms.CharField(required=True, help_text='Required')
    elutiontube23 = forms.CharField(required=True, help_text='Required')
    elutiontube24 = forms.CharField(required=True, help_text='Required')

    def clean_Qiasymphony24Load_worksheet(self):
        data = self.cleaned_data['Qiasymphony24Load_worksheet']
        return data

    def clean_sampletube1(self):
        data = self.cleaned_data['sampletube1']
        return data
    def clean_sampletube2(self):
        data = self.cleaned_data['sampletube2']
        return data
    def clean_sampletube3(self):
        data = self.cleaned_data['sampletube3']
        return data
    def clean_sampletube4(self):
        data = self.cleaned_data['sampletube4']
        return data
    def clean_sampletube5(self):
        data = self.cleaned_data['sampletube5']
        return data
    def clean_sampletube6(self):
        data = self.cleaned_data['sampletube6']
        return data
    def clean_sampletube7(self):
        data = self.cleaned_data['sampletube7']
        return data
    def clean_sampletube8(self):
        data = self.cleaned_data['sampletube8']
        return data
    def clean_sampletube9(self):
        data = self.cleaned_data['sampletube9']
        return data
    def clean_sampletube10(self):
        data = self.cleaned_data['sampletube10']
        return data
    def clean_sampletube11(self):
        data = self.cleaned_data['sampletube11']
        return data
    def clean_sampletube12(self):
        data = self.cleaned_data['sampletube12']
        return data
    def clean_sampletube13(self):
        data = self.cleaned_data['sampletube13']
        return data
    def clean_sampletube14(self):
        data = self.cleaned_data['sampletube14']
        return data
    def clean_sampletube15(self):
        data = self.cleaned_data['sampletube15']
        return data
    def clean_sampletube16(self):
        data = self.cleaned_data['sampletube16']
        return data
    def clean_sampletube17(self):
        data = self.cleaned_data['sampletube17']
        return data
    def clean_sampletube18(self):
        data = self.cleaned_data['sampletube18']
        return data
    def clean_sampletube19(self):
        data = self.cleaned_data['sampletube19']
        return data
    def clean_sampletube20(self):
        data = self.cleaned_data['sampletube20']
        return data
    def clean_sampletube21(self):
        data = self.cleaned_data['sampletube21']
        return data
    def clean_sampletube22(self):
        data = self.cleaned_data['sampletube22']
        return data
    def clean_sampletube23(self):
        data = self.cleaned_data['sampletube23']
        return data
    def clean_sampletube24(self):
        data = self.cleaned_data['sampletube24']
        return data
    def clean_elutiontube1(self):
        data = self.cleaned_data['elutiontube1']
        return data
    def clean_elutiontube2(self):
        data = self.cleaned_data['elutiontube2']
        return data
    def clean_elutiontube3(self):
        data = self.cleaned_data['elutiontube3']
        return data
    def clean_elutiontube4(self):
        data = self.cleaned_data['elutiontube4']
        return data
    def clean_elutiontube5(self):
        data = self.cleaned_data['elutiontube5']
        return data
    def clean_elutiontube6(self):
        data = self.cleaned_data['elutiontube6']
        return data
    def clean_elutiontube7(self):
        data = self.cleaned_data['elutiontube7']
        return data
    def clean_elutiontube8(self):
        data = self.cleaned_data['elutiontube8']
        return data
    def clean_elutiontube9(self):
        data = self.cleaned_data['elutiontube9']
        return data
    def clean_elutiontube10(self):
        data = self.cleaned_data['elutiontube10']
        return data
    def clean_elutiontube11(self):
        data = self.cleaned_data['elutiontube11']
        return data
    def clean_elutiontube12(self):
        data = self.cleaned_data['elutiontube12']
        return data
    def clean_elutiontube13(self):
        data = self.cleaned_data['elutiontube13']
        return data
    def clean_elutiontube14(self):
        data = self.cleaned_data['elutiontube14']
        return data
    def clean_elutiontube15(self):
        data = self.cleaned_data['elutiontube15']
        return data
    def clean_elutiontube16(self):
        data = self.cleaned_data['elutiontube16']
        return data
    def clean_elutiontube17(self):
        data = self.cleaned_data['elutiontube17']
        return data
    def clean_elutiontube18(self):
        data = self.cleaned_data['elutiontube18']
        return data
    def clean_elutiontube19(self):
        data = self.cleaned_data['elutiontube19']
        return data
    def clean_elutiontube20(self):
        data = self.cleaned_data['elutiontube20']
        return data
    def clean_elutiontube21(self):
        data = self.cleaned_data['elutiontube21']
        return data
    def clean_elutiontube22(self):
        data = self.cleaned_data['elutiontube22']
        return data
    def clean_elutiontube23(self):
        data = self.cleaned_data['elutiontube23']
        return data
    def clean_elutiontube24(self):
        data = self.cleaned_data['elutiontube24']
        return data

    class Meta:
        model = Qiasymphony24Load
        fields = ('Qiasymphony24Load_id', 'Qiasymphony24Load_worksheet', 'Qiasymphony24Load_method',
                  'Qiasymphony24Check_result', 'sampletube1', 'sampletube2', 'sampletube3', 'sampletube4',
                  'sampletube5', 'sampletube6', 'sampletube7', 'sampletube8', 'sampletube9', 'sampletube10',
                  'sampletube11', 'sampletube12', 'sampletube13', 'sampletube14', 'sampletube15', 'sampletube16',
                  'sampletube17', 'sampletube18', 'sampletube19', 'sampletube20', 'sampletube21', 'sampletube22',
                  'sampletube23', 'sampletube24', 'elutiontube1', 'elutiontube2', 'elutiontube3', 'elutiontube4',
                  'elutiontube5', 'elutiontube6', 'elutiontube7', 'elutiontube8', 'elutiontube9', 'elutiontube10',
                  'elutiontube11', 'elutiontube12', 'elutiontube13', 'elutiontube14', 'elutiontube15', 'elutiontube16',
                  'elutiontube17', 'elutiontube18', 'elutiontube19', 'elutiontube20', 'elutiontube21', 'elutiontube22',
                  'elutiontube23', 'elutiontube24')
