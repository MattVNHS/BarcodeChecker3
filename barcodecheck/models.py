from django.db import models


class BarcodeChecker(models.Model):
    barcodecheckfunction = models.CharField(max_length=30)
    user = models.CharField(max_length=30)
    dateTime_check = models.DateTimeField(verbose_name='date.joined', auto_now_add=True)
    worksheet = models.CharField(max_length=10)
    barcode1 = models.CharField(max_length=10)
    barcode2 = models.CharField(max_length=10)

