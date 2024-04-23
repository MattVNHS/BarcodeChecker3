from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



# Extending the baseUserManager that comes with django by defining create_user and create_superuser
# class ShireUserManager(BaseUserManager):
#     def create_user(self, email, username, first_name, last_name, password=None):
#         raise ValueError("New users must have a Shire account.")
#
#
#     def create_superuser(self, email, username, first_name, last_name, password):
#         raise ValueError("New users must have a Shire account. Superusers can then be created using Django Admin")



class STAFF(models.Model):
    STAFF_CODE = models.CharField(primary_key=True, max_length=4, db_column="STAFF_CODE" )  # Unique identifier
    PASSWORD = models.CharField(max_length=10)
    NAME = models.CharField(max_length=50)
    EMAIL = models.EmailField(verbose_name='email', max_length=70)
    # DNA_MODULE_ACCESS and CYTO_MODULE_ACCESS ?
    EMPLOYMENT_END_DATE = models.DateTimeField()
    REQUIRED_FIELDS = []
    class Meta:
        app_label = 'account'
        managed = False
        db_table = '[dbo].[STAFF]'

#
# class ShireUser(AbstractBaseUser, PermissionsMixin): #STAFF):
#     # Inherits from the STAFF model, this means STAFF_CODE etc comes from Shire_Data database while
#     # the django specific parts of the user model is stored in the local database
#     # is_staff = allows users to access admin screen
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#
#     STAFF_CODE = models.CharField(primary_key=True, max_length=4, db_column="STAFF_CODE")  # Unique identifier
#     PASSWORD = models.CharField(max_length=10, db_column='PASSWORD')
#     NAME = models.CharField(max_length=50)
#     EMAIL = models.EmailField(verbose_name='email', max_length=70)
#     # DNA_MODULE_ACCESS and CYTO_MODULE_ACCESS ?
#     EMPLOYMENT_END_DATE = models.DateTimeField()
#
#     class Meta:
#         app_label = 'account'
#         managed = False
#         db_table = '[dbo].[STAFF]'
#
#     USERNAME_FIELD = 'STAFF_CODE'
#     PASSWORD_FIELD = 'PASSWORD'
#     EMAIL_FIELD = 'EMAIL'
#     REQUIRED_FIELDS = ['EMAIL']
#
#
#
#     objects = ShireUserManager()
#
#     def __str__(self):
#         return self.username
#
#     # These perm = permissions needed for a custom user to work
#     def has_perm(self, perm, obj=None):
#         return self.is_admin
#
#     def has_module_perms(self, app_label):
#         return True


    #email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    # username = models.CharField(max_length=30, unique=True)
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    # date_joined = models.DateTimeField(verbose_name='date.joined', auto_now_add=True)
    # last_login = models.DateTimeField(verbose_name='last.login', auto_now_add=True)
    # is_admin = models.BooleanField(default=False)


    # username_field is the field we want user to log in with. Required field is the field that users need to enter to
    # register
    # USERNAME_FIELD = 'STAFF_CODE'
    # EMAIL_FIELD = 'EMAIL'
    # REQUIRED_FIELDS = ['EMAIL']

    # Need to reference the account manage we built above (create_user and create_superuser)
    # objects = ShireUserManager()
    #
    # def __str__(self):
    #     return self.username
    #
    # # These perm = permissions needed for a custom user to work
    # def has_perm(self, perm, obj=None):
    #     return self.is_admin
    #
    # def has_module_perms(self, app_label):
    #     return True

#
#
# # Extending the baseUserManager that comes with django by defining create_user and create_superuser
# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, first_name, last_name, password=None):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not username:
#             raise ValueError("Users must have a username")
#         if not first_name:
#             raise ValueError("Users must have a first name")
#         if not last_name:
#             raise ValueError("Users must have a last name")
#
# # If they do have all the above then we create a user (creating user) - normalize_email converts email all to lower case
#         user = self.model(
#                 email=self.normalize_email(email),
#                 username=username,
#                 first_name=first_name,
#                 last_name=last_name,
#             )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, username, first_name, last_name, password):
#         user = self.create_user(
#                 email=self.normalize_email(email),
#                 password=password,
#                 username=username,
#                 first_name=first_name,
#                 last_name=last_name,
#                 )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#
#


