from django import forms
from barcodecheck.models import *
from django.contrib.auth import authenticate
from datetime import datetime
import re
from django.core.exceptions import ValidationError


class BarcodeCheckForm(forms.ModelForm):
    barcode = forms.CharField(required=True, help_text='Required')

    class Meta:
        model = Barcodes
        fields = ('barcode',)

#
# class BarcodeCheck2Form(forms.ModelForm):
#     worksheet = forms.CharField(required=True, help_text='Required')
#     barcode1 = forms.CharField(required=True, help_text='Required')
#     barcode2 = forms.CharField(required=True, help_text='Required')
#     barcode_check_method = forms.CharField(required=False)
#     barcodecheck_result = forms.BooleanField(required=False)
#
#     def clean_barcode1(self):
#         data = self.cleaned_data['barcode1']
#         if not re.match(r'^[A-Z]\d{2}[.]\d{5,6}$', 'barcode1'):
#             raise ValidationError('invalid lab number entered')
#         return data
#
#     def clean_barcode2(self):
#         data = self.cleaned_data['barcode2']
#         if not re.match(r'^[A-Z]\d{2}[.]\d{5,6}$', 'barcode2'):
#             raise ValidationError('invalid lab number entered')
#         return data
#
#     def clean_worksheet(self):
#         data = self.cleaned_data['worksheet']
#         return data
#
#     class Meta:
#         model = BarcodeCheck
#         fields = ('barcodecheckid', 'worksheet', 'barcode1', 'barcode2', 'barcode_check_method', 'barcodecheck_result')
#
#
# class BarcodeCheck3Form(forms.ModelForm):
#     worksheet = forms.CharField(required=True, help_text='Required')
#     barcode1 = forms.CharField(required=True, help_text='Required')
#     barcode2 = forms.CharField(required=True, help_text='Required')
#     barcode3 = forms.CharField(required=True, help_text='Required')
#     barcode_check_method = forms.CharField(required=False)
#     barcodecheck_result = forms.BooleanField(required=False)
#
#     def clean_barcode1(self):
#         data = self.cleaned_data['barcode1']
#         return data
#
#     def clean_barcode2(self):
#         data = self.cleaned_data['barcode2']
#         return data
#
#     def clean_barcode3(self):
#         data = self.cleaned_data['barcode3']
#         return data
#
#     def clean_worksheet(self):
#         data = self.cleaned_data['worksheet']
#         return data
#
#     class Meta:
#         model = BarcodeCheck
#         fields = ('barcodecheckid', 'worksheet', 'barcode1', 'barcode2', 'barcode3', 'barcode_check_method',
#                   'barcodecheck_result')
#
#
# class BarcodeCheck4Form(forms.ModelForm):
#     worksheet = forms.CharField(required=True, help_text='Required')
#     barcode1 = forms.CharField(required=True, help_text='Required')
#     barcode2 = forms.CharField(required=True, help_text='Required')
#     barcode3 = forms.CharField(required=True, help_text='Required')
#     barcode4 = forms.CharField(required=True, help_text='Required')
#     barcode_check_method = forms.CharField(required=False)
#     barcodecheck_result = forms.BooleanField(required=False)
#
#     def clean_barcode1(self):
#         data = self.cleaned_data['barcode1']
#         return data
#
#     def clean_barcode2(self):
#         data = self.cleaned_data['barcode2']
#         return data
#
#     def clean_barcode3(self):
#         data = self.cleaned_data['barcode3']
#         return data
#
#     def clean_barcode4(self):
#         data = self.cleaned_data['barcode4']
#         return data
#
#     def clean_worksheet(self):
#         data = self.cleaned_data['worksheet']
#         return data
#
#     class Meta:
#         model = BarcodeCheck
#         fields = ('barcodecheckid', 'worksheet', 'barcode1', 'barcode2', 'barcode3', 'barcode4',
#                   'barcode_check_method', 'barcodecheck_result')
#
# class BarcodeCheck5Form(forms.ModelForm):
#     worksheet = forms.CharField(required=True, help_text='Required')
#     barcode1 = forms.CharField(required=True, help_text='Required')
#     barcode2 = forms.CharField(required=True, help_text='Required')
#     barcode3 = forms.CharField(required=True, help_text='Required')
#     barcode4 = forms.CharField(required=True, help_text='Required')
#     barcode5 = forms.CharField(required=True, help_text='Required')
#     barcode_check_method = forms.CharField(required=False)
#     barcodecheck_result = forms.BooleanField(required=False)
#
#     def clean_barcode1(self):
#         data = self.cleaned_data['barcode1']
#         return data
#
#     def clean_barcode2(self):
#         data = self.cleaned_data['barcode2']
#         return data
#
#     def clean_barcode3(self):
#         data = self.cleaned_data['barcode3']
#         return data
#
#     def clean_barcode4(self):
#         data = self.cleaned_data['barcode4']
#         return data
#
#     def clean_barcode5(self):
#         data = self.cleaned_data['barcode5']
#         return data
#
#     def clean_worksheet(self):
#         data = self.cleaned_data['worksheet']
#         return data
#
#     class Meta:
#         model = BarcodeCheck
#         fields = ('barcodecheckid', 'worksheet', 'barcode1', 'barcode2', 'barcode3', 'barcode4', 'barcode5',
#                   'barcode_check_method', 'barcodecheck_result')
#
#
# class BarcodeCheck6Form(forms.ModelForm):
#     worksheet = forms.CharField(required=True, help_text='Required')
#     barcode1 = forms.CharField(required=True, help_text='Required')
#     barcode2 = forms.CharField(required=True, help_text='Required')
#     barcode3 = forms.CharField(required=True, help_text='Required')
#     barcode4 = forms.CharField(required=True, help_text='Required')
#     barcode5 = forms.CharField(required=True, help_text='Required')
#     barcode6 = forms.CharField(required=True, help_text='Required')
#     barcode_check_method = forms.CharField(required=False)
#     barcodecheck_result = forms.BooleanField(required=False)
#
#     def clean_barcode1(self):
#         data = self.cleaned_data['barcode1']
#         return data
#
#     def clean_barcode2(self):
#         data = self.cleaned_data['barcode2']
#         return data
#
#     def clean_barcode3(self):
#         data = self.cleaned_data['barcode3']
#         return data
#
#     def clean_barcode4(self):
#         data = self.cleaned_data['barcode4']
#         return data
#
#     def clean_barcode5(self):
#         data = self.cleaned_data['barcode5']
#         return data
#
#     def clean_barcode6(self):
#         data = self.cleaned_data['barcode6']
#         return data
#
#     def clean_worksheet(self):
#         data = self.cleaned_data['worksheet']
#         return data
#
#     class Meta:
#         model = BarcodeCheck
#         fields = ('barcodecheckid', 'worksheet', 'barcode1', 'barcode2', 'barcode3', 'barcode4', 'barcode5', 'barcode6',
#                   'barcode_check_method', 'barcodecheck_result')
#
#
# class BarcodeCheck7Form(forms.ModelForm):
#     worksheet = forms.CharField(required=True, help_text='Required')
#     barcode1 = forms.CharField(required=True, help_text='Required')
#     barcode2 = forms.CharField(required=True, help_text='Required')
#     barcode3 = forms.CharField(required=True, help_text='Required')
#     barcode4 = forms.CharField(required=True, help_text='Required')
#     barcode5 = forms.CharField(required=True, help_text='Required')
#     barcode6 = forms.CharField(required=True, help_text='Required')
#     barcode7 = forms.CharField(required=True, help_text='Required')
#     barcode_check_method = forms.CharField(required=False)
#     barcodecheck_result = forms.BooleanField(required=False)
#
#     def clean_barcode1(self):
#         data = self.cleaned_data['barcode1']
#         return data
#
#     def clean_barcode2(self):
#         data = self.cleaned_data['barcode2']
#         return data
#
#     def clean_barcode3(self):
#         data = self.cleaned_data['barcode3']
#         return data
#
#     def clean_barcode4(self):
#         data = self.cleaned_data['barcode4']
#         return data
#
#     def clean_barcode5(self):
#         data = self.cleaned_data['barcode5']
#         return data
#
#     def clean_barcode6(self):
#         data = self.cleaned_data['barcode6']
#         return data
#
#     def clean_barcode7(self):
#         data = self.cleaned_data['barcode7']
#         return data
#
#     def clean_worksheet(self):
#         data = self.cleaned_data['worksheet']
#         return data
#
#     class Meta:
#         model = BarcodeCheck
#         fields = ('barcodecheckid', 'worksheet', 'barcode1', 'barcode2', 'barcode3', 'barcode4', 'barcode5', 'barcode6',
#                   'barcode7', 'barcode_check_method', 'barcodecheck_result')
#
#
# class BarcodeCheck8Form(forms.ModelForm):
#     worksheet = forms.CharField(required=True, help_text='Required')
#     barcode1 = forms.CharField(required=True, help_text='Required')
#     barcode2 = forms.CharField(required=True, help_text='Required')
#     barcode3 = forms.CharField(required=True, help_text='Required')
#     barcode4 = forms.CharField(required=True, help_text='Required')
#     barcode5 = forms.CharField(required=True, help_text='Required')
#     barcode6 = forms.CharField(required=True, help_text='Required')
#     barcode7 = forms.CharField(required=True, help_text='Required')
#     barcode8 = forms.CharField(required=True, help_text='Required')
#     barcode_check_method = forms.CharField(required=False)
#     barcodecheck_result = forms.BooleanField(required=False)
#
#     def clean_barcode1(self):
#         data = self.cleaned_data['barcode1']
#         return data
#
#     def clean_barcode2(self):
#         data = self.cleaned_data['barcode2']
#         return data
#
#     def clean_barcode3(self):
#         data = self.cleaned_data['barcode3']
#         return data
#
#     def clean_barcode4(self):
#         data = self.cleaned_data['barcode4']
#         return data
#
#     def clean_barcode5(self):
#         data = self.cleaned_data['barcode5']
#         return data
#
#     def clean_barcode6(self):
#         data = self.cleaned_data['barcode6']
#         return data
#
#     def clean_barcode7(self):
#         data = self.cleaned_data['barcode7']
#         return data
#
#     def clean_barcode8(self):
#         data = self.cleaned_data['barcode8']
#         return data
#
#     def clean_worksheet(self):
#         data = self.cleaned_data['worksheet']
#         return data
#
#     class Meta:
#         model = BarcodeCheck
#         fields = ('barcodecheckid', 'worksheet', 'barcode1', 'barcode2', 'barcode3', 'barcode4', 'barcode5', 'barcode6',
#                   'barcode7', 'barcode8', 'barcode_check_method', 'barcodecheck_result')
#
