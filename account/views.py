from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse


class Login(TemplateView):
    template_name = 'account/login.html'
    title = 'WMRGL'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

    def post(self, request):
        _username = request.POST["txtUsername"]
        _password = request.POST["txtPassword"]

        user = authenticate(request, username=_username, password=_password)

        if user is not None:

            login(request, user)
            return HttpResponseRedirect(reverse('home'))

        else:
            # Otherwise, return with failure message
            messages.warning(self.request, 'The username or password are not valid')

            return render(request, self.template_name)


# # How to logout of the application
def logout_view(request):
    logout(request)
    return redirect('login')