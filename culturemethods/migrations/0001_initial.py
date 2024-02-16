# Generated by Django 4.2.7 on 2024-02-16 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CultureCheck',
            fields=[
                ('culturecheck_id', models.AutoField(primary_key=True, serialize=False)),
                ('culturecheck_method', models.CharField(max_length=30)),
                ('dateTime_check', models.DateTimeField(auto_now_add=True, verbose_name='date_and_time')),
                ('culturecheckbarcode1', models.CharField(max_length=10)),
                ('culturecheckbarcode2', models.CharField(max_length=10)),
                ('culturecheckbarcode3', models.CharField(max_length=10)),
                ('culturecheckbarcode4', models.CharField(max_length=10)),
                ('culturecheckbarcode5', models.CharField(max_length=10)),
                ('culturecheckbarcode6', models.CharField(max_length=10)),
                ('culturecheckbarcode7', models.CharField(max_length=10)),
                ('culturecheckbarcode8', models.CharField(max_length=10)),
                ('culturecheckbarcode9', models.CharField(max_length=10)),
                ('culturecheckbarcode10', models.CharField(max_length=10)),
                ('culturecheckbarcode11', models.CharField(max_length=10)),
                ('culturecheckbarcode12', models.CharField(max_length=10)),
                ('culturecheckbarcode13', models.CharField(max_length=10)),
                ('culturecheckbarcode14', models.CharField(max_length=10)),
                ('culturecheckbarcode15', models.CharField(max_length=10)),
                ('culturecheckbarcode16', models.CharField(max_length=10)),
                ('culturecheck_result', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]