# -*- coding: utf-8 -*-
import json
import datetime
import pytz


def listado_locaciones(locaciones):
    locaciones = [locacion_serializer(locacion) for locacion in locaciones]
    return json.dumps(locaciones)


def locacion_serializer(locacion):
    return {
        'LocacionId': locacion.id,
        'Nombre': locacion.nombre,
        'SubcategoriaServicio': locacion.sub_categoria.nombre,
        'Municipio': locacion.municipio.nombre,
        'Estado': locacion.activo,
        'FechaRegistro': str(locacion.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(locacion.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
    }
