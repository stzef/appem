# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-09 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0003_auto_20160809_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autorre',
            fields=[
                ('cautorre', models.AutoField(primary_key=True, serialize=False)),
                ('nautorre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('cruta', models.AutoField(primary_key=True, serialize=False)),
                ('nruta', models.CharField(max_length=45)),
                ('cesdo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
        ),
        migrations.CreateModel(
            name='Tercero',
            fields=[
                ('citerce', models.AutoField(primary_key=True, serialize=False)),
                ('idterce', models.CharField(max_length=20)),
                ('dv', models.CharField(max_length=1)),
                ('rasocial', models.CharField(max_length=200)),
                ('nomcomer', models.CharField(max_length=200)),
                ('ape1', models.CharField(max_length=40)),
                ('ape2', models.CharField(max_length=40)),
                ('nom1', models.CharField(max_length=40)),
                ('nom2', models.CharField(max_length=40)),
                ('sigla', models.CharField(max_length=100)),
                ('nomegre', models.CharField(max_length=100)),
                ('replegal', models.CharField(max_length=100)),
                ('dirterce', models.CharField(max_length=80)),
                ('telterce', models.CharField(max_length=20)),
                ('faxterce', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('contacto', models.CharField(max_length=20)),
                ('topcxc', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ndiacxc', models.IntegerField()),
                ('clipre', models.IntegerField()),
                ('fnaci', models.DateField()),
                ('naju', models.IntegerField()),
                ('ordenruta', models.IntegerField()),
                ('cautorre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terceros.Autorre')),
                ('cciu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Ciudad')),
                ('cesdo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
                ('cregiva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Regiva')),
                ('cruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terceros.Ruta')),
                ('ctiide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Tiide')),
            ],
        ),
        migrations.CreateModel(
            name='Vende',
            fields=[
                ('cvende', models.AutoField(primary_key=True, serialize=False)),
                ('nvende', models.CharField(max_length=80)),
                ('porventa', models.DecimalField(decimal_places=4, max_digits=7)),
                ('cesdo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Esdo')),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('czona', models.AutoField(primary_key=True, serialize=False)),
                ('nzona', models.CharField(max_length=40)),
                ('activo', models.CharField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='tercero',
            name='cvende',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terceros.Vende'),
        ),
        migrations.AddField(
            model_name='tercero',
            name='czona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terceros.Zona'),
        ),
    ]
