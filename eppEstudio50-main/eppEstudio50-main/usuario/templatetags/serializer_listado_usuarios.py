# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from usuario.utiles import listado_usuarios, listado_grupos

register = template.Library()


def serializer_usuarios(object_list):
    return listado_usuarios(object_list)


register.filter('serializer_usuarios', serializer_usuarios)


def serializer_grupos(object_list):
    return listado_grupos(object_list)


register.filter('serializer_grupos', serializer_grupos)
