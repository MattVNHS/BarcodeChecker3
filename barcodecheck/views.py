from django.shortcuts import render, redirect
from datetime import datetime
from .models import BarcodeCheck
from django.http import HttpResponseRedirect
from barcodecheck.forms import BarcodeCheck2Form
from django.contrib import messages




def barcodecheck2_view(request):
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



    context = {}
    if request.method == "POST":
        form = BarcodeCheck2Form(request.POST)
        if form.is_valid():
            BarcodeCheck.worksheet = form.cleaned_data['worksheet']
            BarcodeCheck.barcode1 = form.cleaned_data['barcode1']
            BarcodeCheck.barcode2 = form.cleaned_data['barcode2']
            if BarcodeCheck.barcode1 == BarcodeCheck.barcode2:
                BarcodeCheck.barcodecheck_result = True
                BarcodeCheck.barcode_check_function = '2 Barcode check'
                return render(request, 'barcodecheck/barcodecheck2.html')
            return render(request, 'barcodecheck/barcodecheck2.html')
        else:
            # Need to include an error message here if barcodes do not match (once included above)
            context['barcodecheck2'] = form
            print(form.errors.as_data())
    else:
        form = BarcodeCheck2Form()
        context['barcodecheck2'] = form
    return render(request, 'barcodecheck/barcodecheck2.html', context)
