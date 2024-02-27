from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from barcodecheck.forms import *
from django.contrib import messages

from django.views.generic.edit import FormView

from django.forms import formset_factory



class BarcodecheckFormView(FormView):
    template_name = 'barcodecheck/barcodecheck.html'
    model = Barcodes

    success_url = '/'


    ''' BarcodecheckFormView defines the FormView class, to create the appropriate number of barcode check forms I
    edited the get_form_class() method. I used formset_factory to create a formset from the BarcodeCheckForm and passed 
    the extra parameter to create the required number for BarcodeCheckForm forms. self.kwargs['checks'] is passed in 
    the url. This way the required number of barcodes to be checked can be passed in the url. 
    https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_class
    Accessed kwargs following this: https://stackoverflow.com/questions/34462739/use-url-parameter-in-class-based-view-django'''

    def get_form_class(self, **kwargs):
        form_class = formset_factory(BarcodeCheckForm, extra=self.kwargs['checks'])
        return form_class

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(form)
       # if all(x == barcode_check_instance.barcode1 for x in [barcode_check_instance.barcode2,
        #                                                                   barcode_check_instance.barcode3]):
        return super().form_valid(form)



#
#
# def barcodecheck2_view(request):
#     context = {}
#     user = request.user
#     if not user.is_authenticated:
#         return redirect('login')
#     if request.method == "POST":
#         form = BarcodeCheck2Form(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = request.user
#             obj.save()
#             # Save the form instance to a variable
#             barcode_check_instance = form.save(commit=False)
#             # Assign values to model instance fields
#             barcode_check_instance.worksheet = form.cleaned_data['worksheet']
#             barcode_check_instance.barcode1 = form.cleaned_data['barcode1']
#             barcode_check_instance.barcode2 = form.cleaned_data['barcode2']
#
#             # Handle matching barcodes here
#             if barcode_check_instance.barcode1 == barcode_check_instance.barcode2:
#                 barcode_check_instance.barcodecheck_result = form.cleaned_data['barcodecheck_result']
#                 barcode_check_instance.barcode_check_method = form.cleaned_data['barcode_check_method']
#                 barcode_check_instance.save()
#                 return render(request, 'barcodecheck/barcodecheck2_success.html')
#             else:
#                 # Handle non-matching barcodes here
#                 barcode_check_instance.barcodecheck_result = False
#                 barcode_check_instance.barcode_check_method = '2 barcode check'
#                 barcode_check_instance.save()
#             return render(request, 'barcodecheck/barcodecheck2_fail.html')
#         else:
#             # if form is not valid
#             context['barcodecheck2'] = form
#             print(form.errors.as_data())
#     else:
#         form = BarcodeCheck2Form()
#         context['barcodecheck2'] = form
#     return render(request, 'barcodecheck/barcodecheck2.html', context)
#
#
# def barcodecheck3_view(request):
#     context = {}
#     user = request.user
#     if not user.is_authenticated:
#         return redirect('login')
#     if request.method == "POST":
#         form = BarcodeCheck3Form(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = request.user
#             obj.save()
#             # Save the form instance to a variable
#             barcode_check_instance = form.save(commit=False)
#             # Assign values to model instance fields
#             barcode_check_instance.worksheet = form.cleaned_data['worksheet']
#             barcode_check_instance.barcode1 = form.cleaned_data['barcode1']
#             barcode_check_instance.barcode2 = form.cleaned_data['barcode2']
#             barcode_check_instance.barcode3 = form.cleaned_data['barcode3']
#             # Handle matching barcodes here
#             if all(x == barcode_check_instance.barcode1 for x in [barcode_check_instance.barcode2,
#                                                                   barcode_check_instance.barcode3]):
#                 barcode_check_instance.barcodecheck_result = form.cleaned_data['barcodecheck_result']
#                 barcode_check_instance.barcode_check_method = form.cleaned_data['barcode_check_method']
#                 barcode_check_instance.save()
#                 return render(request, 'barcodecheck/barcodecheck3_success.html')
#             else:
#                 # Handle non-matching barcodes here
#                 barcode_check_instance.barcodecheck_result = False
#                 barcode_check_instance.barcode_check_method = '3 barcode check'
#                 barcode_check_instance.save()
#             return render(request, 'barcodecheck/barcodecheck3_fail.html')
#         else:
#             # if form is not valid
#             context['barcodecheck3'] = form
#             print(form.errors.as_data())
#     else:
#         form = BarcodeCheck3Form()
#         context['barcodecheck3'] = form
#     return render(request, 'barcodecheck/barcodecheck3.html', context)
#
#
# def barcodecheck4_view(request):
#     context = {}
#     user = request.user
#     if not user.is_authenticated:
#         return redirect('login')
#     if request.method == "POST":
#         form = BarcodeCheck4Form(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = request.user
#             obj.save()
#             # Save the form instance to a variable
#             barcode_check_instance = form.save(commit=False)
#             # Assign values to model instance fields
#             barcode_check_instance.worksheet = form.cleaned_data['worksheet']
#             barcode_check_instance.barcode1 = form.cleaned_data['barcode1']
#             barcode_check_instance.barcode2 = form.cleaned_data['barcode2']
#             barcode_check_instance.barcode3 = form.cleaned_data['barcode3']
#             barcode_check_instance.barcode4 = form.cleaned_data['barcode4']
#             # Handle matching barcodes here
#             if all(x == barcode_check_instance.barcode1 for x in [barcode_check_instance.barcode2,
#                                                                   barcode_check_instance.barcode3,
#                                                                   barcode_check_instance.barcode4]):
#                 barcode_check_instance.barcodecheck_result = form.cleaned_data['barcodecheck_result']
#                 barcode_check_instance.barcode_check_method = form.cleaned_data['barcode_check_method']
#                 barcode_check_instance.save()
#                 return render(request, 'barcodecheck/barcodecheck4_success.html')
#             else:
#                 # Handle non-matching barcodes here
#                 barcode_check_instance.barcodecheck_result = False
#                 barcode_check_instance.barcode_check_method = '4 barcode check'
#                 barcode_check_instance.save()
#             return render(request, 'barcodecheck/barcodecheck4_fail.html')
#         else:
#             # if form is not valid
#             context['barcodecheck4'] = form
#             print(form.errors.as_data())
#     else:
#         form = BarcodeCheck4Form()
#         context['barcodecheck4'] = form
#     return render(request, 'barcodecheck/barcodecheck4.html', context)
#
#
# def barcodecheck5_view(request):
#     context = {}
#     user = request.user
#     if not user.is_authenticated:
#         return redirect('login')
#     if request.method == "POST":
#         form = BarcodeCheck5Form(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = request.user
#             obj.save()
#             # Save the form instance to a variable
#             barcode_check_instance = form.save(commit=False)
#             # Assign values to model instance fields
#             barcode_check_instance.worksheet = form.cleaned_data['worksheet']
#             barcode_check_instance.barcode1 = form.cleaned_data['barcode1']
#             barcode_check_instance.barcode2 = form.cleaned_data['barcode2']
#             barcode_check_instance.barcode3 = form.cleaned_data['barcode3']
#             barcode_check_instance.barcode4 = form.cleaned_data['barcode4']
#             barcode_check_instance.barcode5 = form.cleaned_data['barcode5']
#             # Handle matching barcodes here
#             if all(x == barcode_check_instance.barcode1 for x in [barcode_check_instance.barcode2,
#                                                                   barcode_check_instance.barcode3,
#                                                                   barcode_check_instance.barcode4,
#                                                                   barcode_check_instance.barcode5]):
#                 barcode_check_instance.barcodecheck_result = form.cleaned_data['barcodecheck_result']
#                 barcode_check_instance.barcode_check_method = form.cleaned_data['barcode_check_method']
#                 barcode_check_instance.save()
#                 return render(request, 'barcodecheck/barcodecheck5_success.html')
#             else:
#                 # Handle non-matching barcodes here
#                 barcode_check_instance.barcodecheck_result = False
#                 barcode_check_instance.barcode_check_method = '5 barcode check'
#                 barcode_check_instance.save()
#             return render(request, 'barcodecheck/barcodecheck5_fail.html')
#         else:
#             # if form is not valid
#             context['barcodecheck5'] = form
#             print(form.errors.as_data())
#     else:
#         form = BarcodeCheck5Form()
#         context['barcodecheck5'] = form
#     return render(request, 'barcodecheck/barcodecheck5.html', context)
#
#
# def barcodecheck6_view(request):
#     context = {}
#     user = request.user
#     if not user.is_authenticated:
#         return redirect('login')
#     if request.method == "POST":
#         form = BarcodeCheck6Form(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = request.user
#             obj.save()
#             # Save the form instance to a variable
#             barcode_check_instance = form.save(commit=False)
#             # Assign values to model instance fields
#             barcode_check_instance.worksheet = form.cleaned_data['worksheet']
#             barcode_check_instance.barcode1 = form.cleaned_data['barcode1']
#             barcode_check_instance.barcode2 = form.cleaned_data['barcode2']
#             barcode_check_instance.barcode3 = form.cleaned_data['barcode3']
#             barcode_check_instance.barcode4 = form.cleaned_data['barcode4']
#             barcode_check_instance.barcode5 = form.cleaned_data['barcode5']
#             barcode_check_instance.barcode6 = form.cleaned_data['barcode6']
#             # Handle matching barcodes here
#             if all(x == barcode_check_instance.barcode1 for x in [barcode_check_instance.barcode2,
#                                                                   barcode_check_instance.barcode3,
#                                                                   barcode_check_instance.barcode4,
#                                                                   barcode_check_instance.barcode5,
#                                                                   barcode_check_instance.barcode6]):
#                 barcode_check_instance.barcodecheck_result = form.cleaned_data['barcodecheck_result']
#                 barcode_check_instance.barcode_check_method = form.cleaned_data['barcode_check_method']
#                 barcode_check_instance.save()
#                 return render(request, 'barcodecheck/barcodecheck6_success.html')
#             else:
#                 # Handle non-matching barcodes here
#                 barcode_check_instance.barcodecheck_result = False
#                 barcode_check_instance.barcode_check_method = '6 barcode check'
#                 barcode_check_instance.save()
#             return render(request, 'barcodecheck/barcodecheck6_fail.html')
#         else:
#             # if form is not valid
#             context['barcodecheck6'] = form
#             print(form.errors.as_data())
#     else:
#         form = BarcodeCheck6Form()
#         context['barcodecheck6'] = form
#     return render(request, 'barcodecheck/barcodecheck6.html', context)
#
#
# def barcodecheck7_view(request):
#     context = {}
#     user = request.user
#     if not user.is_authenticated:
#         return redirect('login')
#     if request.method == "POST":
#         form = BarcodeCheck7Form(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = request.user
#             obj.save()
#             # Save the form instance to a variable
#             barcode_check_instance = form.save(commit=False)
#             # Assign values to model instance fields
#             barcode_check_instance.worksheet = form.cleaned_data['worksheet']
#             barcode_check_instance.barcode1 = form.cleaned_data['barcode1']
#             barcode_check_instance.barcode2 = form.cleaned_data['barcode2']
#             barcode_check_instance.barcode3 = form.cleaned_data['barcode3']
#             barcode_check_instance.barcode4 = form.cleaned_data['barcode4']
#             barcode_check_instance.barcode5 = form.cleaned_data['barcode5']
#             barcode_check_instance.barcode6 = form.cleaned_data['barcode6']
#             barcode_check_instance.barcode7 = form.cleaned_data['barcode7']
#             # Handle matching barcodes here
#             if all(x == barcode_check_instance.barcode1 for x in [barcode_check_instance.barcode2,
#                                                                   barcode_check_instance.barcode3,
#                                                                   barcode_check_instance.barcode4,
#                                                                   barcode_check_instance.barcode5,
#                                                                   barcode_check_instance.barcode6,
#                                                                   barcode_check_instance.barcode7]):
#                 barcode_check_instance.barcodecheck_result = form.cleaned_data['barcodecheck_result']
#                 barcode_check_instance.barcode_check_method = form.cleaned_data['barcode_check_method']
#                 barcode_check_instance.save()
#                 return render(request, 'barcodecheck/barcodecheck7_success.html')
#             else:
#                 # Handle non-matching barcodes here
#                 barcode_check_instance.barcodecheck_result = False
#                 barcode_check_instance.barcode_check_method = '7 barcode check'
#                 barcode_check_instance.save()
#             return render(request, 'barcodecheck/barcodecheck7_fail.html')
#         else:
#             # if form is not valid
#             context['barcodecheck7'] = form
#             print(form.errors.as_data())
#     else:
#         form = BarcodeCheck7Form()
#         context['barcodecheck7'] = form
#     return render(request, 'barcodecheck/barcodecheck7.html', context)
#
#
# def barcodecheck8_view(request):
#     context = {}
#     user = request.user
#     if not user.is_authenticated:
#         return redirect('login')
#     if request.method == "POST":
#         form = BarcodeCheck8Form(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = request.user
#             obj.save()
#             # Save the form instance to a variable
#             barcode_check_instance = form.save(commit=False)
#             # Assign values to model instance fields
#             barcode_check_instance.worksheet = form.cleaned_data['worksheet']
#             barcode_check_instance.barcode1 = form.cleaned_data['barcode1']
#             barcode_check_instance.barcode2 = form.cleaned_data['barcode2']
#             barcode_check_instance.barcode3 = form.cleaned_data['barcode3']
#             barcode_check_instance.barcode4 = form.cleaned_data['barcode4']
#             barcode_check_instance.barcode5 = form.cleaned_data['barcode5']
#             barcode_check_instance.barcode6 = form.cleaned_data['barcode6']
#             barcode_check_instance.barcode7 = form.cleaned_data['barcode7']
#             barcode_check_instance.barcode8 = form.cleaned_data['barcode8']
#             # Handle matching barcodes here
#             if all(x == barcode_check_instance.barcode1 for x in [barcode_check_instance.barcode2,
#                                                                   barcode_check_instance.barcode3,
#                                                                   barcode_check_instance.barcode4,
#                                                                   barcode_check_instance.barcode5,
#                                                                   barcode_check_instance.barcode6,
#                                                                   barcode_check_instance.barcode7,
#                                                                   barcode_check_instance.barcode8]):
#                 barcode_check_instance.barcodecheck_result = form.cleaned_data['barcodecheck_result']
#                 barcode_check_instance.barcode_check_method = form.cleaned_data['barcode_check_method']
#                 barcode_check_instance.save()
#                 return render(request, 'barcodecheck/barcodecheck8_success.html')
#             else:
#                 # Handle non-matching barcodes here
#                 barcode_check_instance.barcodecheck_result = False
#                 barcode_check_instance.barcode_check_method = '8 barcode check'
#                 barcode_check_instance.save()
#             return render(request, 'barcodecheck/barcodecheck8_fail.html')
#         else:
#             # if form is not valid
#             context['barcodecheck8'] = form
#             print(form.errors.as_data())
#     else:
#         form = BarcodeCheck8Form()
#         context['barcodecheck8'] = form
#     return render(request, 'barcodecheck/barcodecheck8.html', context)
