# -*- coding: utf-8 -*-
from django.db import models


class CategoriaLicenciaConduccion(models.Model):

    nombre = models.CharField(max_length=250)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_categoria_lic_conduccion'
        verbose_name = 'categoria lic conduccion'
        verbose_name_plural = 'categorias lic conduccion'
        ordering = ['id']
        permissions = (
            ('enable_categorialicenciaconduccion', 'Can enable categoria licencia conduccion'),
            ('disable_categorialicenciaconduccion', 'Can disable categoria licencia conduccion'),
        )