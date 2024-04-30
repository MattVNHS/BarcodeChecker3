from django.db import models

class STAFF(models.Model):
    STAFF_CODE = models.CharField(primary_key=True, max_length=4, db_column="STAFF_CODE" )  # Unique identifier
    PASSWORD = models.CharField(max_length=10)
    NAME = models.CharField(max_length=50)
    EMAIL = models.EmailField(verbose_name='email', max_length=70)
    # DNA_MODULE_ACCESS and CYTO_MODULE_ACCESS ?
    EMPLOYMENT_END_DATE = models.DateTimeField()
    class Meta:
        app_label = 'account'
        managed = False
        db_table = '[dbo].[STAFF]'
