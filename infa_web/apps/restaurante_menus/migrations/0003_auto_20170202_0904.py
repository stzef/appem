# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-02 09:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante_menus', '0002_auto_20170201_1123'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CgposMenus',
            new_name='GposMenus',
        ),
    ]