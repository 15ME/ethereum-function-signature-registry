# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-04 19:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0005_bytessignature_bytes4_signature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bytessignature',
            name='unicode_bytes4_signature',
        ),
    ]
