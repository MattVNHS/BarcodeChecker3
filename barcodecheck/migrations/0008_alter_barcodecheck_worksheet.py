# Generated by Django 5.0.1 on 2024-02-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcodecheck', '0007_barcodecheck_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barcodecheck',
            name='worksheet',
            field=models.CharField(max_length=12),
        ),
    ]