# Generated by Django 4.0.6 on 2022-09-26 02:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driverId', models.CharField(max_length=30)),
                ('driverName', models.CharField(max_length=50)),
                ('salaryPackage', models.FloatField()),
                ('createdOn', models.DateTimeField(default=datetime.datetime(2022, 9, 26, 7, 59, 24, 903304))),
            ],
        ),
    ]
