from base_check.models import *


class MatchPairCheck(Check):
    def checkPassFail(self):
        barcodes = self.matchpairbarcode_set.exclude(barcode="")
        if all(x.barcode == x.comparisonId.barcode for x in barcodes):
            self.check_pass = True
        self.save()
        return self.check_pass

    class Meta:
        verbose_name = "Match Pair Check"
        verbose_name_plural = "Match Pair Checks"


class MatchPairBarcode(SampleBarcode):
    comparisonId = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    Check = models.ForeignKey(MatchPairCheck, on_delete=models.CASCADE, related_name="barcodes")