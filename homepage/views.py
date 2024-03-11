from django.shortcuts import render, redirect
from homepage.forms import *
def home_screen_view(request):

    # initialise each form and pass to the context
    barcode_form = BarcodeForm()
    qiasymphony_form = QiasymphonyForm()
    context = {'qiasymphony_form': qiasymphony_form, 'barcode_form': barcode_form}

    # Each check has a form in homepage/forms.py with a hidden url_name field
    if request.method == 'POST':
        return redirect(request.POST['url_name'], barcode_count=request.POST['barcode_count'])

    return render(request, 'homepage/home.html', context)
