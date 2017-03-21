# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 16:20
from __future__ import unicode_literals

import alarm.models
from django.db import migrations, models


def set_random_tokens(apps, schema_editor):
    from alarm.models import generateRandomToken
    alarms = apps.get_model("alarm", "Alarm").objects.all()
    for a in alarms:
        a.random_token = generateRandomToken()
        a.save()


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0011_alarm_random_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='random_token',
            field=models.CharField(
                default=alarm.models.generateRandomToken,
                max_length=10,
            )
        ),
        migrations.RunPython(set_random_tokens),
        migrations.AlterField(
            model_name='alarm',
            name='random_token',
            field=models.CharField(
                default=alarm.models.generateRandomToken,
                max_length=10,
                unique=True
            ),
        ),
    ]
