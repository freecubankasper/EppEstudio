# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from equipo_proteccion_personal.utiles import serializer_factura_object_list

register = template.Library()


def serializer_facturas(object_list):
    return serializer_factura_object_list.listado_facturas(object_list)


register.filter('serializer_facturas', serializer_facturas)