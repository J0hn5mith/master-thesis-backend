# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 11:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarmconfig',
            name='area',
        ),
        migrations.RemoveField(
            model_name='alarmconfig',
            name='time_to_deactivate',
        ),
        migrations.RemoveField(
            model_name='alarmconfigarea',
            name='center',
        ),
        migrations.RemoveField(
            model_name='alarmconfigarea',
            name='radius',
        ),
    ]