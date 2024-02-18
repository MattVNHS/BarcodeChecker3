from django.contrib import admin
from barcodecheck.models import BarcodeCheck


@admin.register(BarcodeCheck)
class BarcodeCheckAdmin(admin.ModelAdmin):
    list_display = ('barcodecheckid', 'user', 'dateTime_check', 'worksheet', 'barcode_check_method', 'barcodecheck_result',
                    'barcode1', 'barcode2', 'barcode3', 'barcode4', 'barcode5', 'barcode6', 'barcode7',
                    'barcode8')
    search_fields = ('barcodecheckid', 'user', 'dateTime_check', 'barcodecheck_result', 'barcode_check_method',
                     'worksheet', 'barcode1', 'barcode2', 'barcode3', 'barcode4', 'barcode5', 'barcode6', 'barcode7',
                     'barcode8')
    readonly_fields = ('dateTime_check',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
