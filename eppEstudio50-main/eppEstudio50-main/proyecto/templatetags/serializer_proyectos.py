# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from equipo_proteccion_personal.utiles import serializer_equipo_proteccion_object_list
import json
import datetime
import pytz

register = template.Library()


def serializer_proyectos(object_list):
    return listado_proyectos(object_list)


register.filter('serializer_proyectos', serializer_proyectos)

def listado_proyectos(proyectos):
    proyectos = [proyecto_serializer(proyecto) for proyecto in proyectos]
    return json.dumps(proyectos)


def proyecto_serializer(proyecto):
    return {
        'ProyectoId': proyecto.id,
        'Nombre': proyecto.nombre,
        'Categoria': proyecto.categoria.nombre,

    }