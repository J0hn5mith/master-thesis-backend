# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 10:08
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0008_auto_20170310_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=colorful.fields.RGBColorField(default='#c38398'),
        ),
    ]
