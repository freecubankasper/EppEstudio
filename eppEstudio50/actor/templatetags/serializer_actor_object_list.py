# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from actor.utiles import serializer_actor_object_list


register = template.Library()


def serializer_actores(object_list):
    return serializer_actor_object_list.listado_actores(object_list)


register.filter('serializer_actores', serializer_actores)