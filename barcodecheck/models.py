from django.db import models
from datetime import datetime


class BarcodeCheck(models.Model):
    barcodecheckid = models.AutoField(primary_key=True)
    barcode_check_function = models.CharField(max_length=30)
    dateTime_check = models.DateTimeField(verbose_name='date_and_time', auto_now_add=True)
    worksheet = models.CharField(max_length=8)
    barcode1 = models.CharField(max_length=10)
    barcode2 = models.CharField(max_length=10)
    barcodecheck_result = models.BooleanField(default=False)

    def __str__(self):
        return (f"{self.barcodecheckid} {self.barcode_check_function} {self.dateTime_check} {self.worksheet} "
                f"{self.barcode1} {self.barcode2}")



