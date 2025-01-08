from django.contrib import admin

# Register your models here.

from django.contrib import admin
from match_all_check.models import *
from match_pair_check.models import *
from .models import CheckTable


class MatchAllBarcodeAdmin(admin.ModelAdmin):
    list_display = ("barcode", "id")


class MatchPairBarcodeAdmin(admin.ModelAdmin):
    list_display = ("id", "barcode")


admin.site.register(MatchAllBarcode, MatchAllBarcodeAdmin)
admin.site.register(MatchPairBarcode, MatchPairBarcodeAdmin)
admin.site.register(CheckTable)


class MatchAllBarcodeInline(admin.TabularInline):
    model = MatchAllBarcode


class MatchAllCheckAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "dateTime_check", "worksheet", "check_number", "check_description", "check_pass")
    inlines = [
        MatchAllBarcodeInline,
    ]


admin.site.register(MatchAllCheck, MatchAllCheckAdmin)


class MatchPairBarcodeInline(admin.TabularInline):
    model = MatchPairBarcode


class MatchPairCheckAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "dateTime_check", "worksheet", "check_pass")
    inlines = [
        MatchPairBarcodeInline,
    ]


admin.site.register(MatchPairCheck, MatchPairCheckAdmin)



class MatchAllCheckInline(admin.TabularInline):
    model = MatchAllCheck
class WorksheetAdmin(admin.ModelAdmin):
    list_display = ["worksheet_number",]
    inlines = [
        MatchAllCheckInline,
    ]

admin.site.register(Worksheet, WorksheetAdmin)