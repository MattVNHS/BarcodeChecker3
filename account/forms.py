from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.contrib.auth import authenticate


# As we created a customer user and usermanager we need to create a customer user registration form. Using the
# UserCreationForms to base off
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text=' Required. Add a valid email address')
    username = forms.CharField(max_length=60, help_text='Required')
    first_name = forms.CharField(max_length=60, help_text=' Required')
    last_name = forms.CharField(max_length=60, help_text=' Required')

    class Meta:
        model = Account
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')


# Form for authenticating users - using a complete custom form for this
class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    # What is needed to log in with
    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            password = self.cleaned_data["password"]
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'username', 'first_name', 'last_name')

    # Think below is if you want the user to be able to change their username, and email
    # def clean_email(self):
    #     if self.is_valid():
    #         email = self.cleaned_data['email']
    #     try:
    #         account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
    #     except Account.DoesNotExist:
    #         return email
    #     raise forms.ValidationError('Email "%s" is already in use.' % email)
    #
    # def clean_username(self):
    #     if self.is_valid():
    #         username = self.cleaned_data['username']
    #     try:
    #         account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
    #     except Account.DoesNotExist:
    #         return username
    #     raise forms.ValidationError('Username "%s" is already in use.' % username)
