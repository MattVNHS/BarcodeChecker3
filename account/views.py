from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

# Might be able to tidy the login view

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



# # How to logout of the application
def logout_view(request):
    logout(request)
    return redirect('login')