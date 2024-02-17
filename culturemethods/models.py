from django.db import models
from django.conf import settings


class CultureCheck(models.Model):
    culturecheck_id = models.AutoField(primary_key=True)
    culturecheck_method = models.CharField(max_length=30)
    dateTime_check = models.DateTimeField(verbose_name='date_and_time', auto_now_add=True)
    culturecheckbarcode1 = models.CharField(max_length=22)
    culturecheckbarcode2 = models.CharField(max_length=22)
    culturecheckbarcode3 = models.CharField(max_length=22)
    culturecheckbarcode4 = models.CharField(max_length=22)
    culturecheckbarcode5 = models.CharField(max_length=22)
    culturecheckbarcode6 = models.CharField(max_length=22)
    culturecheckbarcode7 = models.CharField(max_length=22)
    culturecheckbarcode8 = models.CharField(max_length=22)
    culturecheckbarcode9 = models.CharField(max_length=22)
    culturecheckbarcode10 = models.CharField(max_length=22)
    culturecheckbarcode11 = models.CharField(max_length=22)
    culturecheckbarcode12 = models.CharField(max_length=22)
    culturecheckbarcode13 = models.CharField(max_length=22)
    culturecheckbarcode14 = models.CharField(max_length=22)
    culturecheckbarcode15 = models.CharField(max_length=22)
    culturecheckbarcode16 = models.CharField(max_length=22)
    culturecheck_result = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.culturecheck_id} {self.culturecheck_method} {self.dateTime_check} {self.culturecheckbarcode1}"
                f"{self.culturecheckbarcode2} {self.culturecheckbarcode3} {self.culturecheckbarcode4}"
                f"{self.culturecheckbarcode5} {self.culturecheckbarcode6} {self.culturecheckbarcode7}"
                f"{self.culturecheckbarcode8} {self.culturecheckbarcode9} {self.culturecheckbarcode10}"
                f"{self.culturecheckbarcode11} {self.culturecheckbarcode12} {self.culturecheckbarcode13}"
                f"{self.culturecheckbarcode14} {self.culturecheckbarcode15} {self.culturecheckbarcode16}"
                f"{self.culturecheck_result} {self.user}")
