from base_check.models import *


class MatchAllCheck(Check):
    def checkPassFail(self):
        barcodes_entered = self.matchallbarcode_set.exclude(barcode="")
        if all(x.barcode == barcodes_entered[0].barcode for x in barcodes_entered):
            self.check_pass = True
        self.save()
        return self.check_pass

    class Meta:
        verbose_name_plural = "Match All Checks"


class MatchPairCheck(Check):
    def checkPassFail(self):
        barcodes = self.matchpairbarcode_set.exclude(barcode="")
        if all(x.barcode == x.comparisonId.barcode for x in barcodes):
            self.check_pass = True
        self.save()
        return self.check_pass

    class Meta:
        verbose_name_plural = "Match Pair Checks"


class MatchAllBarcode(SampleBarcode):
    Check = models.ForeignKey(MatchAllCheck, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "matchpairbarcode"


class MatchPairBarcode(SampleBarcode):
    comparisonId = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    Check = models.ForeignKey(MatchPairCheck, on_delete=models.CASCADE)