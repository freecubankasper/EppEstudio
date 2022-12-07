# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from equipamiento.utiles import serializer_equipamiento_object_list

register = template.Library()


def serializer_equipamientos(object_list):
    return serializer_equipamiento_object_list.listado_equipamientos(object_list)


register.filter('serializer_equipamientos', serializer_equipamientos)