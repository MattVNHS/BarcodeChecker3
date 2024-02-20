from django.contrib import admin
from extractionmethods.models import Qiasymphony24Load


@admin.register(Qiasymphony24Load)
class BarcodeCheckAdmin(admin.ModelAdmin):
    list_display = ('Qiasymphony24Load_id', 'user', 'dateTime_check', 'Qiasymphony24Load_worksheet', 'Qiasymphony24Load_method',
                  'Qiasymphony24Check_result', 'sampletube1', 'sampletube2', 'sampletube3', 'sampletube4',
                  'sampletube5', 'sampletube6', 'sampletube7', 'sampletube8', 'sampletube9', 'sampletube10',
                  'sampletube11', 'sampletube12', 'sampletube13', 'sampletube14', 'sampletube15', 'sampletube16',
                  'sampletube17', 'sampletube18', 'sampletube19', 'sampletube20', 'sampletube21', 'sampletube22',
                  'sampletube23', 'sampletube24', 'elutiontube1', 'elutiontube2', 'elutiontube3', 'elutiontube4',
                  'elutiontube5', 'elutiontube6', 'elutiontube7', 'elutiontube8', 'elutiontube9', 'elutiontube10',
                  'elutiontube11', 'elutiontube12', 'elutiontube13', 'elutiontube14', 'elutiontube15', 'elutiontube16',
                  'elutiontube17', 'elutiontube18', 'elutiontube19', 'elutiontube20', 'elutiontube21', 'elutiontube22',
                  'elutiontube23', 'elutiontube24')

    # need to use user__username as user is a foriegn key defined in the model and can't be used on it own.
    # However, as user has username, first_name, last_name, and email built into we can call username from user.
    search_fields = ('Qiasymphony24Load_id', 'user__username', 'Qiasymphony24Load_worksheet', 'Qiasymphony24Load_method',
                  'Qiasymphony24Check_result', 'sampletube1', 'sampletube2', 'sampletube3', 'sampletube4',
                  'sampletube5', 'sampletube6', 'sampletube7', 'sampletube8', 'sampletube9', 'sampletube10',
                  'sampletube11', 'sampletube12', 'sampletube13', 'sampletube14', 'sampletube15', 'sampletube16',
                  'sampletube17', 'sampletube18', 'sampletube19', 'sampletube20', 'sampletube21', 'sampletube22',
                  'sampletube23', 'sampletube24', 'elutiontube1', 'elutiontube2', 'elutiontube3', 'elutiontube4',
                  'elutiontube5', 'elutiontube6', 'elutiontube7', 'elutiontube8', 'elutiontube9', 'elutiontube10',
                  'elutiontube11', 'elutiontube12', 'elutiontube13', 'elutiontube14', 'elutiontube15', 'elutiontube16',
                  'elutiontube17', 'elutiontube18', 'elutiontube19', 'elutiontube20', 'elutiontube21', 'elutiontube22',
                  'elutiontube23', 'elutiontube24')
    readonly_fields = ('dateTime_check',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()