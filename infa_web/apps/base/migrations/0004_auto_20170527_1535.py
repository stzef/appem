# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-27 20:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20170526_1427'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='esdo',
            options={'ordering': ['nesdo'], 'permissions': (('list_esdo', 'Puede Listar Estados'), ('list_parameters', 'Puede Listar Parametros'), ('save_parameters', 'Puede Crear Parametros'))},
        ),
    ]