from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

# Check model is abstract - MatchAllCheck and MatchPairCheck inherit from the Check model and define the checkPassFail method.


class Check(models.Model):
    dateTime_check = models.DateTimeField(verbose_name='date_and_time', auto_now_add=True)
    worksheet = models.CharField(max_length=12, validators=[RegexValidator(regex=r'^\d{6}$|""',
                                                                           message='invalid worksheet entered')])
    check_pass = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Check"
        verbose_name_plural = "Checks"
        abstract = True

    def __str__(self):
        return f"{self.user}: {self.worksheet}, {self.dateTime_check.strftime("%H:%M:%S %d-%m-%Y")}"

    def checkPassFail(self):
        pass


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


# Barcode model is abstract - SampleBarcode inherits from the Barcode model and defines SampleBarcode.barcode validator.
# This allows for extension of new Barcode classes, e.g. ReagentBarcode with their own validators.

# SampleBarcode model is abstract - MatchAllBarcode and MatchPairBarcode inherit from the SampleBarcode model.

class Barcode(models.Model):
    barcode = None
    Check = None

    class Meta:
        verbose_name = "Barcode"
        verbose_name_plural = "Barcodes"
        abstract = True

    def __str__(self):
        return f"{self.pk}: {self.barcode}"


class SampleBarcode(Barcode):
    barcode = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^[A-Z]\d{2}[.]\d{5,6}$',
                                                                         message='invalid lab number entered')])

    class Meta:
        abstract = True


class MatchAllBarcode(SampleBarcode):
    Check = models.ForeignKey(MatchAllCheck, on_delete=models.CASCADE)


class MatchPairBarcode(SampleBarcode):
    comparisonId = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    Check = models.ForeignKey(MatchPairCheck, on_delete=models.CASCADE)