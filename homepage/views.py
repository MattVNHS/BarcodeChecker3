from django.shortcuts import render, redirect
from homepage.forms import *
def home_screen_view(request):
    barcode_form = BarcodeForm()
    qiasymphony_form = QiasymphonyForm()
    context = {'qiasymphony_form': qiasymphony_form, 'barcode_form': barcode_form}
    if request.method == 'POST':
        print(request)
        return redirect("Qiasymphony", barcode_count=request.POST['barcode_count'] )
    return render(request, 'homepage/home.html', context)
