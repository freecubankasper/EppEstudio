# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from abastecimiento.utiles import serializer_abastecimiento_object_list

register = template.Library()


def serializer_abastecimientos(object_list):
    return serializer_abastecimiento_object_list.listado_abastecimientos(object_list)


register.filter('serializer_abastecimientos', serializer_abastecimientos)