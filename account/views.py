from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse


class Login(TemplateView):

    template_name = 'account/login.html'
    title = 'WMRGL'

    def get(self, request):
        _context = {
            "Title": self.title,
        }
        return render(request, self.template_name, _context)


    def post(self, request):

        try:
            _username = request.POST["txtUsername"]
            _password = request.POST["txtPassword"]

            user = authenticate(request, username=_username, password=_password)

            if user is not None:

                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                # Otherwise, return with failure message

                _context = {
                    "Title": self.title,
                    "error_message": "The username or password are not valid",
                }

                return render(request, self.template_name, _context)

        except Exception as ex:
            # Redisplay the login screen

            _context = {
                "Title": self.title,
                "error_message": "The username or password are not valid with error message " + str(ex)
            }
            print('Exception')
            return render(request, self.template_name, _context)



#from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm


#
# def registration_view(request):
#     context = {}
#     if request.POST:
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')
#             account = authenticate(email=email, password=raw_password)
#             login(request, account)
#             return redirect('home')
#         else:
#             context['registration_form'] = form
#
#     else:
#         form = RegistrationForm()
#         context['registration_form'] = form
#     return render(request, 'account/register.html', context)
#
#
# # How to logout of the application
def logout_view(request):
    logout(request)
    return redirect('home')
#
#
# def login_view(request):
#     context = {}
#     user = request.user
#     if user.is_authenticated:
#         return redirect("home")
#     if request.POST:
#         form = AccountAuthenticationForm(request.POST)
#         if form.is_valid():
#             email = request.POST['email']
#             password = request.POST['password']
#             user = authenticate(email=email, password=password)
#             if user:
#                 login(request, user)
#                 return redirect("home")
#     else:
#         form = AccountAuthenticationForm()
#
#     context['login_form'] = form
#     return render(request, 'account/login.html', context)
#
# def account_view(request):
#     if not request.user.is_authenticated:
#         return redirect("login")
#     context = {}
#     if request.POST:
#         form = AccountUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.initial = {
#                 "email": request.POST['email'],
#                 "username": request.POST['username'],
#                 "first_name": request.POST['first_name'],
#                 "last_name": request.POST['last_name'],
#             }
#             form.save()
#             context['success_message'] = "Updated"
#     else:
#             form = AccountUpdateForm(
#             initial={
#                 "email": request.user.email,
#                 "username": request.user.username,
#                 "first_name": request.user.first_name,
#                 "last_name": request.user.last_name,
#                 }
#             )
#     context['account_form'] = form
#     return render(request, 'account/account.html', context)