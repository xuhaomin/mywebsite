# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-12 15:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilibili', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Achive',
            new_name='Archive',
        ),
    ]