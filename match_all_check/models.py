from base_check.models import *
import re

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


class MatchAllSlideCheck(Check):
    def checkPassFail(self):
        barcodes_entered = self.barcodes.exclude(barcode="")
        slide_labnos =  [re.search("^[A-Z]\d{2}[.]\d{5,6}", x.barcode).group() for x in barcodes_entered]
        if all(x == slide_labnos[0] for x in slide_labnos):
            self.check_pass = True
        self.save()
        return self.check_pass

    class Meta:
        verbose_name = "Match All Slide Check"
        verbose_name_plural = "Match All Slide Checks"


class MatchAllSlideBarcode(SlideBarcode):
    Check = models.ForeignKey(MatchAllSlideCheck, on_delete=models.CASCADE, related_name="barcodes")

    class Meta:
        verbose_name = "match all barcode"