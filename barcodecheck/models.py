from django.db import models
from datetime import datetime
from django.conf import settings


# class BarcodeCheck(models.Model):
#     barcodecheckid = models.AutoField(primary_key=True)
#     barcode_check_method = models.CharField(max_length=30)
#     dateTime_check = models.DateTimeField(verbose_name='date_and_time', auto_now_add=True)
#     worksheet = models.CharField(max_length=12)
#     barcode1 = models.CharField(max_length=10)
#     barcode2 = models.CharField(max_length=10)
#     barcode3 = models.CharField(max_length=10)
#     barcode4 = models.CharField(max_length=10)
#     barcode5 = models.CharField(max_length=10)
#     barcode6 = models.CharField(max_length=10)
#     barcode7 = models.CharField(max_length=10)
#     barcode8 = models.CharField(max_length=10)
#     barcodecheck_result = models.BooleanField(default=False)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return (f"{self.barcodecheckid} {self.barcode_check_method} {self.dateTime_check} {self.worksheet} "
#                 f"{self.barcode1} {self.barcode2} {self.barcode3} {self.barcode4} {self.barcode5} {self.barcode6}"
#                 f" {self.barcode7} {self.barcode8} {self.user}")
