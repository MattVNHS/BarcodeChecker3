from django.shortcuts import render, redirect
from datetime import datetime
from .models import BarcodeCheck
from django.http import HttpResponseRedirect
from barcodecheck.forms import BarcodeCheck2Form


def barcodecheck2_view(request):
    context = {}
    if request.method == "POST":
        form = BarcodeCheck2Form(request.POST)
        if form.is_valid():
            BarcodeCheck.barcode1 = form.cleaned_data['barcode1']
            BarcodeCheck.barcode2 = form.cleaned_data['barcode2']
            BarcodeCheck.save()
            # if barcode1 == barcode2
            #     barcodecheck_result = "MATCH"
            #     return render(request, 'barcodecheck2')

            # Using home to test is we get to this point... this can be updated later to redirect to new page or return
            # same page
            return redirect('home')
        else:
            context['barcodecheck2'] = form
    else:
        form = BarcodeCheck2Form()
        context['barcodecheck2_form'] = form
    return render(request, 'barcodecheck/barcodecheck2.html', context)
