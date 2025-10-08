from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


class CheckTable(models.Model):
    check_name = models.CharField(blank=True, max_length=150)
    check_hub = models.CharField(blank=True, max_length=50)
    check_process = models.CharField(blank=True, max_length=150)
    check_type = models.CharField(blank=True, max_length=150) #This needs to be choices from existing check models
    barcode_range_start = models.IntegerField(null=False, default=2)
    barcode_range_stop = models.IntegerField(null=False, default=2)
    barcode_range_step = models.IntegerField(null=False, default=2)
    class Meta:
        verbose_name = "Check Table"

class Worksheet(models.Model):
    worksheet_number = models.CharField(max_length=12, validators=[RegexValidator(regex=r'^\d{6}$|""',
                                                                           message='invalid worksheet entered')], primary_key=True)

    def __str__(self):
        return f"{self.worksheet_number}"

# Check model is abstract - Specific check models inherit from the Check model and define the checkPassFail method.


class Check(models.Model):
    dateTime_check = models.DateTimeField(verbose_name='date_and_time', auto_now_add=True)
    worksheet = models.ForeignKey(Worksheet, on_delete=models.CASCADE, null=True)
    check_number = models.IntegerField(null=True, default=1)
    check_description = models.CharField(blank=True, max_length=None)
    check_pass = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Check"
        verbose_name_plural = "Checks"
        abstract = True

    def __str__(self):
        return f"{self.user}: {self.worksheet}, {self.check_number}, {self.dateTime_check.strftime("%H:%M:%S %d-%m-%Y")}"

    def checkPassFail(self):
        pass



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
        return f"{self.barcode}"


class SampleBarcode(Barcode):
    barcode = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^[A-Z]\d{2}[.]\d{5,6}$',
                                                                         message='invalid lab number entered')])

    class Meta:
        abstract = True

