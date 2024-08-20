from base_check.views import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from match_pair_check.models import *
from match_pair_check.forms import *


@method_decorator(login_required, name='dispatch')
class WorksheetMatchPairView(WorksheetCheckView):
    model = MatchPairCheck
    form_class = MatchPairForm
    barcode_model = MatchPairBarcode
    barcode_form = BarcodePairForm
    success_url = '/'

    def form_valid(self, form):
        context = self.get_context_data()
        barcodes = context['barcodes']
        worksheet_number = context["worksheet_number"]
        barcodes_entered = [True for x in barcodes if x.has_changed()]
        if len(barcodes_entered) % 2 != 0:
            messages.warning(self.request, 'Cannot have an odd number of barcodes entered')
            return self.form_invalid(form)
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.worksheet, created = Worksheet.objects.get_or_create(worksheet_number=worksheet_number)
        self.object.check_number = context["check_number"]
        self.object.check_description = context["check_description"]
        if barcodes.is_valid():
            self.object.save()
            barcodes.instance = self.object
            barcodes.save()
            # assign comparisonId's to barcode instances.
            # if x % 2 == 0: then x is a multiple of 2 (or is 0)
            # therefore its comparisonId should be the next barcodes pk. This is reversed if x % 2 == 0: is False
            # barcodes[0].comparisonId should be barcodes[1] and barcodes[1].comparisonId should be barcodes[0]
            # there is probably a better way of doing this....
            for x in range(len(barcodes)):
                if x % 2 == 0:
                    barcodes[x].instance.comparisonId = barcodes[x + 1].instance
                else:
                    barcodes[x].instance.comparisonId = barcodes[x - 1].instance
            barcodes.save()

            for error in barcodes.errors:
                messages.warning(self.request, error)

            if self.object.checkPassFail():
                messages.success(self.request, 'Check Passed')
            else:
                messages.warning(self.request, 'Check Failed - Barcodes do not match')

        else:
            return self.form_invalid(form)
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class AssignedMatchPairView(AssignedMatchAllWorksheetCheck):
    pass


@method_decorator(login_required, name='dispatch')
class MatchPairCheckAudit(AuditView):
    model = MatchPairCheck