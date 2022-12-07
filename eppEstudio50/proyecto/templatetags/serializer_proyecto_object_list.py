# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from proyecto.utiles import serializer_proyecto_object_list

register = template.Library()


def serializer_proyectos(object_list):
    return serializer_proyecto_object_list.listado_proyectos(object_list)


register.filter('serializer_proyectos', serializer_proyectos)

