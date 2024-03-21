from django.db import models
from django.conf import settings


class Check(models.Model):
    dateTime_check = models.DateTimeField(verbose_name='date_and_time', auto_now_add=True)
    worksheet = models.CharField(max_length=12)
    barcode_count = models.IntegerField()
    check_pass = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return ( f"{self.user}: {self.worksheet}, {self.dateTime_check.strftime("%H:%M:%S %d-%m-%Y")}")


class Barcode(models.Model):
    barcode = models.CharField(max_length=10)
    comparisonId = models.IntegerField(null=True)
    Check = models.ForeignKey(Check, on_delete=models.CASCADE)

    def __str__(self):
        return ( f"{self.barcode}")