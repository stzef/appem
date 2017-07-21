from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from django.contrib.staticfiles.templatetags.staticfiles import static
from infa_web.parameters import ManageParameters

import json
import datetime
from infa_web.apps.restaurante_menus.models import *
from infa_web.apps.base.forms import CommonForm
from infa_web.apps.restaurante_comandas.models import *
from infa_web.apps.restaurante_comandas.forms import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from infa_web.custom.generic_views import CustomListView, CustomCreateView, CustomUpdateView

from infa_web.apps.base.utils import get_current_user
from django.db.models import Max, Count

from django.contrib.auth.models import User
from infa_web.apps.usuarios.models import Usuario
from infa_web.apps.base.views import AjaxableResponseMixin
from django.core.urlresolvers import reverse_lazy

# pedido actual
# pedido anterior -> listar las comandas

def GetInfoMesa(mesa,request_db):
	query = Coda.objects.using(request_db).filter(cresupedi__isnull=True,cmesa=mesa,cesdo__cesdo=1)
	vttotal = float(0)
	mesero = None
	comandas = []
	if query.exists():
		comandas = query
		totales = sum( [ comanda.vttotal for comanda in comandas] )
		vttotal = totales
		mesero = comandas[0].cmero
	return {"vttotal":vttotal,"mesero":mesero,"comandas":comandas}

def generar_ccoda(talocoda,request_db):
	maxCcoda = Coda.objects.using(request_db).filter(ctalocoda=talocoda).aggregate(Max('ccoda'))
	if maxCcoda["ccoda__max"]:
		ccoda = maxCcoda["ccoda__max"] + 1
	else:
		ccoda = 1
	return ccoda

def create_Coda(data,name_db):
	if not isinstance(data,list):
		data = [data]

	list_coda = []
	coda = None
	for item in data:
		coda = Coda(**item["coda"])
		coda.save(using=name_db)
		for deta in item["deta"]:
			deta["ccoda"] = coda
			codadeta = Codadeta(**deta)
			codadeta.save(using=name_db)
		list_coda.append(coda)
	return list_coda

# States #
class TableCreate(AjaxableResponseMixin,CustomCreateView):
	model = Mesas
	template_name = "mesas/table.html"
	form_class = TableForm
	success_url=reverse_lazy("add-table")

	def get_context_data(self, **kwargs):
		context = super(TableCreate, self).get_context_data(**kwargs)

		context_request = RequestContext(self.request)
		#context['context_request'] = context_request
		self.context_instance = RequestContext(self.request)


		context['title'] = 'Crear Mesa'
		context['mode_view'] = 'create'
		context['url'] = reverse_lazy('add-table')
		return context

class TableUpdate(AjaxableResponseMixin,CustomUpdateView):
	model = Mesas
	template_name = "mesas/table.html"
	form_class = TableForm
	success_url=reverse_lazy("add-table")

	def get_context_data(self, **kwargs):
		context = super(TableUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Editar Mesa'
		context['mode_view'] = 'edit'
		context['url'] = reverse_lazy('edit-table',kwargs={'pk': self.kwargs["pk"]},)
		context['current_pk'] = self.kwargs["pk"]
		return context

class TablesList(CustomListView):
	model = Mesas
	template_name = "mesas/list-tables.html"
# States #

class OrdersList(CustomListView):
	model = Coda
	template_name = "ordenes/list-orders.html"

	def get_queryset(self):
		queryset = Coda.objects.using(self.request.db).filter()
		cmesa = self.request.GET.get('cmesa',None)
		if cmesa :
			queryset = Coda.objects.using(self.request.db).filter(cmesa__cmesa=cmesa)
		return queryset

def GetCommandsOrder(request, cmesa):
	comandas = Coda.objects.using(request.db).filter(cmesa=cmesa,cesdo__cesdo=1)

	return comandas

@csrf_exempt
def SaveSummary(request):
	data = json.loads(request.body)

	mesa = Mesas.objects.using(request.db).get(cmesa= data["cmesa"])

	comandas = Coda.objects.using(request.db).filter(cmesa=mesa,cresupedi__isnull=True,cesdo__cesdo=1)
	totales = sum( [ comanda.vttotal for comanda in comandas] )
	try:
		cresupedi = Resupedi.objects.latest('cresupedi').cresupedi + 1
	except Exception as e:
		cresupedi = 1
	today = datetime.date.today().strftime("%Y-%m-%d")
	resupedi = Resupedi(
		cresupedi=cresupedi,
		fresupedi = today, #"2017-01-01",
		vttotal = totales,
		detaanula = "",
		ifcortesia = False,
	)
	resupedi.save(using=request.db)
	medio_pago_it = 1
	for medio_pago in data["medios_pago"]:
		resupedipago = Resupedipago(
			cresupedi = resupedi,
			banmpago = Banfopa.objects.using(request.db).get(cbanfopa=int(medio_pago["banmpago"])),
			cmpago = MediosPago.objects.using(request.db).get(cmpago=int(medio_pago["cmpago"])),
			docmpago = medio_pago["docmpago"],
			it = int(medio_pago_it),
			vmpago = float(medio_pago["vmpago"])
		)
		medio_pago_it += 1
		resupedipago.save(using=request.db)
		print "...................................."
		print resupedipago
		print "...................................."

	for comanda in comandas:
		comanda.cresupedi = resupedi
		comanda.save(using=request.db)

	resupedi = serializers.serialize("json", [resupedi],fields=('cresupedi','vttotal','detaanula','ifcortesia'),use_natural_foreign_keys=True)
	resupedi = json.loads(resupedi)[0]

	response = {
		"resupedi" : resupedi
	}
	return HttpResponse(json.dumps(response), "application/json")

@csrf_exempt
def SaveCommand(request):
	data = json.loads(request.body)

	mesero = get_current_user(request.db,request.user,mesero=True)

	talocoda = mesero.ctalocoda
	ccoda = generar_ccoda(talocoda,request.db)
	mesa = Mesas.objects.using(request.db).get(cmesa= data["cmesa"])

	dataCoda = {
		'ccoda' : ccoda,
		'ctalocoda' : talocoda,
		'cmesa' : mesa,
		#'cesdo' : CESTADO_ACTIVO,
		'cmero' : mesero,
		#'cresupedi' : models.ForeignKey(Resupedi),
		'detaanula' : "",
		'vttotal' : 0,
		'fcoda' : "2017-02-02",
	}

	dataCodadeta = []
	it = 0
	for codadeta in data["deta"]:

		cmenu = codadeta[data["cols"]["cmenu"]["i"]]
		menu = Menus.objects.using(request.db).get(cmenu= cmenu)

		canti = float(codadeta[data["cols"]["canti"]["i"]])
		vunita = float(codadeta[data["cols"]["vunita"]["i"]])


		item = {
			'it' : it,
			'cmenu' : menu,
			'nlargo' : "",
			'canti' : canti,
			'vunita' : vunita,
			'vtotal' : canti * vunita,
		}
		dataCoda["vttotal"] += item["vtotal"]
		dataCodadeta.append(item)
		it += 1

	coda = create_Coda({"coda":dataCoda,"deta":dataCodadeta},request.db)
	coda = serializers.serialize("json", coda,use_natural_foreign_keys=True)
	coda = json.loads(coda)[0]


	return HttpResponse(json.dumps(coda), "application/json")

def ViewAnnulmentCommand(request):
	form = CommonForm(request.db)

	context = {"form":form}
	return render(request, "ordenes/procesos/annulment-commad.html", context)

@csrf_exempt
def AnnulmentItemCommand(request):
	data = json.loads(request.body)

	responses = []
	for data in data["codadeta"]:
		menu = Menus.objects.using(request.db).get(cmenu = data["cmenu"])
		coda = Coda.objects.using(request.db).get(ccoda = data["ccoda"])
		codadeta = Codadeta.objects.using(request.db).get(cmenu= menu,ccoda= coda)

		response = {}
		if coda.cresupedi is None:
			response["message"] = "El Item se eliminio Correctamente %s" % coda.ccoda
			response["status"] = "success"
			coda.vttotal -= codadeta.vtotal
			codadeta.delete()

			coda.save(using=request.db)

			coda_json = serializers.serialize("json", [coda],use_natural_foreign_keys=True)
			coda_json = json.loads(coda_json)[0]

			response["json"] = coda_json
			responses.append(response)

		else:
			response["message"] = "El Item  No se puede Anular ( Esta Registrada en un Resumen de Pedido )"
			response["status"] = "danger"
			responses.append(response)




	print responses

	return HttpResponse(json.dumps(responses), "application/json")

@csrf_exempt
def AnnulmentCommand(request):

	mesas = request.POST.get("mesas", "")
	ccoda = request.POST.get("ccoda", "")
	detaanula = request.POST.get("detaanula", "")
	cesdo = request.POST.get("cesdo", "")

	coda = Coda.objects.using(request.db).get(ccoda = ccoda)
	response = {}
	if coda.cresupedi is None:
		response["message"] = "Se realizo el cambio de estado de la comanda %s" % coda.ccoda
		response["status"] = "success"

		coda.detaanula = detaanula
		coda.cesdo = Esdo.objects.using(request.db).get(cesdo = cesdo)

		coda.save(using=request.db)
	else:
		response["message"] = "La Comanda No se puede Anular ( Esta Registrada en un Resumen de Pedido )"
		response["status"] = "danger"

	return HttpResponse(json.dumps(response), "application/json")

@csrf_exempt
def InfoSummaryUpdate(request,pk):
	mesa = Mesas.objects.using(request.db).get(cmesa=pk)
	info_mesa = GetInfoMesa(mesa,request.db)

	mesa = json.loads(serializers.serialize("json", [mesa],use_natural_foreign_keys=True))[0]
	comandas = json.loads(serializers.serialize("json", info_mesa["comandas"],use_natural_foreign_keys=True))
	mesero = json.loads(serializers.serialize("json", [info_mesa["mesero"]],use_natural_foreign_keys=True))[0]

	mesa["comandas"] = comandas
	mesa["vttotal"] = str(info_mesa["vttotal"])
	mesa["mesero"] = mesero

	return HttpResponse(json.dumps(mesa), "application/json")

@csrf_exempt
def GetResupediMesa(request,cmesa):
	# data = json.loads(request.body)
	mesa = Mesas.objects.using(request.db).get(cmesa = cmesa)

	# comandas = Coda.objects.using(request.db).all().annotate(Count("cresupedi"))
	comandas = Coda.objects.using(request.db).filter(cmesa=mesa,cresupedi__isnull=False).annotate(Count("cresupedi"))
	comandas = map( lambda c: c.cresupedi, comandas )
	print comandas
	comandas_json = json.loads(serializers.serialize("json", comandas,use_natural_foreign_keys=True))



	response = comandas_json

	return HttpResponse(json.dumps(response), "application/json")

def OrdersJoin(request):
	data = json.loads(request.body)
	cmesa = data["mesa"]
	mesa = Mesas.objects.using(request.db).get(cmesa=cmesa)

	cmesas = data["mesas"]
	mesas = Mesas.objects.using(request.db).filter(cmesa__in=cmesas)
	comandas = Coda.objects.using(request.db).filter(cresupedi__isnull=True,cmesa__in=mesas,cesdo__cesdo=1)

	for comanda in comandas:
		comanda.cmesa = mesa
		comanda.save(using=request.db)

	from django.template import loader, Context

	mesas = Mesas.objects.using(request.db).all()

	for mesa in mesas:
		info_mesa = GetInfoMesa(mesa,request.db)
		mesa.comandas = info_mesa["comandas"]
		mesa.vttotal = info_mesa["vttotal"]
		mesa.mesero = info_mesa["mesero"]

	t = loader.get_template('ordenes/partials/summary-mesas.html')
	c = Context({ 'mesas': mesas })
	rendered = t.render(c)

	response = {"html":rendered}
	return HttpResponse(json.dumps(response), "application/json")

def TakeOrder(request):

	mesero = get_current_user(request.db,request.user,mesero=True)
	print "_-________________"
	print mesero

	gruposMenu = GposMenus.objects.using(request.db).all().order_by("orden")
	for grupoMenu in gruposMenu:
		grupoMenu.menus = Menus.objects.using(request.db).filter(cgpomenu=grupoMenu)

	mesas = Mesas.objects.using(request.db).all()
	today = datetime.date.today()
	mesas_activas = Mesas.objects.using(request.db).filter(
		cmesa__in=Coda.objects.using(request.db).filter(
			cmero=mesero,
			cesdo__cesdo=1,
			fcoda__date=str(today)
		).values('cmesa')
	)

	print mesas_activas
	print "_-________________"

	context = {
		'gruposMenu' : gruposMenu,
		'mesas' : mesas,
		'mesas_activas' : mesas_activas,
		'mesero' : mesero
	}
	return render(request, "ordenes/take-order.html", context)

def OrderSummary(request):
	mesas = Mesas.objects.using(request.db).all()


	for mesa in mesas:
		info_mesa = GetInfoMesa(mesa,request.db)
		mesa.vttotal = info_mesa["vttotal"]
		mesa.mesero = info_mesa["mesero"]
		mesa.comandas = info_mesa["comandas"]

		#query = Coda.objects.using(request.db).filter(cresupedi__isnull=True,cmesa=mesa,cesdo__cesdo=1)
		#if query.exists():
		#	mesa.comandas = query
		#	totales = sum( [ comanda.vttotal for comanda in mesa.comandas] )
		#	mesa.vttotal = totales
		#	mesa.mesero = mesa.comandas[0].cmero

	if request.is_ajax():
		pass
	else:
		context = {
			'mesas' : mesas,
			'form_medios_pagos' : ResupedipagoForm(request.db)
		}
		return render(request, "ordenes/summary.html", context)

"""
class OrderPrint(PDFTemplateView):
	template_name = "ordenes/print/format_half_letter.html"

	def get_context_data(self, **kwargs):
		context = super(OrderPrint, self).get_context_data(**kwargs)
		manageParameters = ManageParameters(self.request.db)
		data = self.request.GET

		formato = data.get('formato')
		cresupedi = data.get('cresupedi')

		resupedi = Resupedi.objects.using(self.request.db).filter(cresupedi=cresupedi)
		comandas = Coda.objects.using(self.request.db).filter(cresupedi=resupedi,cesdo__cesdo=1)
		for comanda in comandas:
			comandas.deta = Codadeta.objects.using(self.request.db).filter(ccoda=comanda)
		print comandas

		if formato or formato == "half_letter":
			self.template_name = "ordenes/print/format_half_letter.html"
			#context['orientation'] = 'portrait'
			context['orientation'] = 'landscape'

		elif formato == "neckband":
			self.template_name = "ordenes/print/format_half_letter.html"
			#context['orientation'] = 'portrait'
			context['orientation'] = 'landscape'
		else:
			self.template_name = "ordenes/print/format_half_letter.html"
			#context['orientation'] = 'portrait'
			context['orientation'] = 'landscape'

		data.company_logo = static(manageParameters.get_param_value('company_logo'))

		context['data'] = data
		context['title'] = 'Impresion de Resumen de Pedido'
		context['comandas'] = comandas

		return context

"""

import reportlab
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape, portrait
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from django.utils import timezone

def OrderPrint(request):

	text_footer_stzef = "AppEm - Software para administracion de Empresas sitematizaref@gmail.com"

	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'inline; attachment; filename="somefilename.pdf"'

	manageParameters = ManageParameters(request.db)
	data = request.GET

	formato = data.get('formato')
	cresupedi = data.get('cresupedi')

	resupedi = Resupedi.objects.using(request.db).get(cresupedi=cresupedi)
	comandas = Coda.objects.using(request.db).filter(cresupedi=resupedi,cesdo__cesdo=1)

	doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=10,leftMargin=10, topMargin=0,bottomMargin=40)
	doc.pagesize = portrait((190, 1900))

	hr_linea = "___________________________________"

	elements = []

	data_header = [
		[manageParameters.get("company_name")],
		[manageParameters.get("text_header_pos_bill")],
		[manageParameters.get("company_id_name") + " : " + manageParameters.get("company_id")],
		# ["I.V.I Serie 5205964"],
		# [sucursal.nsucur],
		# ["Dir:" + sucursal.dirsucur],
		# ["Tel:" + sucursal.telsucur],
		# ["Cel:" + sucursal.celsucur],
	]

	data = [
		["===============", "=========", "============"],
		["Descripcion", "Cant", "Vr. Tot"],
		["_______________", "_________", "____________"],
	]

	for comanda in comandas:
		detalles = Codadeta.objects.using(request.db).filter(ccoda=comanda)
		for detalle in detalles:
			data.append([detalle.cmenu.nmenu[:10],str(detalle.canti),str(detalle.vtotal)])

	data.append(["_______________", "_________", "____________"])
	data.append(["Total","-->",str(resupedi.vttotal)])
	data.append(["===============", "=========", "============"])

	style_table_header = TableStyle([
		('ALIGN',(1,1),(-2,-2),'RIGHT'),
		('TEXTCOLOR',(1,1),(-2,-2),colors.red),
		('VALIGN',(0,0),(0,-1),'TOP'),
		('TEXTCOLOR',(0,0),(0,-1),colors.blue),
		('ALIGN',(0,-1),(-1,-1),'CENTER'),
		('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
		('TEXTCOLOR',(0,-1),(-1,-1),colors.green),

		('LEFTPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),

		('BOX', (0,0), (-1,-1), 0.25, colors.black),
	])

	style_table_facdeta = TableStyle([
		('ALIGN',(1,1),(-2,-2),'RIGHT'),
		('TEXTCOLOR',(1,1),(-2,-2),colors.red),
		('VALIGN',(0,0),(0,-1),'TOP'),
		('TEXTCOLOR',(0,0),(0,-1),colors.blue),
		('ALIGN',(0,-1),(-1,-1),'CENTER'),
		('VALIGN',(0,-1),(-1,-1),'MIDDLE'),

		('LEFTPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),

		('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
	])

	#Configure style and word wrap
	s = getSampleStyleSheet()

	s.add(ParagraphStyle(name='tirilla',fontSize=8,leading=12,rightMargin=0,leftMargin=0, topMargin=0,bottomMargin=0))
	s.add(ParagraphStyle(name='header',fontSize=8,leading=12,alignment=TA_CENTER))

	bodytext = s["tirilla"]
	headertext = s["header"]
	#s.wordWrap = 'CJK'
	bodytext.wordWrap = 'LTR'
	data2 = [[Paragraph(cell, bodytext) for cell in row] for row in data]
	t=Table(data2)
	t.setStyle(style_table_facdeta)

	data2_header = [[Paragraph(cell, headertext) for cell in row] for row in data_header]
	t_header=Table(data2_header)
	t_header.setStyle(style_table_header)

	elements.append(t_header)
	elements.append(Paragraph("<br/>Resumen de Pedido No. %s" % resupedi.cresupedi,s['tirilla']))

	elements.append(Paragraph("Fecha : %s " % timezone.localtime(resupedi.fresupedi),s['tirilla']))
	# elements.append(Paragraph("Atendido por : %s <br/>" % factura.cvende.nvende,s['tirilla']))
	elements.append(t)
	elements.append(Paragraph(manageParameters.get("text_footer_pos_bill") ,s['tirilla']))
	elements.append(Paragraph(hr_linea ,s['tirilla']))
	elements.append(Paragraph(text_footer_stzef ,s['tirilla']))
	elements.append(Paragraph(hr_linea ,s['tirilla']))
	elements.append(Paragraph("." ,s['tirilla']))
	doc.build(elements)

	return response
