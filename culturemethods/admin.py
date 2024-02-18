from django.contrib import admin
from culturemethods.models import CultureCheck


@admin.register(CultureCheck)
class BarcodeCheckAdmin(admin.ModelAdmin):
    list_display = ('culturecheck_id', 'user', 'dateTime_check', 'culturecheck_method', 'culturecheck_result',
                    'culturecheckbarcode1', 'culturecheckbarcode2', 'culturecheckbarcode3',
                    'culturecheckbarcode4', 'culturecheckbarcode5', 'culturecheckbarcode6', 'culturecheckbarcode7',
                    'culturecheckbarcode8')
    search_fields = ('culturecheck_id', 'user', 'dateTime_check', 'culturecheck_result', 'culturecheck_method',
                     'culturecheckbarcode1', 'culturecheckbarcode2', 'culturecheckbarcode3',
                     'culturecheckbarcode4', 'culturecheckbarcode5', 'culturecheckbarcode6', 'culturecheckbarcode7',
                     'culturecheckbarcode8')
    readonly_fields = ('dateTime_check',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
