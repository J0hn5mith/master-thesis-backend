# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 11:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0020_auto_20170501_1334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sharedtag',
            options={'permissions': (('view_shared_tag', 'View shared tag'), ('change_shared_tag', 'Change shared tag'))},
        ),
    ]
