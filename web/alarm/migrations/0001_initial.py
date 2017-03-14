# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 10:27
from __future__ import unicode_literals

import datetime
import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_to_deactivate', models.DateTimeField(default=datetime.timedelta(0, 60))),
            ],
        ),
        migrations.CreateModel(
            name='AlarmConfigArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center', django.contrib.gis.db.models.fields.PointField(default=[0, 0], srid=4326)),
                ('radius', models.FloatField(default=2, validators=(django.core.validators.MinValueValidator(0),))),
            ],
        ),
        migrations.AddField(
            model_name='alarmconfig',
            name='area',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='alarm.AlarmConfigArea'),
        ),
    ]
