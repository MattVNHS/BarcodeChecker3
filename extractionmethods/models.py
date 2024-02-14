from django.db import models
from datetime import datetime
from django.conf import settings


class Qiasymphony24Load(models.Model):
    Qiasymphony24Load_id = models.AutoField(primary_key=True)
    Qiasymphony24Load_method = models.CharField(max_length=30)
    Qiasymphony24Load_worksheet = models.CharField(max_length=12)
    Qiasymphony24Check_result = models.BooleanField(default=False)
    dateTime_check = models.DateTimeField(verbose_name='date_and_time', auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sampletube1 = models.CharField(max_length=10)
    sampletube2 = models.CharField(max_length=10)
    sampletube3 = models.CharField(max_length=10)
    sampletube4 = models.CharField(max_length=10)
    sampletube5 = models.CharField(max_length=10)
    sampletube6 = models.CharField(max_length=10)
    sampletube7 = models.CharField(max_length=10)
    sampletube8 = models.CharField(max_length=10)
    sampletube9 = models.CharField(max_length=10)
    sampletube10 = models.CharField(max_length=10)
    sampletube11 = models.CharField(max_length=10)
    sampletube12 = models.CharField(max_length=10)
    sampletube13 = models.CharField(max_length=10)
    sampletube14 = models.CharField(max_length=10)
    sampletube15 = models.CharField(max_length=10)
    sampletube16 = models.CharField(max_length=10)
    sampletube17 = models.CharField(max_length=10)
    sampletube18 = models.CharField(max_length=10)
    sampletube19 = models.CharField(max_length=10)
    sampletube20 = models.CharField(max_length=10)
    sampletube21 = models.CharField(max_length=10)
    sampletube22 = models.CharField(max_length=10)
    sampletube23 = models.CharField(max_length=10)
    sampletube24 = models.CharField(max_length=10)
    elutiontube1 = models.CharField(max_length=10)
    elutiontube2 = models.CharField(max_length=10)
    elutiontube3 = models.CharField(max_length=10)
    elutiontube4 = models.CharField(max_length=10)
    elutiontube5 = models.CharField(max_length=10)
    elutiontube6 = models.CharField(max_length=10)
    elutiontube7 = models.CharField(max_length=10)
    elutiontube8 = models.CharField(max_length=10)
    elutiontube9 = models.CharField(max_length=10)
    elutiontube10 = models.CharField(max_length=10)
    elutiontube11 = models.CharField(max_length=10)
    elutiontube12 = models.CharField(max_length=10)
    elutiontube13 = models.CharField(max_length=10)
    elutiontube14 = models.CharField(max_length=10)
    elutiontube15 = models.CharField(max_length=10)
    elutiontube16 = models.CharField(max_length=10)
    elutiontube17 = models.CharField(max_length=10)
    elutiontube18 = models.CharField(max_length=10)
    elutiontube19 = models.CharField(max_length=10)
    elutiontube20 = models.CharField(max_length=10)
    elutiontube21 = models.CharField(max_length=10)
    elutiontube22 = models.CharField(max_length=10)
    elutiontube23 = models.CharField(max_length=10)
    elutiontube24 = models.CharField(max_length=10)

    def __str__(self):
        return (f"{self.Qiasymphony24Load_id} {self.Qiasymphony24Load_method} {self.Qiasymphony24Load_worksheet} {self.Qiasymphony24Check_result}"
                f"{self.dateTime_check} {self.user} {self.sampletube1} {self.sampletube2} {self.sampletube3} {self.sampletube4}"
                f" {self.sampletube5} {self.sampletube6} {self.sampletube7} {self.sampletube8} {self.sampletube9} {self.sampletube10}"
                f" {self.sampletube11} {self.sampletube12} {self.sampletube13} {self.sampletube14} {self.sampletube15} {self.sampletube16}"
                f" {self.sampletube17} {self.sampletube18} {self.sampletube19} {self.sampletube20} {self.sampletube21} {self.sampletube22}"
                f" {self.sampletube23} {self.sampletube24} {self.elutiontube1} {self.elutiontube2} {self.elutiontube3} {self.elutiontube4}"
                f" {self.elutiontube5} {self.elutiontube6} {self.elutiontube7} {self.elutiontube8} {self.elutiontube9} {self.elutiontube10}"
                f" {self.elutiontube11} {self.elutiontube12} {self.elutiontube13} {self.elutiontube14} {self.elutiontube15} {self.elutiontube16}"
                f" {self.elutiontube17} {self.elutiontube18} {self.elutiontube19} {self.elutiontube20} {self.elutiontube21} {self.elutiontube22}"
                f" {self.elutiontube23} {self.elutiontube24}")
