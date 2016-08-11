from __future__ import unicode_literals
from infa_web.apps.articulos.models import *
from infa_web.apps.terceros.models import *
from infa_web.apps.base.models import *
from django.db import models
from infa_web.apps.base.constantes import *

class Timo(models.Model):
	ctimo = models.IntegerField(primary_key=True)
	ntimo = models.CharField(max_length=40)
	prefijo = models.CharField(max_length=4)
	filas = models.IntegerField()
	nrepo = models.CharField(max_length=20)

	def __str__(self):
		return self.ntimo

class Mven(models.Model):
	cmven = models.AutoField(primary_key=True)
	fmven = models.DateTimeField()
	docrefe = models.CharField(max_length=10)
	citerce = models.ForeignKey(Tercero)
	ctimo = models.ForeignKey(Timo)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	vttotal = models.DecimalField(max_digits=15, decimal_places=2)
	descri = models.CharField(max_length=250)
	detaanula = models.CharField(max_length=250)
	cbode0 = models.ForeignKey(Bode, related_name='cbode0',default=DEFAULT_BODEGA)
	cbode1 = models.ForeignKey(Bode, related_name='cbode1',default=DEFAULT_BODEGA)

	def __str__(self):
		return str(self.cmven)

class Mvendeta(models.Model):
	cmven = models.ForeignKey(Mven)
	it = models.CharField(max_length=4)
	carlos = models.ForeignKey(Arlo)
	nlargo = models.CharField(max_length=100)
	canti = models.DecimalField(max_digits=15, decimal_places=2)
	vunita = models.DecimalField(max_digits=15, decimal_places=2)
	vtotal = models.DecimalField(max_digits=15, decimal_places=2)

class Mvsa(models.Model):
	cmvsa = models.AutoField(primary_key=True)
	fmvsa = models.DateTimeField()
	docrefe = models.CharField(max_length=10)
	citerce = models.ForeignKey(Tercero)
	ctimo = models.ForeignKey(Timo)
	cesdo = models.ForeignKey(Esdo,default=CESTADO_ACTIVO)
	vttotal = models.DecimalField(max_digits=15, decimal_places=2)
	descri = models.CharField(max_length=250)
	detaanula = models.CharField(max_length=250)
	cbode0 = models.ForeignKey(Bode, related_name = 'cbode_0',default=DEFAULT_BODEGA)
	cbode1 = models.ForeignKey(Bode, related_name = 'cbode_1',default=DEFAULT_BODEGA)

class Mvsadeta(models.Model):
	cmvsa = models.ForeignKey(Mvsa)
	it = models.CharField(max_length=4)
	citerce = models.ForeignKey(Tercero)
	nlargo = models.CharField(max_length=100)
	canti = models.DecimalField(max_digits=15, decimal_places=2)
	vunita = models.DecimalField(max_digits=15, decimal_places=2)
	vtotal = models.DecimalField(max_digits=15, decimal_places=2)
