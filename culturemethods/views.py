from django.shortcuts import render
from culturemethods.forms import CultureCheck3Form

def culturecheck3_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = CultureCheck3Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # Save the form instance to a variable
            culture_check_instance = form.save(commit=False)
            # Assign values to model instance fields
            culture_check_instance.culturecheckbarcode1_input = form.cleaned_data['culturecheckbarcode1'[0:10]]
            culture_check_instance.culturecheckbarcode2_input = form.cleaned_data['culturecheckbarcode2'[0:10]]
            culture_check_instance.culturecheckbarcode3_input = form.cleaned_data['culturecheckbarcode3'[0:10]]

            # Handle matching barcodes here
            if (culture_check_instance.culturecheckbarcode1 == culture_check_instance.culturecheckbarcode2 and
                    culture_check_instance.culturecheckbarcode1 == culture_check_instance.culturecheckbarcode3):
                culture_check_instance.culturecheck_result = form.cleaned_data['culturecheck_result']
                culture_check_instance.culturecheck_method = form.cleaned_data['culturecheck_method']
                culture_check_instance.save()
                return render(request, 'culturemethods/culturecheck3_success.html')
            else:
                # Handle non-matching barcodes here
                culture_check_instance.culturecheck_result = False
                culture_check_instance.culturecheck_method = '3barcodecheck_culture'
                culture_check_instance.save()
            return render(request, 'culturemethods/culturecheck3_fail.html')
        else:
            # Need to include an error message here if form is not valid
            context['3barcodecheck_culture'] = form
            print(form.errors.as_data())
    else:
        form = CultureCheck3Form()
        context['3barcodecheck_culture'] = form
    return render(request, 'culturemethods/culturecheck3.html', context)
