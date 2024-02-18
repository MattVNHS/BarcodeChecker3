from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from extractionmethods.forms import (Qiasymphony24Form)

def Qiasymphony24_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = Qiasymphony24Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # Save the form instance to a variable
            qiasymphony_check_instance = form.save(commit=False)
            # Assign values to model instance fields
            qiasymphony_check_instance.Qiasymphony24Load_worksheet = form.cleaned_data['Qiasymphony24Load_worksheet']
            qiasymphony_check_instance.sampletube1 = form.cleaned_data['sampletube1']
            qiasymphony_check_instance.sampletube2 = form.cleaned_data['sampletube2']
            qiasymphony_check_instance.sampletube3 = form.cleaned_data['sampletube3']
            qiasymphony_check_instance.sampletube4 = form.cleaned_data['sampletube4']
            qiasymphony_check_instance.sampletube5 = form.cleaned_data['sampletube5']
            qiasymphony_check_instance.sampletube6 = form.cleaned_data['sampletube6']
            qiasymphony_check_instance.sampletube7 = form.cleaned_data['sampletube7']
            qiasymphony_check_instance.sampletube8 = form.cleaned_data['sampletube8']
            qiasymphony_check_instance.sampletube9 = form.cleaned_data['sampletube9']
            qiasymphony_check_instance.sampletube10 = form.cleaned_data['sampletube10']
            qiasymphony_check_instance.sampletube11 = form.cleaned_data['sampletube11']
            qiasymphony_check_instance.sampletube12 = form.cleaned_data['sampletube12']
            qiasymphony_check_instance.sampletube13 = form.cleaned_data['sampletube13']
            qiasymphony_check_instance.sampletube14 = form.cleaned_data['sampletube14']
            qiasymphony_check_instance.sampletube15 = form.cleaned_data['sampletube15']
            qiasymphony_check_instance.sampletube16 = form.cleaned_data['sampletube16']
            qiasymphony_check_instance.sampletube17 = form.cleaned_data['sampletube17']
            qiasymphony_check_instance.sampletube18 = form.cleaned_data['sampletube18']
            qiasymphony_check_instance.sampletube19 = form.cleaned_data['sampletube19']
            qiasymphony_check_instance.sampletube20 = form.cleaned_data['sampletube20']
            qiasymphony_check_instance.sampletube21 = form.cleaned_data['sampletube21']
            qiasymphony_check_instance.sampletube22 = form.cleaned_data['sampletube22']
            qiasymphony_check_instance.sampletube23 = form.cleaned_data['sampletube23']
            qiasymphony_check_instance.sampletube24 = form.cleaned_data['sampletube24']
            qiasymphony_check_instance.elutiontube1 = form.cleaned_data['elutiontube1']
            qiasymphony_check_instance.elutiontube2 = form.cleaned_data['elutiontube2']
            qiasymphony_check_instance.elutiontube3 = form.cleaned_data['elutiontube3']
            qiasymphony_check_instance.elutiontube4 = form.cleaned_data['elutiontube4']
            qiasymphony_check_instance.elutiontube5 = form.cleaned_data['elutiontube5']
            qiasymphony_check_instance.elutiontube6 = form.cleaned_data['elutiontube6']
            qiasymphony_check_instance.elutiontube7 = form.cleaned_data['elutiontube7']
            qiasymphony_check_instance.elutiontube8 = form.cleaned_data['elutiontube8']
            qiasymphony_check_instance.elutiontube9 = form.cleaned_data['elutiontube9']
            qiasymphony_check_instance.elutiontube10 = form.cleaned_data['elutiontube10']
            qiasymphony_check_instance.elutiontube11 = form.cleaned_data['elutiontube11']
            qiasymphony_check_instance.elutiontube12 = form.cleaned_data['elutiontube12']
            qiasymphony_check_instance.elutiontube13 = form.cleaned_data['elutiontube13']
            qiasymphony_check_instance.elutiontube14 = form.cleaned_data['elutiontube14']
            qiasymphony_check_instance.elutiontube15 = form.cleaned_data['elutiontube15']
            qiasymphony_check_instance.elutiontube16 = form.cleaned_data['elutiontube16']
            qiasymphony_check_instance.elutiontube17 = form.cleaned_data['elutiontube17']
            qiasymphony_check_instance.elutiontube18 = form.cleaned_data['elutiontube18']
            qiasymphony_check_instance.elutiontube19 = form.cleaned_data['elutiontube19']
            qiasymphony_check_instance.elutiontube20 = form.cleaned_data['elutiontube20']
            qiasymphony_check_instance.elutiontube21 = form.cleaned_data['elutiontube21']
            qiasymphony_check_instance.elutiontube22 = form.cleaned_data['elutiontube22']
            qiasymphony_check_instance.elutiontube23 = form.cleaned_data['elutiontube23']
            qiasymphony_check_instance.elutiontube24 = form.cleaned_data['elutiontube24']
            if (qiasymphony_check_instance.sampletube1 == qiasymphony_check_instance.elutiontube1 and
                qiasymphony_check_instance.sampletube2 == qiasymphony_check_instance.elutiontube2 and
                qiasymphony_check_instance.sampletube3 == qiasymphony_check_instance.elutiontube3 and
                qiasymphony_check_instance.sampletube4 == qiasymphony_check_instance.elutiontube4 and
                qiasymphony_check_instance.sampletube5 == qiasymphony_check_instance.elutiontube5 and
                qiasymphony_check_instance.sampletube6 == qiasymphony_check_instance.elutiontube6 and
                qiasymphony_check_instance.sampletube7 == qiasymphony_check_instance.elutiontube7 and
                qiasymphony_check_instance.sampletube8 == qiasymphony_check_instance.elutiontube8 and
                qiasymphony_check_instance.sampletube9 == qiasymphony_check_instance.elutiontube9 and
                qiasymphony_check_instance.sampletube10 == qiasymphony_check_instance.elutiontube10 and
                qiasymphony_check_instance.sampletube11 == qiasymphony_check_instance.elutiontube11 and
                qiasymphony_check_instance.sampletube12 == qiasymphony_check_instance.elutiontube12 and
                qiasymphony_check_instance.sampletube13 == qiasymphony_check_instance.elutiontube13 and
                qiasymphony_check_instance.sampletube14 == qiasymphony_check_instance.elutiontube14 and
                qiasymphony_check_instance.sampletube15 == qiasymphony_check_instance.elutiontube15 and
                qiasymphony_check_instance.sampletube16 == qiasymphony_check_instance.elutiontube16 and
                qiasymphony_check_instance.sampletube17 == qiasymphony_check_instance.elutiontube17 and
                qiasymphony_check_instance.sampletube18 == qiasymphony_check_instance.elutiontube18 and
                qiasymphony_check_instance.sampletube19 == qiasymphony_check_instance.elutiontube19 and
                qiasymphony_check_instance.sampletube20 == qiasymphony_check_instance.elutiontube20 and
                qiasymphony_check_instance.sampletube21 == qiasymphony_check_instance.elutiontube21 and
                qiasymphony_check_instance.sampletube22 == qiasymphony_check_instance.elutiontube22 and
                qiasymphony_check_instance.sampletube23 == qiasymphony_check_instance.elutiontube23 and
                qiasymphony_check_instance.sampletube24 == qiasymphony_check_instance.elutiontube24):
                qiasymphony_check_instance.Qiasymphony24Check_result = form.cleaned_data['Qiasymphony24Check_result']
                qiasymphony_check_instance.Qiasymphony24Load_method = form.cleaned_data['Qiasymphony24Load_method']
                qiasymphony_check_instance.save()
                return render(request, 'extractionmethods/Qiasymphony24Check_success.html')
            else:
                # Handle non-matching barcodes here
                qiasymphony_check_instance.Qiasymphony24Check_result = False
                qiasymphony_check_instance.Qiasymphony24Load_method = 'Qiasymphony24Check'
                qiasymphony_check_instance.save()
            return render(request, 'extractionmethods/Qiasymphony24Check_fail.html')
        else:
            # if form is not valid
            context['Qiasymphony24'] = form
            print(form.errors.as_data())
    else:
        form = Qiasymphony24Form()
        context['Qiasymphony24'] = form
    return render(request, 'extractionmethods/Qiasymphony24Check.html', context)





