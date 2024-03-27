"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from homepage.views import *
from account.views import *
from barcodecheck.views import *
from extractionmethods.views import *
from culturemethods.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_screen_view, name='home'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('account/', account_view, name='account'),

    path('barcodecheck/<int:barcode_count>/', BarcodecheckFormView.as_view(), name='barcodecheck'),
    path('createbarcodecheck/', BarcodecheckCreateView.as_view(), name='createbarcodecheck'),

    path('QiasymphonyCheck/<int:barcode_count>/', QiasymphonyFormView.as_view(), name='Qiasymphony'),

    path('culturecheck2/', culturecheck2_view, name='2barcodecheck_culture'),
    path('culturecheck3/', culturecheck3_view, name='3barcodecheck_culture'),
    path('culturecheck4/', culturecheck4_view, name='4barcodecheck_culture'),
    path('culturecheck5/', culturecheck5_view, name='5barcodecheck_culture'),
    path('culturecheck6/', culturecheck6_view, name='6barcodecheck_culture'),
    path('culturecheck7/', culturecheck7_view, name='7barcodecheck_culture'),
    path('culturecheck8/', culturecheck8_view, name='8barcodecheck_culture'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    # Custom contrib.auth - all below are required to be defined.
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
