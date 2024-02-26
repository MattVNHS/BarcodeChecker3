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

from homepage.views import (
    home_screen_view,
)

from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
)

from barcodecheck.views import (
    BarcodecheckFormView,
    barcodecheck2_view,
    barcodecheck3_view,
    barcodecheck4_view,
    barcodecheck5_view,
    barcodecheck6_view,
    barcodecheck7_view,
    barcodecheck8_view,
)

from extractionmethods.views import (
    Qiasymphony24_view
)

from culturemethods.views import (
    culturecheck2_view,
    culturecheck3_view,
    culturecheck4_view,
    culturecheck5_view,
    culturecheck6_view,
    culturecheck7_view,
    culturecheck8_view,
)



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_screen_view, name='home'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('account/', account_view, name='account'),

    path('barcodecheck/', BarcodecheckFormView.as_view(), name='barcodecheck'),
    path('barcodecheck2/', barcodecheck2_view, name='barcodecheck2'),
    path('barcodecheck3/', barcodecheck3_view, name='barcodecheck3'),
    path('barcodecheck4/', barcodecheck4_view, name='barcodecheck4'),
    path('barcodecheck5/', barcodecheck5_view, name='barcodecheck5'),
    path('barcodecheck6/', barcodecheck6_view, name='barcodecheck6'),
    path('barcodecheck7/', barcodecheck7_view, name='barcodecheck7'),
    path('barcodecheck8/', barcodecheck8_view, name='barcodecheck8'),

    path('Qiasymphony24Check/', Qiasymphony24_view, name='Qiasymphony24'),

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
