# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-08 10:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articulos', '0001_initial'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invinicab',
            fields=[
                ('cii', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('fii', models.DateTimeField()),
                ('fuaii', models.DateTimeField(blank=True, null=True)),
                ('vttotal', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
        ),
        migrations.CreateModel(
            name='Invinideta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nlargo', models.CharField(max_length=100)),
                ('canti', models.DecimalField(decimal_places=2, max_digits=15)),
                ('vunita', models.DecimalField(decimal_places=2, max_digits=15)),
                ('vtotal', models.DecimalField(decimal_places=2, max_digits=15)),
                ('cancalcu', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ajuent', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ajusal', models.DecimalField(decimal_places=2, max_digits=15)),
                ('carlos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulos.Arlo')),
                ('cii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarios.Invinicab')),
            ],
        ),
    ]
