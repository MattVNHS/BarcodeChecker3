from django.contrib import admin
from barcodecheck.models import *

admin.site.register(Barcode)


class BarcodeInline(admin.TabularInline):
    model = Barcode


class CheckAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "dateTime_check", "worksheet", "barcode_count", "check_pass")
    inlines = [
        BarcodeInline,
    ]

admin.site.register(Check, CheckAdmin)
