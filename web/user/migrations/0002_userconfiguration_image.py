# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconfiguration',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Portrait'),
        ),
    ]