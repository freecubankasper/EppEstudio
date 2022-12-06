# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from nomencladores.utiles import serializer_object_list

register = template.Library()


def serializer_organismos(object_list):
    return serializer_object_list.listado_organismos(object_list)


def serializer_entidades(object_list):
    return serializer_object_list.listado_entidades(object_list)


def serializer_municipios(object_list):
    return serializer_object_list.listado_municipios(object_list)


def serializer_idiomas(object_list):
    return serializer_object_list.listado_idiomas(object_list)


def serializer_provincias(object_list):
    return serializer_object_list.listado_provincias(object_list)


def serializer_tipos_entidad(object_list):
    return serializer_object_list.listado_tipos_entidad(object_list)


def serializer_categorias(object_list):
    return serializer_object_list.listado_categorias(object_list)


def serializer_categorias_lic_conduccion(object_list):
    return serializer_object_list.listado_categorias_lic_conduccion(object_list)


def serializer_categorias_servicio(object_list):
    return serializer_object_list.listado_categorias_servicio(object_list)


def serializer_subs_categoria(object_list):
    return serializer_object_list.listado_subs_categoria(object_list)


def serializer_tipos_suelo(object_list):
    return serializer_object_list.listado_tipos_suelo(object_list)


def serializer_tipos_arquitectura(object_list):
    return serializer_object_list.listado_tipos_arquitectura(object_list)


def serializer_tipos_lugar(object_list):
    return serializer_object_list.listado_tipos_lugar(object_list)


def serializer_tipos_vehiculo(object_list):
    return serializer_object_list.listado_tipos_vehiculo(object_list)


def serializer_marcas_comercial_registrada(object_list):
    return serializer_object_list.listado_marcas_comercial_registrada(object_list)


def serializer_modelos_transporte(object_list):
    return serializer_object_list.listado_modelos_transporte(object_list)


def serializer_marcas_transporte(object_list):
    return serializer_object_list.listado_marcas_transporte(object_list)


def serializer_paises(object_list):
    return serializer_object_list.listado_paises(object_list)


def serializer_partes_cuerpo(object_list):
    return serializer_object_list.listado_partes_cuerpo(object_list)


register.filter('serializer_organismos', serializer_organismos)
register.filter('serializer_entidades', serializer_entidades)
register.filter('serializer_idiomas', serializer_idiomas)
register.filter('serializer_municipios', serializer_municipios)
register.filter('serializer_provincias', serializer_provincias)
register.filter('serializer_tipos_entidad', serializer_tipos_entidad)
register.filter('serializer_categorias', serializer_categorias)
register.filter('serializer_categorias_lic_conduccion', serializer_categorias_lic_conduccion)
register.filter('serializer_categorias_servicio', serializer_categorias_servicio)
register.filter('serializer_subs_categoria', serializer_subs_categoria)
register.filter('serializer_tipos_suelo', serializer_tipos_suelo)
register.filter('serializer_tipos_arquitectura', serializer_tipos_arquitectura)
register.filter('serializer_tipos_lugar', serializer_tipos_lugar)
register.filter('serializer_tipos_vehiculo', serializer_tipos_vehiculo)
register.filter('serializer_marcas_comercial_registrada', serializer_marcas_comercial_registrada)
register.filter('serializer_modelos_transporte', serializer_modelos_transporte)
register.filter('serializer_marcas_transporte', serializer_marcas_transporte)
register.filter('serializer_paises', serializer_paises)
register.filter('serializer_partes_cuerpo', serializer_partes_cuerpo)
