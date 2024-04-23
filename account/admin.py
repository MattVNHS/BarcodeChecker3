from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import *

#admin.site.register(ShireUser, UserAdmin)





# # Defining the admin screen layout (what information is in the columns and search boxes
# class AccountAdmin(UserAdmin):
#     list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_admin', 'is_staff')
#     search_fields = ('email', 'username', 'first_name', 'last_name')
#     readonly_fields = ('date_joined', 'last_login')
#
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()
#
#
# admin.site.register(Account, AccountAdmin)

