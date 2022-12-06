# -*- coding: utf-8 -*-
from django.db import models


class CategoriaServicio(models.Model):

    nombre = models.CharField(max_length=250)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_categoria_servicio'
        verbose_name = 'categoria_servicio'
        verbose_name_plural = 'categorias de servicio'
        ordering = ['id']
        permissions = (
            ('enable_categoriaservicio', 'Can enable categoriaservicio'),
            ('disable_categoriaservicio', 'Can disable categoriaservicio'),
        )