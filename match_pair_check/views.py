from base_check.views import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from match_pair_check.forms import *
from audit.views import AuditWorksheetSearchView


@method_decorator(login_required, name='dispatch')
class WorksheetMatchPairView(WorksheetCheckView):
    model = MatchPairCheck
    form_class = MatchPairForm
    barcode_model = MatchPairBarcode
    barcode_form = BarcodePairForm
    success_url = '/'

    def validate_barcodes(self, barcodes):
        """Check for odd number of barcodes."""
        barcodes_entered = [True for x in barcodes if x.has_changed()]
        if len(barcodes_entered) % 2 != 0:
            return 'Cannot have an odd number of barcodes entered'
        return None

    def process_saved_barcodes(self, barcodes):
        """Assign comparisonId's to barcode instances."""
        for x in range(len(barcodes)):
            if x % 2 == 0:
                barcodes[x].instance.comparisonId = barcodes[x + 1].instance
            else:
                barcodes[x].instance.comparisonId = barcodes[x - 1].instance
        barcodes.save()

@method_decorator(login_required, name='dispatch')
class AssignedMatchPairView(AssignedWorksheetCheck):
    pass


@method_decorator(login_required, name='dispatch')
class MatchPairCheckAudit(AuditWorksheetSearchView):
    model = MatchPairCheck