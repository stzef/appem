# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-29 09:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0002_remove_movi_civa'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='movideta',
            unique_together=set([]),
        ),
    ]
