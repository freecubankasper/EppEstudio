# -*- coding: utf-8 -*-
import json
import datetime
import pytz


def listado_abastecimientos(abastecimientos):
    abastecimientos = [abastecimiento_serializer(abastecimiento) for abastecimiento in abastecimientos]
    return json.dumps(abastecimientos)


def abastecimiento_serializer(abastecimiento):
    return {
        'AbastecimientoId': abastecimiento.id,
        'Nombre': abastecimiento.nombre,
        'SubcategoriaServicio': abastecimiento.sub_categoria.nombre,
        'NombreProducto': abastecimiento.nombre_producto,
        'Estado': abastecimiento.activo,
        'FechaRegistro': str(abastecimiento.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(abastecimiento.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
    }
