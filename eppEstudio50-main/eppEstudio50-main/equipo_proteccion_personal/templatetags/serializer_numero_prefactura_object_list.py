# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from equipo_proteccion_personal.utiles import serializer_numero_prefactura_object_list

register = template.Library()


def serializer_numeros_prefactura(object_list):
    return serializer_numero_prefactura_object_list.listado_numeros_prefactura(object_list)


register.filter('serializer_numeros_prefactura', serializer_numeros_prefactura)