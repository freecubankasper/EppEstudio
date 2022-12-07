# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from llamado.utiles import serializer_llamado_object_list

register = template.Library()


def serializer_llamados_proyecto(object_list):
    return serializer_llamado_object_list.listado_llamados_proyecto(object_list)


register.filter('serializer_llamados_proyecto', serializer_llamados_proyecto)