# -*- coding: utf-8 -*-
import json
import datetime
import pytz


def listado_transportes(transportes):
    transportes = [transporte_serializer(transporte) for transporte in transportes]
    return json.dumps(transportes)


def transporte_serializer(transporte):
    return {
        'TransporteId': transporte.id,
        'TipoVehiculo': transporte.tipo_vehiculo.nombre,
        'Marca': transporte.marca.nombre,
        'Modelo': transporte.modelo.nombre,
        'Color': transporte.color,
        'SubcategoriaServicio': transporte.sub_categoria.nombre,
        'Estado': transporte.activo,
        'FechaRegistro': str(transporte.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(transporte.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
    }