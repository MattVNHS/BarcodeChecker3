from base_check.models import *


class MatchAllCheck(Check):
    def checkPassFail(self):
        barcodes_entered = self.barcodes.exclude(barcode="")
        if all(x.barcode == barcodes_entered[0].barcode for x in barcodes_entered):
            self.check_pass = True
        self.save()
        return self.check_pass

    class Meta:
        verbose_name = "Match All Check"
        verbose_name_plural = "Match All Checks"


class MatchAllBarcode(SampleBarcode):
    Check = models.ForeignKey(MatchAllCheck, on_delete=models.CASCADE, related_name="barcodes")

    class Meta:
        verbose_name = "match all barcode"
