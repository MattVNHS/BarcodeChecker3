# Generated by Django 5.0.1 on 2024-07-04 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match_all_check', '0002_alter_matchpairbarcode_comparisonid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matchallcheck',
            options={'verbose_name_plural': 'Match All Checks'},
        ),
        migrations.AlterModelOptions(
            name='matchpaircheck',
            options={'verbose_name_plural': 'Match Pair Checks'},
        ),
    ]
