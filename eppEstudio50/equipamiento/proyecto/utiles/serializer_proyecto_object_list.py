# -*- coding: utf-8 -*-
import json
import datetime
import pytz

from epp.settings import MEDIA_URL


def listado_proyectos(proyectos):
    proyectos = [proyecto_serializer(proyecto) for proyecto in proyectos]
    return json.dumps(proyectos)


def proyecto_serializer(proyecto):
    return {
        'ProyectoId': proyecto.id,
        'Nombre': proyecto.nombre,
        'Categoria': proyecto.categoria.nombre,
        'FechaInicio': str(proyecto.fecha_inicio.strftime("%Y-%m-%d")),
        'FechaFin': str(proyecto.fecha_fin.strftime("%Y-%m-%d")),
        'EstadoProyecto': proyecto.estado_proyecto,
        'Estado': proyecto.activo,
        'FechaRegistro': str(proyecto.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(proyecto.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),

    }
