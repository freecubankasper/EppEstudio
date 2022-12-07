# -*- coding: utf-8 -*-
import json
import datetime
import pytz


def listado_equipamientos(equipamientos):
    equipamientos = [equipamiento_serializer(equipamiento) for equipamiento in equipamientos]
    return json.dumps(equipamientos)


def equipamiento_serializer(equipamiento):
    return {
        'EquipamientoId': equipamiento.id,
        'Nombre': equipamiento.nombre,
        'SubcategoriaServicio': equipamiento.sub_categoria.nombre,
        'Marca': equipamiento.marca.nombre,
        'Estado': equipamiento.activo,
        'FechaRegistro': str(equipamiento.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(equipamiento.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
    }
