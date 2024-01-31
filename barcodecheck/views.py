from django.shortcuts import render, redirect
from datetime import datetime


def barcodecheck2_view(request):
    barcode1 = 'barcodecheck2_value1'
    barcode2 = 'barcodecheck2_value2'
    if barcode1 == barcode2:
        barcodecheck2_comparison_match = "MATCH"
        return render(request, 'barcodecheck/barcodecheck2.html',)
    else:
        barcodecheck2_comparison_match = "MISMATCH"
        return render(request, 'barcodecheck/barcodecheck2.html',)


