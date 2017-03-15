# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alarm', '0007_auto_20170315_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='tag',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='alarm', to='tags.Tag'),
        ),
    ]
