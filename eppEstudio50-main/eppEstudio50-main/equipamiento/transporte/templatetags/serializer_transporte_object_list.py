# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from transporte.utiles import serializer_transporte_object_list

register = template.Library()


def serializer_transportes(object_list):
    return serializer_transporte_object_list.listado_transportes(object_list)


register.filter('serializer_transportes', serializer_transportes)