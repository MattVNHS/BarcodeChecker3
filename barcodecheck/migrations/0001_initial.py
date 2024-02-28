# Generated by Django 5.0.1 on 2024-02-28 16:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime_check', models.DateTimeField(auto_now_add=True, verbose_name='date_and_time')),
                ('worksheet', models.CharField(max_length=12)),
                ('barcode_count', models.IntegerField()),
                ('check_result', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Barcodes',
            fields=[
                ('barcodeId', models.AutoField(primary_key=True, serialize=False)),
                ('barcode', models.CharField(max_length=10)),
                ('comparisonId', models.IntegerField(null=True)),
                ('Check', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barcodecheck.check')),
            ],
        ),
    ]
