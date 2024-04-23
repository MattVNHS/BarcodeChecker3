# Generated by Django 5.0.1 on 2024-04-23 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='STAFF',
            fields=[
                ('STAFF_CODE', models.CharField(db_column='STAFF_CODE', max_length=4, primary_key=True, serialize=False)),
                ('PASSWORD', models.CharField(max_length=10)),
                ('NAME', models.CharField(max_length=50)),
                ('EMAIL', models.EmailField(max_length=70, verbose_name='email')),
                ('EMPLOYMENT_END_DATE', models.DateTimeField()),
            ],
            options={
                'db_table': '[dbo].[STAFF]',
                'managed': False,
            },
        ),
    ]
