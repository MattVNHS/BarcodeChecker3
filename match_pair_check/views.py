from base_check.views import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from match_pair_check.forms import *
from audit.views import AuditWorksheetSearchView
from django.db import transaction

def odd_number_check(barcodes):
    """Check for odd numbers of barcodes."""
    barcodes_entered_count = sum(1 for form in barcodes if form.has_changed())
    if barcodes_entered_count % 2 != 0:
        return 'Cannot have an odd number of barcodes entered'
    return None

def assign_comparisonId(barcodes):
    """Assign comparisonId's to barcode instances."""
    barcodes = [form for form in barcodes if form.has_changed()]
    barcode_pairs = zip(barcodes[::2], barcodes[1::2])
    with transaction.atomic():
        for even_form, odd_form in barcode_pairs:
            instance1 = even_form.instance
            instance2 = odd_form.instance

            instance1.comparisonId = instance2
            instance2.comparisonId = instance1

            instance1.save()
            instance2.save()

''' This mixin keeps the worksheet views DRY.
 Make sure to add it before WorksheetCheckView or AssignedWorksheetCheck or the methods will be overwritten'''
class MatchPairValidationMixin:
    def validate_barcodes(self, barcodes):
        return odd_number_check(barcodes)

    def process_saved_barcodes(self, barcodes):
        return assign_comparisonId(barcodes)

@method_decorator(login_required, name='dispatch')
class WorksheetMatchPairView(MatchPairValidationMixin, WorksheetCheckView):
    model = MatchPairCheck
    form_class = MatchPairForm
    barcode_model = MatchPairBarcode
    barcode_form = BarcodePairForm
    success_url = '/'

@method_decorator(login_required, name='dispatch')
class AssignedMatchPairView(MatchPairValidationMixin, AssignedWorksheetCheck):
    model = MatchPairCheck
    form_class = MatchPairForm
    barcode_model = MatchPairBarcode
    barcode_form = BarcodePairForm
    success_url = '/'
    view_name = 'WorksheetMatchPairView'

@method_decorator(login_required, name='dispatch')
class MatchPairCheckAudit(AuditWorksheetSearchView):
    model = MatchPairCheck