from django.shortcuts import render, redirect
from homepage.forms import CheckForm
from django.contrib.auth.decorators import login_required
from base_check.models import CheckTable
@login_required
def home_screen_view(request):

    # CheckTable contains the details of all checks. we inititalise a CheckForm for each and pass to the context.
    # Each CheckForm has a hidden url_name field that is used to redirect the user to the appropriate check url.

    checks = CheckTable.objects.all()
    forms = []
    for check in checks:
        check_form = CheckForm()
        check_form.fields["barcode_count"].choices = {i: i for i in range(check.barcode_range_start,
                                                                          check.barcode_range_stop,
                                                                          check.barcode_range_step)}
        check_form.fields["url_name"].initial = check.check_type
        forms.append((check.check_name, check_form))

    if request.method == "POST":
        return redirect(request.POST['url_name'], barcode_count=request.POST['barcode_count'])

    context = {"forms": forms}
    return render(request, 'homepage/home.html', context)

