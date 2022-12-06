# -*- coding: utf-8 -*-
import json
import datetime
import pytz


def listado_llamados_proyecto(llamados):
    llamados = [llamado_proyecto_serializer(llamado) for llamado in llamados]
    return json.dumps(llamados)


def llamado_proyecto_serializer(llamado):
    return {
        'LlamadoProyectoId': llamado.id,
        'Titulo': llamado.titulo,
        'Proyecto': llamado.proyecto.nombre,
        'CentroEmergencia': llamado.centro_emergencia,
        'Estado': llamado.activo,
        'FechaRegistro': str(llamado.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(llamado.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
    }
