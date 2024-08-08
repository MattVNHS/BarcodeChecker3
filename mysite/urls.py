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
from django.urls import path

from homepage.views import *
from account.views import *
from match_all_check.views import *
from match_pair_check.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_screen_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('login/', Login.as_view(), name='login'),


    path('match_all_check/<int:barcode_count>/', MatchAllCheckView.as_view(), name='MatchAllCheckView'),
    path('match_all_check_worksheet/<int:barcode_count>/', MatchAllCheckWorksheetView.as_view(), name='MatchAllCheckWorksheetView'),
    path('match_pair_check/<int:barcode_count>/', MatchPairCheckView.as_view(), name='MatchPairCheckView'),
    path('match_all_check_worksheet/<int:worksheet_number>/<int:check_number>/<str:check_description>/<int:barcode_count>/', MatchAllCheckWorksheetView.as_view(), name='MatchAllCheckWorksheetView'),
]
