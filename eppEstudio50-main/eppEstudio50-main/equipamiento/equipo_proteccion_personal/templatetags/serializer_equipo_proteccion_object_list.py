# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from equipo_proteccion_personal.utiles import serializer_equipo_proteccion_object_list

register = template.Library()


def serializer_equipos_proteccion_personal(object_list):
    return serializer_equipo_proteccion_object_list.listado_equipos_proteccion_personal(object_list)


register.filter('serializer_equipos_proteccion_personal', serializer_equipos_proteccion_personal)
