# Generated by Django 5.0.1 on 2024-05-08 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match_all_check', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchpairbarcode',
            name='comparisonId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='match_all_check.matchpairbarcode'),
        ),
    ]
