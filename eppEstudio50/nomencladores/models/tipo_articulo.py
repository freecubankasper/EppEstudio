# -*- coding: utf-8 -*-
from django.db import models


class TipoArticulo(models.Model):

    nombre = models.CharField(max_length=250)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_tipo_articulo'
        verbose_name = 'tipo articulo'
        verbose_name_plural = 'tipos de articulo'
        ordering = ['id']
        permissions = (
            ('enable_tipoarticulo', 'Can enable tipo articulo'),
            ('disable_tipoarticulo', 'Can disable tipo articulo'),
        )