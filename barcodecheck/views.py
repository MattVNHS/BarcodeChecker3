from django.shortcuts import render, redirect
from datetime import datetime
from .models import BarcodeCheck
from django.http import HttpResponseRedirect
from barcodecheck.forms import BarcodeCheck2Form
from django.contrib import messages
from account.models import Account

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

            # Save the instance to the database
            barcode_check_instance.save()

            # Handle barcodecheck_result and barcode_check_function based on your requirements
            if barcode_check_instance.barcode1 == barcode_check_instance.barcode2:
                barcode_check_instance.barcodecheck_result = form.cleaned_data['barcodecheck_result']
                barcode_check_instance.barcode_check_function = form.cleaned_data['barcode_check_function']
            else:
                # Handle non-matching barcodes here
                barcode_check_instance.barcodecheck_result = False
                barcode_check_instance.barcode_check_function = '2 barcode check'
                barcode_check_instance.save()
            return render(request, 'barcodecheck/barcodecheck2.html')
        else:
            # Need to include an error message here if form is not valid
            context['barcodecheck2'] = form
            print(form.errors.as_data())
    else:
        form = BarcodeCheck2Form()
        context['barcodecheck2'] = form

    return render(request, 'barcodecheck/barcodecheck2.html', context)

# context = {}
# if request.method == "POST":
#     check = BarcodeCheck()
#     check.worksheet = request.POST['worksheet']
#     check.barcode1 = request.POST['barcode1']
#     check.barcode2 = request.POST['barcode2']
#     check.barcode_check_function = '2 Barcode check'
#     if check.barcode1 == check.barcode2:
#         check.barcodecheck_result = True
#         check.save()
#         return render(request, 'barcodecheck/barcodecheck2.html')
#     else:
#         check.save()
#         return render(request, 'barcodecheck/barcodecheck2.html')
# else:
#     form = BarcodeCheck2Form()
#     context['barcodecheck2'] = form
#     return render(request, 'barcodecheck/barcodecheck2.html', context)
