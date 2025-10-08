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

from django.conf import settings
from django.conf.urls.static import static

from account.views import *
from audit.views import *
from homepage.views import *
from match_all_check.views import *
from match_pair_check.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_screen_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('login/', Login.as_view(), name='login'),


    path('match_all_check/<int:barcode_count>/', MatchAllView.as_view(), name='MatchAllView'),
    path('match_all_check_worksheet/<int:barcode_count>/', WorksheetMatchAllView.as_view(), name='WorksheetMatchAllView'),
    path('match_pair_check/<int:barcode_count>/', WorksheetMatchPairView.as_view(), name='WorksheetMatchPairView'),

    path('audit_search/', AuditWorksheetSearchView.as_view(), name='Audit'),
    path('audit_barcode_search/', AuditBarcodeSearchView.as_view(), name='barcode_search'),
   # path('match_all_check_audit/', MatchAllCheckAudit.as_view(), name='Audit'),


    path('match_all_check_worksheet/<int:worksheet_number>/<int:check_number>/<str:check_description>/<int:barcode_count>/', AssignedMatchAllView.as_view(), name='WorksheetMatchAllView'),
    path('match_pair_check_worksheet/<int:worksheet_number>/<int:check_number>/<str:check_description>/<int:barcode_count>/', AssignedMatchPairView.as_view(), name='WorksheetMatchPairView'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
