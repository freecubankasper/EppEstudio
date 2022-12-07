# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from especialista.utiles import serializer_especialista_object_list


register = template.Library()


def serializer_especialistas(object_list):
    return serializer_especialista_object_list.listado_especialistas(object_list)


register.filter('serializer_especialistas', serializer_especialistas)