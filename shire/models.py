from django.db import models


# Read-only models for existing tables in the Shire SQL Server database.
# app_label = 'account' makes AccountRouter send reads to the Shire_Data database
# and stops migrations being created for them (allow_migrate returns False).
# managed = False tells Django it does not own or create these tables.
#
# Both tables have a COMPOSITE primary key in SQL Server, which Django 5.0 cannot
# represent. Django requires a single primary_key field, so the first key column is
# marked as primary_key=True. That column is NOT unique on its own, so:
#   - always filter on BOTH key columns when you need a single row
#   - don't rely on .pk, .get(pk=...), .save() or .delete() for these models


class DNA_EXTRACTS(models.Model):
    # Real primary key in SQL Server: (LABNO, TUBE)
    # always filter on BOTH key columns when you need a single row
    LABNO = models.CharField(primary_key=True, max_length=50)
    TUBE = models.CharField(max_length=20)
    EXTRACTION_METHOD = models.CharField(max_length=30, null=True, blank=True)
    EXTRACT_SHEET = models.CharField(max_length=10, null=True, blank=True)
    UPDATEDBY = models.CharField(max_length=10, null=True, blank=True)
    UPDATEDDATE = models.DateTimeField(null=True, blank=True)
    UPDATEDTIME = models.DateTimeField(null=True, blank=True)
    TUBE_BARCODE = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        managed = False
        db_table = '[dbo].[DNA_EXTRACTS]'
        unique_together = (('LABNO', 'TUBE'),)

    def __str__(self):
        return f"{self.LABNO} / {self.TUBE}"


class DNA_EXTRACTSHEET_DET(models.Model):
    # Real primary key in SQL Server: (EXTRACTSHEET, POSITION)
    # always filter on BOTH key columns when you need a single row
    EXTRACTSHEET = models.CharField(primary_key=True, max_length=10)
    POSITION = models.SmallIntegerField()
    LABNO = models.CharField(max_length=30, null=True, blank=True)
    TUBE = models.CharField(max_length=20, null=True, blank=True)
    RACK_BARCODE = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        managed = False
        db_table = '[dbo].[DNA_EXTRACTSHEET_DET]'
        unique_together = (('EXTRACTSHEET', 'POSITION'),)

    def __str__(self):
        return f"{self.EXTRACTSHEET} pos {self.POSITION}"

