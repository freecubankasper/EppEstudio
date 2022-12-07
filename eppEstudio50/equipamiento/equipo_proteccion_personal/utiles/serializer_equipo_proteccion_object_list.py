# -*- coding: utf-8 -*-
import json
import datetime
import pytz


def listado_equipos_proteccion_personal(equipos_proteccion_personal):
    equipos_proteccion_personal = [equipo_proteccion_serializer(equipo_proteccion) for equipo_proteccion in equipos_proteccion_personal]
    return json.dumps(equipos_proteccion_personal)


def equipo_proteccion_serializer(equipo_proteccion):
    return {
        'EquipoProteccionPersonalId': equipo_proteccion.id,
        'Nombre': equipo_proteccion.nombre,
        'Categoria': equipo_proteccion.categoria.nombre,
        'Factura': equipo_proteccion.factura.numero_prefactura.numero_prefactura if equipo_proteccion.factura else 'No facturado',
        'Renovado': "Si" if equipo_proteccion.renovado else "No",
        'Entidad': equipo_proteccion.numero_prefactura.entidad.nombre,
        'Estado': equipo_proteccion.activo,
        'FechaRegistro': str(equipo_proteccion.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
    }
