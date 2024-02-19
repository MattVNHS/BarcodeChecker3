from django.shortcuts import render
from culturemethods.forms import (CultureCheck2Form, CultureCheck3Form, CultureCheck4Form, CultureCheck5Form,
                                  CultureCheck6Form, CultureCheck7Form, CultureCheck8Form)


def culturecheck2_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        form = CultureCheck2Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user

            # getting the first 10 characters from inputted values
            obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1'][0:10]
            obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2'][0:10]

            # checking if the first 10 characters match
            if obj.culturecheckbarcode1 == obj.culturecheckbarcode2:

            # If match then saving original inputted values from user as want to save these to database
                obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1']
                obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2']
                obj.culturecheck_result = form.cleaned_data['culturecheck_result']
                obj.culturecheck_method = form.cleaned_data['culturecheck_method']
                obj.save()
                return render(request, 'culturemethods/culturecheck2_success.html')
            else:
                obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1']
                obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2']
                obj.culturecheck_result = False
                obj.culturecheck_method = '2barcodecheck_culture'
                obj.save()
            return render(request, 'culturemethods/culturecheck2_fail.html')
        else:
            # if form is not valid
            context['2barcodecheck_culture'] = form
            print(form.errors.as_data())
    else:
        form = CultureCheck2Form()
        context['2barcodecheck_culture'] = form
    return render(request, 'culturemethods/culturecheck2.html', context)


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
            # if form is not valid
            context['3barcodecheck_culture'] = form
            print(form.errors.as_data())
    else:
        form = CultureCheck3Form()
        context['3barcodecheck_culture'] = form
    return render(request, 'culturemethods/culturecheck3.html', context)


def culturecheck4_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        form = CultureCheck4Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user

            # getting the first 10 characters from inputted values
            obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1'][0:10]
            obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2'][0:10]
            obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3'][0:10]
            obj.culturecheckbarcode4 = form.cleaned_data['culturecheckbarcode4'][0:10]

            # checking if the first 10 characters match
            if all(x == obj.culturecheckbarcode1 for x in [obj.culturecheckbarcode2,
                                                            obj.culturecheckbarcode3,
                                                            obj.culturecheckbarcode4]):

            # If match then saving original inputted values from user as want to save these to database
                obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1']
                obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2']
                obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3']
                obj.culturecheckbarcode4 = form.cleaned_data['culturecheckbarcode4']
                obj.culturecheck_result = form.cleaned_data['culturecheck_result']
                obj.culturecheck_method = form.cleaned_data['culturecheck_method']
                obj.save()
                return render(request, 'culturemethods/culturecheck4_success.html')
            else:
                obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1']
                obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2']
                obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3']
                obj.culturecheckbarcode4 = form.cleaned_data['culturecheckbarcode4']
                obj.culturecheck_result = False
                obj.culturecheck_method = '4barcodecheck_culture'
                obj.save()
            return render(request, 'culturemethods/culturecheck4_fail.html')
        else:
            # if form is not valid
            context['4barcodecheck_culture'] = form
            print(form.errors.as_data())
    else:
        form = CultureCheck4Form()
        context['4barcodecheck_culture'] = form
    return render(request, 'culturemethods/culturecheck4.html', context)


def culturecheck5_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        form = CultureCheck5Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user

            # getting the first 10 characters from inputted values
            obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1'][0:10]
            obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2'][0:10]
            obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3'][0:10]
            obj.culturecheckbarcode4 = form.cleaned_data['culturecheckbarcode4'][0:10]
            obj.culturecheckbarcode5 = form.cleaned_data['culturecheckbarcode5'][0:10]

            # checking if the first 10 characters match
            if all(x == obj.culturecheckbarcode1 for x in [obj.culturecheckbarcode2,
                                                            obj.culturecheckbarcode3,
                                                            obj.culturecheckbarcode4,
                                                            obj.culturecheckbarcode5]):

            # If match then saving original inputted values from user as want to save these to database
                obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1']
                obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2']
                obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3']
                obj.culturecheckbarcode4 = form.cleaned_data['culturecheckbarcode4']
                obj.culturecheckbarcode5 = form.cleaned_data['culturecheckbarcode5']
                obj.culturecheck_result = form.cleaned_data['culturecheck_result']
                obj.culturecheck_method = form.cleaned_data['culturecheck_method']
                obj.save()
                return render(request, 'culturemethods/culturecheck5_success.html')
            else:
                obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1']
                obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2']
                obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3']
                obj.culturecheckbarcode4 = form.cleaned_data['culturecheckbarcode4']
                obj.culturecheckbarcode5 = form.cleaned_data['culturecheckbarcode5']
                obj.culturecheck_result = False
                obj.culturecheck_method = '5barcodecheck_culture'
                obj.save()
            return render(request, 'culturemethods/culturecheck5_fail.html')
        else:
            # if form is not valid
            context['5barcodecheck_culture'] = form
            print(form.errors.as_data())
    else:
        form = CultureCheck5Form()
        context['5barcodecheck_culture'] = form
    return render(request, 'culturemethods/culturecheck5.html', context)


def culturecheck6_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        form = CultureCheck6Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user

            # getting the first 10 characters from inputted values
            obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1'][0:10]
            obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2'][0:10]
            obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3'][0:10]
            obj.culturecheckbarcode4 = form.cleaned_data['culturecheckbarcode4'][0:10]
            obj.culturecheckbarcode5 = form.cleaned_data['culturecheckbarcode5'][0:10]
            obj.culturecheckbarcode6 = form.cleaned_data['culturecheckbarcode6'][0:10]

            # checking if the first 10 characters match
            if all(x == obj.culturecheckbarcode1 for x in [obj.culturecheckbarcode2,
                                                            obj.culturecheckbarcode3,
                                                            obj.culturecheckbarcode4,
                                                            obj.culturecheckbarcode5,
                                                            obj.culturecheckbarcode6]):

            # If match then saving original inputted values from user as want to save these to database
                obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1']
                obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2']
                obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3']
                obj.culturecheckbarcode4 = form.cleaned_data['culturecheckbarcode4']
                obj.culturecheckbarcode5 = form.cleaned_data['culturecheckbarcode5']
                obj.culturecheckbarcode6 = form.cleaned_data['culturecheckbarcode6']
                obj.culturecheck_result = form.cleaned_data['culturecheck_result']
                obj.culturecheck_method = form.cleaned_data['culturecheck_method']
                obj.save()
                return render(request, 'culturemethods/culturecheck6_success.html')
            else:
                obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1']
                obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2']
                obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3']
                obj.culturecheckbarcode4 = form.cleaned_data['culturecheckbarcode4']
                obj.culturecheckbarcode5 = form.cleaned_data['culturecheckbarcode5']
                obj.culturecheckbarcode6 = form.cleaned_data['culturecheckbarcode6']
                obj.culturecheck_result = False
                obj.culturecheck_method = '6barcodecheck_culture'
                obj.save()
            return render(request, 'culturemethods/culturecheck6_fail.html')
        else:
            # if form is not valid
            context['6barcodecheck_culture'] = form
            print(form.errors.as_data())
    else:
        form = CultureCheck6Form()
        context['6barcodecheck_culture'] = form
    return render(request, 'culturemethods/culturecheck6.html', context)


def culturecheck7_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        form = CultureCheck7Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user

            # getting the first 10 characters from inputted values
            obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1'][0:10]
            obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2'][0:10]
            obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3'][0:10]
            obj.culturecheckbarcode4 = form.cleaned_data['culturecheckbarcode4'][0:10]
            obj.culturecheckbarcode5 = form.cleaned_data['culturecheckbarcode5'][0:10]
            obj.culturecheckbarcode6 = form.cleaned_data['culturecheckbarcode6'][0:10]
            obj.culturecheckbarcode7 = form.cleaned_data['culturecheckbarcode7'][0:10]

            # checking if the first 10 characters match
            if all(x == obj.culturecheckbarcode1 for x in [obj.culturecheckbarcode2,
                                                            obj.culturecheckbarcode3,
                                                            obj.culturecheckbarcode4,
                                                            obj.culturecheckbarcode5,
                                                            obj.culturecheckbarcode6,
                                                            obj.culturecheckbarcode7]):

            # If match then saving original inputted values from user as want to save these to database
                obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1']
                obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2']
                obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3']
                obj.culturecheckbarcode4 = form.cleaned_data['culturecheckbarcode4']
                obj.culturecheckbarcode5 = form.cleaned_data['culturecheckbarcode5']
                obj.culturecheckbarcode6 = form.cleaned_data['culturecheckbarcode6']
                obj.culturecheckbarcode7 = form.cleaned_data['culturecheckbarcode7']
                obj.culturecheck_result = form.cleaned_data['culturecheck_result']
                obj.culturecheck_method = form.cleaned_data['culturecheck_method']
                obj.save()
                return render(request, 'culturemethods/culturecheck7_success.html')
            else:
                obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1']
                obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2']
                obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3']
                obj.culturecheckbarcode4 = form.cleaned_data['culturecheckbarcode4']
                obj.culturecheckbarcode5 = form.cleaned_data['culturecheckbarcode5']
                obj.culturecheckbarcode6 = form.cleaned_data['culturecheckbarcode6']
                obj.culturecheckbarcode7 = form.cleaned_data['culturecheckbarcode7']
                obj.culturecheck_result = False
                obj.culturecheck_method = '7barcodecheck_culture'
                obj.save()
            return render(request, 'culturemethods/culturecheck7_fail.html')
        else:
            # if form is not valid
            context['7barcodecheck_culture'] = form
            print(form.errors.as_data())
    else:
        form = CultureCheck7Form()
        context['7barcodecheck_culture'] = form
    return render(request, 'culturemethods/culturecheck7.html', context)


def culturecheck8_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        form = CultureCheck8Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user

            # getting the first 10 characters from inputted values
            obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1'][0:10]
            obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2'][0:10]
            obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3'][0:10]
            obj.culturecheckbarcode4 = form.cleaned_data['culturecheckbarcode4'][0:10]
            obj.culturecheckbarcode5 = form.cleaned_data['culturecheckbarcode5'][0:10]
            obj.culturecheckbarcode6 = form.cleaned_data['culturecheckbarcode6'][0:10]
            obj.culturecheckbarcode8 = form.cleaned_data['culturecheckbarcode8'][0:10]

            # checking if the first 10 characters match
            if all(x == obj.culturecheckbarcode1 for x in [obj.culturecheckbarcode2,
                                                            obj.culturecheckbarcode3,
                                                            obj.culturecheckbarcode4,
                                                            obj.culturecheckbarcode5,
                                                            obj.culturecheckbarcode6,
                                                            obj.culturecheckbarcode7,
                                                            obj.culturecheckbarcode8]):

            # If match then saving original inputted values from user as want to save these to database
                obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1']
                obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2']
                obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3']
                obj.culturecheckbarcode4 = form.cleaned_data['culturecheckbarcode4']
                obj.culturecheckbarcode5 = form.cleaned_data['culturecheckbarcode5']
                obj.culturecheckbarcode6 = form.cleaned_data['culturecheckbarcode6']
                obj.culturecheckbarcode7 = form.cleaned_data['culturecheckbarcode7']
                obj.culturecheckbarcode8 = form.cleaned_data['culturecheckbarcode8']
                obj.culturecheck_result = form.cleaned_data['culturecheck_result']
                obj.culturecheck_method = form.cleaned_data['culturecheck_method']
                obj.save()
                return render(request, 'culturemethods/culturecheck8_success.html')
            else:
                obj.culturecheckbarcode1 = form.cleaned_data['culturecheckbarcode1']
                obj.culturecheckbarcode2 = form.cleaned_data['culturecheckbarcode2']
                obj.culturecheckbarcode3 = form.cleaned_data['culturecheckbarcode3']
                obj.culturecheckbarcode4 = form.cleaned_data['culturecheckbarcode4']
                obj.culturecheckbarcode5 = form.cleaned_data['culturecheckbarcode5']
                obj.culturecheckbarcode6 = form.cleaned_data['culturecheckbarcode6']
                obj.culturecheckbarcode7 = form.cleaned_data['culturecheckbarcode7']
                obj.culturecheckbarcode8 = form.cleaned_data['culturecheckbarcode8']
                obj.culturecheck_result = False
                obj.culturecheck_method = '8barcodecheck_culture'
                obj.save()
            return render(request, 'culturemethods/culturecheck8_fail.html')
        else:
            # if form is not valid
            context['8barcodecheck_culture'] = form
            print(form.errors.as_data())
    else:
        form = CultureCheck8Form()
        context['8barcodecheck_culture'] = form
    return render(request, 'culturemethods/culturecheck8.html', context)
