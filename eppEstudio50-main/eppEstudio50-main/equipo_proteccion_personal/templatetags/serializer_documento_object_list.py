# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from equipo_proteccion_personal.utiles import serializer_documento_object_list

register = template.Library()


def serializer_documentos(object_list):
    return serializer_documento_object_list.listado_documentos(object_list)


register.filter('serializer_documentos', serializer_documentos)