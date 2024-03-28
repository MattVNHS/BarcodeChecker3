from django.shortcuts import render, redirect
from homepage.forms import *
def home_screen_view(request):

    # initialise each form and pass to the context
    match_all_form = Match_all_Form()
    Match_pair_form = Match_pair_Form()
    context = {'Match_pair_form': Match_pair_form, 'match_all_form': match_all_form}

    # Each check has a form in homepage/forms.py with a hidden url_name field
    if request.method == 'POST':
        return redirect(request.POST['url_name'], barcode_count=request.POST['barcode_count'])

    return render(request, 'homepage/home.html', context)
