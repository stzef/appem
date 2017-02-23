# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-23 08:58
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autorre',
            fields=[
                ('cautorre', models.AutoField(primary_key=True, serialize=False)),
                ('nautorre', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ['nautorre'],
            },
        ),
        migrations.CreateModel(
            name='Cobra',
            fields=[
                ('ccobra', models.AutoField(primary_key=True, serialize=False)),
                ('ncobra', models.CharField(max_length=80)),
            ],
            options={
                'ordering': ['ncobra'],
            },
        ),
        migrations.CreateModel(
            name='Coti',
            fields=[
                ('ccoti', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fcoti', models.DateTimeField()),
                ('descri', models.CharField(max_length=300)),
                ('osberini', models.CharField(max_length=250)),
                ('autoriza', models.CharField(max_length=100)),
                ('obserfin', models.CharField(max_length=250)),
                ('ffin', models.DateTimeField()),
                ('fentre', models.DateTimeField()),
                ('ifareglad', models.BooleanField()),
                ('docuref', models.CharField(max_length=10)),
                ('fhcoti', models.DateTimeField()),
                ('detaanula', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('cpersona', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('npersona', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['npersona'],
            },
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('cruta', models.AutoField(primary_key=True, serialize=False)),
                ('nruta', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['nruta'],
            },
        ),
        migrations.CreateModel(
            name='Tercero',
            fields=[
                ('citerce', models.AutoField(primary_key=True, serialize=False)),
                ('idterce', models.CharField(max_length=20)),
                ('dv', models.CharField(max_length=1)),
                ('rasocial', models.CharField(max_length=200)),
                ('nomcomer', models.CharField(max_length=200)),
                ('ape1', models.CharField(blank=True, max_length=40, null=True)),
                ('ape2', models.CharField(blank=True, max_length=40, null=True)),
                ('nom1', models.CharField(blank=True, max_length=40, null=True)),
                ('nom2', models.CharField(blank=True, max_length=40, null=True)),
                ('sigla', models.CharField(blank=True, max_length=100, null=True)),
                ('replegal', models.CharField(blank=True, max_length=100, null=True)),
                ('dirterce', models.CharField(max_length=80)),
                ('telterce', models.CharField(max_length=20)),
                ('faxterce', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=40, null=True)),
                ('contacto', models.CharField(blank=True, max_length=20, null=True)),
                ('topcxc', models.DecimalField(blank=True, decimal_places=2, default=1000000, max_digits=15, null=True)),
                ('clipre', models.IntegerField(default=1)),
                ('fnaci', models.DateField(default=django.utils.timezone.now)),
                ('ordenruta', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vende',
            fields=[
                ('cvende', models.AutoField(primary_key=True, serialize=False)),
                ('nvende', models.CharField(max_length=80)),
                ('porventa', models.DecimalField(decimal_places=4, max_digits=7, validators=[django.core.validators.MinValueValidator(0)])),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
            options={
                'ordering': ['nvende'],
            },
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('czona', models.AutoField(primary_key=True, serialize=False)),
                ('nzona', models.CharField(max_length=40)),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
            options={
                'ordering': ['nzona'],
            },
        ),
    ]
