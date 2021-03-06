import os

DEFAULT_TERCERO = 1
DEFAULT_DOMICILIARIO = 1
DEFAULT_EMPACADOR = 1
DEFAULT_BANCO = 1000
DEFAULT_CAJA = 1
DEFAULT_SUCURSAL = 1

CESDO_ACTIVO = 1
CESDO_ANULADO = 2

DEFAULT_TALONARIO=01

DEFAULT_FORMA_PAGO = 1001
FORMA_PAGO_CONTADO = 1001
FORMA_PAGO_CREDITO = 2001

MEDIO_PAGO_EFECTIVO = 1000
MEDIO_PAGO_EFECTIVO = 1000

DEFAULT_MEDIO_PAGO = 1001
MEDIOS_PAGO_CONTADO = [1000]
MEDIOS_PAGO_CREDITO = [1001,1002,1003]

DEFAULT_MARCA = 1
DEFAULT_BODEGA = 1
DEFAULT_UBICACION = 1
DEFAULT_GRUPO = 1
DEFAULT_ZONA = 1
DEFAULT_RUTA = 1
DEFAULT_UNIDAD = 1
DEFAULT_PERSONA = "PN"
DEFAULT_LISTA_PRECIOS = 1
DEFAULT_AUTORRETENEDOR = 1
DEFAULT_IVA = 1
DEFAULT_REGIMEN_IVA = 1
DEFAULT_VENDE = 1
DEFAULT_TIIDE = 1
DEFAULT_CIUDAD = 1
DEFAULT_ACTIVO = 1
DEFAULT_CTIARLO = 1

PREFIJO_MOVIMIENTOS_ENTRADA = 10
PREFIJO_MOVIMIENTOS_SALIDA = 20

PREFIJO_MOVIMIENTOS_RC = 30
PREFIJO_MOVIMIENTOS_CXC = 40
PREFIJO_MOVIMIENTOS_AB = 40

CESTADO_ACTIVO = 1
CESTADO_INACTIVO = 2

CTIARLO_ARTICULO = 1
CTIARLO_SERVICIO = 2
CTIARLO_OTRO = 3

DEFAULT_IMAGE_ARTICLE="img/articles/default.jpg"
DEFAULT_IMAGE_INGREDIENTS="img/ingredients/default.jpg"
DEFAULT_IMAGE_DISHES="img/dishes/default.jpg"
DEFAULT_IMAGE_WAITERS="img/waiters/default.jpg"
DEFAULT_IMAGE_MENUS ="img/menus/default.jpg"

if 'APPEMPRESARIAL_USER' in os.environ:
	APPEMPRESARIAL_USER = os.environ["APPEMPRESARIAL_USER"]
	APPEMPRESARIAL_EMAIL = os.environ["APPEMPRESARIAL_EMAIL"]
	APPEMPRESARIAL_PASS = os.environ["APPEMPRESARIAL_PASS"]


EMPRESA = {
	'MIN_CARLOS' : 1000
}
