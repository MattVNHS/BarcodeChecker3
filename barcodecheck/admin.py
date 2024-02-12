from django.contrib import admin
from barcodecheck.models import BarcodeCheck


@admin.register(BarcodeCheck)
class BarcodeCheckAdmin(admin.ModelAdmin):
    list_display = ('barcodecheckid', 'user', 'barcodecheck_result', 'barcode_check_function', 'dateTime_check', 'worksheet', 'barcode1',
                    'barcode2')
    search_fields = ('barcodecheckid', 'barcodecheck_result', 'barcode_check_function', 'dateTime_check', 'worksheet', 'barcode1', 'barcode2')
    readonly_fields = ('dateTime_check',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
