from django.shortcuts import render, redirect
from datetime import datetime
from .models import BarcodeCheck
from barcodecheck.forms import BarcodeCheck2Form


def barcodecheck2_view(request):
    context = {}
    if request.POST:
        form = BarcodeCheck2Form(request.POST)
        if form.is_valid():
            barcodecheck.barcode1 = form.cleaned_data['barcode1']
            barcodecheck.barcode1 = form.cleaned_data['barcode2']
            barcodecheck.save()
            # if barcodecheck2_value1 == barcodecheck2_value2
            #     barcodecheck_result = "MATCH"
            #     return render(request, 'barcodecheck2')
            return redirect('home')
        else:
            context['barcodecheck2'] = form
    else:
        form = BarcodeCheck2Form()
        context['barcodecheck2_form'] = form
    return render(request, 'barcodecheck/barcodecheck2.html', context)
