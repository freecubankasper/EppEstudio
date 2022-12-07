# -*- coding: utf-8 -*-
import json
import datetime
import pytz


def listado_numeros_prefactura(numeros_prefactura):
    numeros_prefactura = [numero_prefactura_serializer(numero_prefactura) for numero_prefactura in numeros_prefactura]
    return json.dumps(numeros_prefactura)


def numero_prefactura_serializer(numero_prefactura):
    return {
        'NumeroPrefacturaId': numero_prefactura.id,
        'NumeroPrefactura': numero_prefactura.numero_prefactura,
        'Entidad': numero_prefactura.entidad.nombre,
        'Estado': numero_prefactura.activo,
        'FechaRegistro': str(numero_prefactura.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(numero_prefactura.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
    }
