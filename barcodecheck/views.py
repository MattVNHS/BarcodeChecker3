from django.shortcuts import render, redirect
from datetime import datetime
from .models import BarcodeCheck
from django.http import HttpResponseRedirect
from barcodecheck.forms import BarcodeCheck2Form
from django.contrib import messages


def barcodecheck2_view(request):
    context = {}
    if request.method == "POST":
        check = BarcodeCheck()
        check.worksheet = request.POST['worksheet']
        check.barcode1 = request.POST['barcode1']
        check.barcode2 = request.POST['barcode2']
        check.barcode_check_function = '2 Barcode check'
        if check.barcode1 == check.barcode2:
            check.barcodecheck_result = True
            check.save()
            return render(request, 'barcodecheck/barcodecheck2.html')
        else:
            check.save()
            return render(request, 'barcodecheck/barcodecheck2.html')
    else:
      form = BarcodeCheck2Form()
      context['barcodecheck2'] = form
      return render(request, 'barcodecheck/barcodecheck2.html', context)



    # context = {}
    # if request.method == "POST":
    #     form = BarcodeCheck2Form(request.POST)
    #     if form.is_valid():
    #         BarcodeCheck.barcode1 = form.cleaned_data['barcode1']
    #         BarcodeCheck.barcode2 = form.cleaned_data['barcode2']
    #         BarcodeCheck.save()
    #         if barcode1 == barcode2
    #             barcodecheck_result = "MATCH"
    #             return render(request, 'barcodecheck2')
    #
    #         Using home to test is we get to this point... this can be updated later to redirect to new page or return
    #         same page
    #         return redirect('home')
    #     else:
    #         Need to include an error message here if barcodes do not match (once included above)
    #         context['barcodecheck2'] = form
    # else:
    #     form = BarcodeCheck2Form()
    #     context['barcodecheck2'] = form
    #     return render(request, 'barcodecheck/barcodecheck2.html', context)
