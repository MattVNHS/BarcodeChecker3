from match_all_check.forms import *
from match_all_check.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from base_check.views import *
from audit.views import AuditWorksheetSearchView

# For checks with a worksheet we add 'worksheet' to the fields attribute.

@method_decorator(login_required, name='dispatch')
class MatchAllView(CheckView):
    model = MatchAllCheck
    barcode_model = MatchAllBarcode
    barcode_form = BarcodeForm
    success_url = '/'

@method_decorator(login_required, name='dispatch')
class WorksheetMatchAllView(WorksheetCheckView):
    model = MatchAllCheck
    form_class = MatchAllForm
    barcode_model = MatchAllBarcode
    barcode_form = BarcodeForm
    success_url = '/'

@method_decorator(login_required, name='dispatch')
class AssignedMatchAllView(AssignedWorksheetCheck):
    model = MatchAllCheck
    barcode_model = MatchAllBarcode
    barcode_form = BarcodeForm
    view_name = 'WorksheetMatchAllView'
    success_url = '/'

@method_decorator(login_required, name='dispatch')
class MatchAllCheckAudit(AuditWorksheetSearchView):
    model = MatchAllCheck
