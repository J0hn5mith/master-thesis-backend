# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 12:30
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PositionMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=16, unique=True)),
                ('time_stamp', models.DateTimeField()),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
