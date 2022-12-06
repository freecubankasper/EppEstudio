# -*- coding: utf-8 -*-
import json
import datetime
import pytz


def listado_facturas(facturas):
    facturas = [factura_serializer(factura) for factura in facturas]
    return json.dumps(facturas)


def factura_serializer(factura):
    return {
        'FacturaId': factura.id,
        'NumeroPrefactura': factura.numero_prefactura.numero_prefactura,
        'Entidad': factura.numero_prefactura.entidad.nombre,
        'EstadoPago': "Si" if factura.estado_pago else "No",
        'Estado': factura.activo,
        'FechaPago': str(factura.fecha_pago.strftime("%Y-%m-%d") if factura.fecha_pago else '-'),
        'FechaRegistro': str(factura.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
    }
