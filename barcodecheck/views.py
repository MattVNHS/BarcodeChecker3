from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from barcodecheck.forms import (BarcodeCheck2Form, BarcodeCheck3Form, BarcodeCheck4Form, BarcodeCheck5Form,
                                BarcodeCheck6Form, BarcodeCheck7Form, BarcodeCheck8Form, BarcodeCheckForm)
from django.contrib import messages
from django.views import View
from django.views.generic.base import TemplateView


class BarcodeCheckView(View):
    def check_authentication(self, request):
        user = request.user
        if not user.is_authenticated:
            return redirect('login')
        context = {}
        form = BarcodeCheckForm()
        context['barcodecheck'] = form
        return render(request, 'barcodecheck/barcodecheck.html', context)

    def post(self, request):
        context = {}
        form = BarcodeCheckForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user

            # getting barcode and worksheet data from POST form
            obj.barcode1 = form.cleaned_data['barcode1']
            obj.barcode2 = form.cleaned_data['barcode2']
            obj.worksheet = form.cleaned_data['worksheet']

            # check if barcodes match
            if obj.barcode1 == obj.barcode2:
                obj.barcodecheck_result = True
                obj.barcode_check_method = 'barcode check_dev'
                obj.save()
                return render(request, 'barcodecheck/barcodecheck_success.html')
            else:
                obj.barcodecheck_result = False
                obj.barcode_check_method = 'barcode check_dev'
                obj.save()
                return render(request, 'barcodecheck/barcodecheck_fail.html')
        else:
            context['barcodecheck'] = form
            return render(request, 'barcodecheck/barcodecheck.html', context)

    def get(self, request):
        context = {}
        form = BarcodeCheckForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user

            # getting barcode and worksheet data from POST form
            obj.barcode1 = form.cleaned_data['barcode1']
            obj.barcode2 = form.cleaned_data['barcode2']
            obj.worksheet = form.cleaned_data['worksheet']

            # check if barcodes match
            if obj.barcode1 == obj.barcode2:
                obj.barcodecheck_result = True
                obj.barcode_check_method = 'barcode check_dev'
                obj.save()
                return render(request, 'barcodecheck/barcodecheck_success.html')
            else:
                obj.barcodecheck_result = False
                obj.barcode_check_method = 'barcode check_dev'
                obj.save()
                return render(request, 'barcodecheck/barcodecheck_fail.html')
        else:
            context['barcodecheck'] = form
            return render(request, 'barcodecheck/barcodecheck.html', context)






def barcodecheck2_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = BarcodeCheck2Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # Save the form instance to a variable
            barcode_check_instance = form.save(commit=False)
            # Assign values to model instance fields
            barcode_check_instance.worksheet = form.cleaned_data['worksheet']
            barcode_check_instance.barcode1 = form.cleaned_data['barcode1']
            barcode_check_instance.barcode2 = form.cleaned_data['barcode2']

            # Handle matching barcodes here
            if barcode_check_instance.barcode1 == barcode_check_instance.barcode2:
                barcode_check_instance.barcodecheck_result = form.cleaned_data['barcodecheck_result']
                barcode_check_instance.barcode_check_method = form.cleaned_data['barcode_check_method']
                barcode_check_instance.save()
                return render(request, 'barcodecheck/barcodecheck2_success.html')
            else:
                # Handle non-matching barcodes here
                barcode_check_instance.barcodecheck_result = False
                barcode_check_instance.barcode_check_method = '2 barcode check'
                barcode_check_instance.save()
            return render(request, 'barcodecheck/barcodecheck2_fail.html')
        else:
            # if form is not valid
            context['barcodecheck2'] = form
            print(form.errors.as_data())
    else:
        form = BarcodeCheck2Form()
        context['barcodecheck2'] = form
    return render(request, 'barcodecheck/barcodecheck2.html', context)


def barcodecheck3_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = BarcodeCheck3Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # Save the form instance to a variable
            barcode_check_instance = form.save(commit=False)
            # Assign values to model instance fields
            barcode_check_instance.worksheet = form.cleaned_data['worksheet']
            barcode_check_instance.barcode1 = form.cleaned_data['barcode1']
            barcode_check_instance.barcode2 = form.cleaned_data['barcode2']
            barcode_check_instance.barcode3 = form.cleaned_data['barcode3']
            # Handle matching barcodes here
            if all(x == barcode_check_instance.barcode1 for x in [barcode_check_instance.barcode2,
                                                                  barcode_check_instance.barcode3]):
                barcode_check_instance.barcodecheck_result = form.cleaned_data['barcodecheck_result']
                barcode_check_instance.barcode_check_method = form.cleaned_data['barcode_check_method']
                barcode_check_instance.save()
                return render(request, 'barcodecheck/barcodecheck3_success.html')
            else:
                # Handle non-matching barcodes here
                barcode_check_instance.barcodecheck_result = False
                barcode_check_instance.barcode_check_method = '3 barcode check'
                barcode_check_instance.save()
            return render(request, 'barcodecheck/barcodecheck3_fail.html')
        else:
            # if form is not valid
            context['barcodecheck3'] = form
            print(form.errors.as_data())
    else:
        form = BarcodeCheck3Form()
        context['barcodecheck3'] = form
    return render(request, 'barcodecheck/barcodecheck3.html', context)


def barcodecheck4_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = BarcodeCheck4Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # Save the form instance to a variable
            barcode_check_instance = form.save(commit=False)
            # Assign values to model instance fields
            barcode_check_instance.worksheet = form.cleaned_data['worksheet']
            barcode_check_instance.barcode1 = form.cleaned_data['barcode1']
            barcode_check_instance.barcode2 = form.cleaned_data['barcode2']
            barcode_check_instance.barcode3 = form.cleaned_data['barcode3']
            barcode_check_instance.barcode4 = form.cleaned_data['barcode4']
            # Handle matching barcodes here
            if all(x == barcode_check_instance.barcode1 for x in [barcode_check_instance.barcode2,
                                                                  barcode_check_instance.barcode3,
                                                                  barcode_check_instance.barcode4]):
                barcode_check_instance.barcodecheck_result = form.cleaned_data['barcodecheck_result']
                barcode_check_instance.barcode_check_method = form.cleaned_data['barcode_check_method']
                barcode_check_instance.save()
                return render(request, 'barcodecheck/barcodecheck4_success.html')
            else:
                # Handle non-matching barcodes here
                barcode_check_instance.barcodecheck_result = False
                barcode_check_instance.barcode_check_method = '4 barcode check'
                barcode_check_instance.save()
            return render(request, 'barcodecheck/barcodecheck4_fail.html')
        else:
            # if form is not valid
            context['barcodecheck4'] = form
            print(form.errors.as_data())
    else:
        form = BarcodeCheck4Form()
        context['barcodecheck4'] = form
    return render(request, 'barcodecheck/barcodecheck4.html', context)


def barcodecheck5_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = BarcodeCheck5Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # Save the form instance to a variable
            barcode_check_instance = form.save(commit=False)
            # Assign values to model instance fields
            barcode_check_instance.worksheet = form.cleaned_data['worksheet']
            barcode_check_instance.barcode1 = form.cleaned_data['barcode1']
            barcode_check_instance.barcode2 = form.cleaned_data['barcode2']
            barcode_check_instance.barcode3 = form.cleaned_data['barcode3']
            barcode_check_instance.barcode4 = form.cleaned_data['barcode4']
            barcode_check_instance.barcode5 = form.cleaned_data['barcode5']
            # Handle matching barcodes here
            if all(x == barcode_check_instance.barcode1 for x in [barcode_check_instance.barcode2,
                                                                  barcode_check_instance.barcode3,
                                                                  barcode_check_instance.barcode4,
                                                                  barcode_check_instance.barcode5]):
                barcode_check_instance.barcodecheck_result = form.cleaned_data['barcodecheck_result']
                barcode_check_instance.barcode_check_method = form.cleaned_data['barcode_check_method']
                barcode_check_instance.save()
                return render(request, 'barcodecheck/barcodecheck5_success.html')
            else:
                # Handle non-matching barcodes here
                barcode_check_instance.barcodecheck_result = False
                barcode_check_instance.barcode_check_method = '5 barcode check'
                barcode_check_instance.save()
            return render(request, 'barcodecheck/barcodecheck5_fail.html')
        else:
            # if form is not valid
            context['barcodecheck5'] = form
            print(form.errors.as_data())
    else:
        form = BarcodeCheck5Form()
        context['barcodecheck5'] = form
    return render(request, 'barcodecheck/barcodecheck5.html', context)


def barcodecheck6_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = BarcodeCheck6Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # Save the form instance to a variable
            barcode_check_instance = form.save(commit=False)
            # Assign values to model instance fields
            barcode_check_instance.worksheet = form.cleaned_data['worksheet']
            barcode_check_instance.barcode1 = form.cleaned_data['barcode1']
            barcode_check_instance.barcode2 = form.cleaned_data['barcode2']
            barcode_check_instance.barcode3 = form.cleaned_data['barcode3']
            barcode_check_instance.barcode4 = form.cleaned_data['barcode4']
            barcode_check_instance.barcode5 = form.cleaned_data['barcode5']
            barcode_check_instance.barcode6 = form.cleaned_data['barcode6']
            # Handle matching barcodes here
            if all(x == barcode_check_instance.barcode1 for x in [barcode_check_instance.barcode2,
                                                                  barcode_check_instance.barcode3,
                                                                  barcode_check_instance.barcode4,
                                                                  barcode_check_instance.barcode5,
                                                                  barcode_check_instance.barcode6]):
                barcode_check_instance.barcodecheck_result = form.cleaned_data['barcodecheck_result']
                barcode_check_instance.barcode_check_method = form.cleaned_data['barcode_check_method']
                barcode_check_instance.save()
                return render(request, 'barcodecheck/barcodecheck6_success.html')
            else:
                # Handle non-matching barcodes here
                barcode_check_instance.barcodecheck_result = False
                barcode_check_instance.barcode_check_method = '6 barcode check'
                barcode_check_instance.save()
            return render(request, 'barcodecheck/barcodecheck6_fail.html')
        else:
            # if form is not valid
            context['barcodecheck6'] = form
            print(form.errors.as_data())
    else:
        form = BarcodeCheck6Form()
        context['barcodecheck6'] = form
    return render(request, 'barcodecheck/barcodecheck6.html', context)


def barcodecheck7_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = BarcodeCheck7Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # Save the form instance to a variable
            barcode_check_instance = form.save(commit=False)
            # Assign values to model instance fields
            barcode_check_instance.worksheet = form.cleaned_data['worksheet']
            barcode_check_instance.barcode1 = form.cleaned_data['barcode1']
            barcode_check_instance.barcode2 = form.cleaned_data['barcode2']
            barcode_check_instance.barcode3 = form.cleaned_data['barcode3']
            barcode_check_instance.barcode4 = form.cleaned_data['barcode4']
            barcode_check_instance.barcode5 = form.cleaned_data['barcode5']
            barcode_check_instance.barcode6 = form.cleaned_data['barcode6']
            barcode_check_instance.barcode7 = form.cleaned_data['barcode7']
            # Handle matching barcodes here
            if all(x == barcode_check_instance.barcode1 for x in [barcode_check_instance.barcode2,
                                                                  barcode_check_instance.barcode3,
                                                                  barcode_check_instance.barcode4,
                                                                  barcode_check_instance.barcode5,
                                                                  barcode_check_instance.barcode6,
                                                                  barcode_check_instance.barcode7]):
                barcode_check_instance.barcodecheck_result = form.cleaned_data['barcodecheck_result']
                barcode_check_instance.barcode_check_method = form.cleaned_data['barcode_check_method']
                barcode_check_instance.save()
                return render(request, 'barcodecheck/barcodecheck7_success.html')
            else:
                # Handle non-matching barcodes here
                barcode_check_instance.barcodecheck_result = False
                barcode_check_instance.barcode_check_method = '7 barcode check'
                barcode_check_instance.save()
            return render(request, 'barcodecheck/barcodecheck7_fail.html')
        else:
            # if form is not valid
            context['barcodecheck7'] = form
            print(form.errors.as_data())
    else:
        form = BarcodeCheck7Form()
        context['barcodecheck7'] = form
    return render(request, 'barcodecheck/barcodecheck7.html', context)


def barcodecheck8_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = BarcodeCheck8Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # Save the form instance to a variable
            barcode_check_instance = form.save(commit=False)
            # Assign values to model instance fields
            barcode_check_instance.worksheet = form.cleaned_data['worksheet']
            barcode_check_instance.barcode1 = form.cleaned_data['barcode1']
            barcode_check_instance.barcode2 = form.cleaned_data['barcode2']
            barcode_check_instance.barcode3 = form.cleaned_data['barcode3']
            barcode_check_instance.barcode4 = form.cleaned_data['barcode4']
            barcode_check_instance.barcode5 = form.cleaned_data['barcode5']
            barcode_check_instance.barcode6 = form.cleaned_data['barcode6']
            barcode_check_instance.barcode7 = form.cleaned_data['barcode7']
            barcode_check_instance.barcode8 = form.cleaned_data['barcode8']
            # Handle matching barcodes here
            if all(x == barcode_check_instance.barcode1 for x in [barcode_check_instance.barcode2,
                                                                  barcode_check_instance.barcode3,
                                                                  barcode_check_instance.barcode4,
                                                                  barcode_check_instance.barcode5,
                                                                  barcode_check_instance.barcode6,
                                                                  barcode_check_instance.barcode7,
                                                                  barcode_check_instance.barcode8]):
                barcode_check_instance.barcodecheck_result = form.cleaned_data['barcodecheck_result']
                barcode_check_instance.barcode_check_method = form.cleaned_data['barcode_check_method']
                barcode_check_instance.save()
                return render(request, 'barcodecheck/barcodecheck8_success.html')
            else:
                # Handle non-matching barcodes here
                barcode_check_instance.barcodecheck_result = False
                barcode_check_instance.barcode_check_method = '8 barcode check'
                barcode_check_instance.save()
            return render(request, 'barcodecheck/barcodecheck8_fail.html')
        else:
            # if form is not valid
            context['barcodecheck8'] = form
            print(form.errors.as_data())
    else:
        form = BarcodeCheck8Form()
        context['barcodecheck8'] = form
    return render(request, 'barcodecheck/barcodecheck8.html', context)
