# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-06 20:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liepin', '0003_auto_20170506_2022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cata',
            old_name='datemine',
            new_name='data',
        ),
    ]
