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