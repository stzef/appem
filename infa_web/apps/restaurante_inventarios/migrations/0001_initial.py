# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-02 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invinicabingre',
            fields=[
                ('cii', models.CharField(max_length=8, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Invinidetaingre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurante_inventarios.Invinicabingre')),
            ],
        ),
    ]