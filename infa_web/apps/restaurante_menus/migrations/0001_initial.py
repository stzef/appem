# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-08 10:09
from __future__ import unicode_literals

import django.core.validators
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
            name='GposMenus',
            fields=[
                ('cgpomenu', models.IntegerField(primary_key=True, serialize=False)),
                ('ngpomenu', models.CharField(max_length=50)),
                ('orden', models.IntegerField(default=0)),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
            options={
                'ordering': ['ngpomenu'],
            },
        ),
        migrations.CreateModel(
            name='Ingredientes',
            fields=[
                ('cingre', models.IntegerField(primary_key=True, serialize=False)),
                ('ningre', models.CharField(max_length=50)),
                ('canti', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('vcosto', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('ifcostear', models.BooleanField(default=True)),
                ('stomin', models.DecimalField(decimal_places=2, default=1, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('stomax', models.DecimalField(decimal_places=2, default=100, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('ifedinom', models.BooleanField(max_length=1)),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
                ('civa', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Iva')),
                ('cunidad', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='articulos.Unidades')),
            ],
            options={
                'ordering': ['-ningre'],
            },
        ),
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('cmenu', models.IntegerField(primary_key=True, serialize=False)),
                ('nmenu', models.CharField(max_length=50)),
                ('fcrea', models.DateTimeField(auto_now_add=True)),
                ('npax', models.IntegerField(default=1)),
                ('pvta1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('pvta2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('pvta3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('vttotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('foto', models.FileField(blank=True, default=b'img/menus/default.jpg', null=True, upload_to='img/menus/')),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
                ('cgpomenu', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurante_menus.GposMenus')),
            ],
        ),
        migrations.CreateModel(
            name='Menusdeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('it', models.CharField(max_length=50)),
                ('nplato', models.CharField(max_length=50)),
                ('canti', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('vunita', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('vtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('cmenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurante_menus.Menus')),
            ],
        ),
        migrations.CreateModel(
            name='Platos',
            fields=[
                ('cplato', models.IntegerField(primary_key=True, serialize=False)),
                ('nplato', models.CharField(max_length=50)),
                ('fcrea', models.DateTimeField(auto_now_add=True)),
                ('npax', models.IntegerField(default=1)),
                ('vttotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('foto', models.FileField(blank=True, default=b'img/dishes/default.jpg', null=True, upload_to='img/dishes/')),
            ],
        ),
        migrations.CreateModel(
            name='Platosdeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('it', models.CharField(max_length=50)),
                ('canti', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('vunita', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('vtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('cingre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurante_menus.Ingredientes')),
                ('cplato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurante_menus.Platos')),
                ('cunidad', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='articulos.Unidades')),
            ],
        ),
        migrations.AddField(
            model_name='menusdeta',
            name='cplato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurante_menus.Platos'),
        ),
    ]
