# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from locacion.utiles import serializer_locacion_object_list

register = template.Library()


def serializer_locaciones(object_list):
    return serializer_locacion_object_list.listado_locaciones(object_list)


register.filter('serializer_locaciones', serializer_locaciones)