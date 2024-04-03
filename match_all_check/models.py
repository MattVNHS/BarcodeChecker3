from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


class Check(models.Model):
    dateTime_check = models.DateTimeField(verbose_name='date_and_time', auto_now_add=True)
    worksheet = models.CharField(max_length=12, validators=[RegexValidator(regex=r'^\d{6}$',
                                                                           message='invalid worksheet entered')])
    barcode_count = models.IntegerField()
    check_pass = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Check"
        verbose_name_plural = "Checks"

    def __str__(self):
        return ( f"{self.user}: {self.worksheet}, {self.dateTime_check.strftime("%H:%M:%S %d-%m-%Y")}")


class Barcode(models.Model):
    barcode = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^[A-Z]\d{2}[.]\d{5,6}$',
                                                                         message='invalid lab number entered')])
    comparisonId = models.IntegerField(null=True)
    Check = models.ForeignKey(Check, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Barcode"
        verbose_name_plural = "Barcodes"
    def __str__(self):
        return f"{self.pk}: {self.barcode}"