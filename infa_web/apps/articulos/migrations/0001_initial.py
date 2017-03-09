# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-09 09:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arlo',
            fields=[
                ('carlos', models.IntegerField(primary_key=True, serialize=False)),
                ('cbarras', models.CharField(blank=True, max_length=50, null=True)),
                ('ncorto', models.CharField(max_length=50)),
                ('nlargo', models.CharField(max_length=100)),
                ('canti', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('vcosto', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('ifcostear', models.BooleanField(default=True)),
                ('ifpvfijo', models.BooleanField()),
                ('stomin', models.DecimalField(decimal_places=2, default=1, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('stomax', models.DecimalField(decimal_places=2, default=100, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('pvta1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('pvta2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('pvta3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('pvta4', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('pvta5', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('pvta6', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('vcosto1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('fcosto1', models.DateField(blank=True, null=True)),
                ('vcosto2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('fcosto2', models.DateField(blank=True, null=True)),
                ('vcosto3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('fcosto3', models.DateField(blank=True, null=True)),
                ('ifedinom', models.BooleanField(max_length=1)),
                ('refe', models.CharField(blank=True, max_length=100, null=True)),
                ('ifdesglo', models.BooleanField()),
                ('mesesgara', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('porult1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('porult2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('porult3', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('porult4', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('porult5', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('porult6', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('foto1', models.FileField(blank=True, default=b'img/articles/default.jpg', null=True, upload_to='img/articles/')),
                ('foto2', models.FileField(blank=True, default=b'img/articles/default.jpg', null=True, upload_to='img/articles/')),
                ('foto3', models.FileField(blank=True, default=b'img/articles/default.jpg', null=True, upload_to='img/articles/')),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
            options={
                'ordering': ['-nlargo'],
            },
        ),
        migrations.CreateModel(
            name='Arlosdesglo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itglo', models.CharField(max_length=4, validators=[django.core.validators.MinValueValidator(0)])),
                ('cantiglo', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('costoglo', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('vtoglo', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('carlosglo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carlosglo', to='articulos.Arlo')),
                ('carlosp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carlosp', to='articulos.Arlo')),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
        ),
        migrations.CreateModel(
            name='Gpo',
            fields=[
                ('cgpo', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('ngpo', models.CharField(max_length=80)),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
            options={
                'ordering': ['ngpo'],
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('cmarca', models.AutoField(primary_key=True, serialize=False)),
                ('nmarca', models.CharField(max_length=60)),
                ('cesdo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
            options={
                'ordering': ['nmarca'],
            },
        ),
        migrations.CreateModel(
            name='Tiarlos',
            fields=[
                ('ctiarlos', models.AutoField(primary_key=True, serialize=False)),
                ('ntiarlos', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ['ntiarlos'],
            },
        ),
        migrations.CreateModel(
            name='Unidades',
            fields=[
                ('cunidad', models.AutoField(primary_key=True, serialize=False)),
                ('nunidad', models.CharField(max_length=60)),
                ('peso', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'ordering': ['nunidad'],
            },
        ),
        migrations.AddField(
            model_name='arlo',
            name='cgpo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='articulos.Gpo'),
        ),
    ]
