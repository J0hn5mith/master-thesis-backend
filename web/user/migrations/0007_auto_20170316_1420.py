# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20170316_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconfiguration',
            name='notify_by_amail',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userconfiguration',
            name='notify_by_sms',
            field=models.BooleanField(default=False),
        ),
    ]
