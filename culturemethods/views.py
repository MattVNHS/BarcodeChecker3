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

            # getting the first 10 characters from inputted values
            obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1'][0:10]
            obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2'][0:10]
            obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3'][0:10]

            # checking if the first 10 characters match
            if (obj.culturecheckbarcode1 == obj.culturecheckbarcode2 and
                    obj.culturecheckbarcode1 == obj.culturecheckbarcode3):

            # If match then saving original inputted values from user as want to save these to database
                obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1']
                obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2']
                obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3']
                obj.culturecheck_result = form.cleaned_data['culturecheck_result']
                obj.culturecheck_method = form.cleaned_data['culturecheck_method']
                obj.save()
                return render(request, 'culturemethods/culturecheck3_success.html')
            else:
                obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1']
                obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2']
                obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3']
                obj.culturecheck_result = False
                obj.culturecheck_method = '3barcodecheck_culture'
                obj.save()
            return render(request, 'culturemethods/culturecheck3_fail.html')
        else:
            # Need to include an error message here if form is not valid
            context['3barcodecheck_culture'] = form
            print(form.errors.as_data())
    else:
        form = CultureCheck3Form()
        context['3barcodecheck_culture'] = form
    return render(request, 'culturemethods/culturecheck3.html', context)
