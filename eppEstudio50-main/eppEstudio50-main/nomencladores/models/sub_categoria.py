# -*- coding: utf-8 -*-
from django.db import models

from nomencladores.models.categoria_servicio import CategoriaServicio


class SubCategoria(models.Model):

    nombre = models.CharField(max_length=250)

    categoria_servicio = models.ForeignKey(CategoriaServicio, on_delete=models.CASCADE)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_sub_categoria'
        verbose_name = 'sub_categoria'
        verbose_name_plural = ' sub categorias'
        ordering = ['id']
        permissions = (
            ('enable_subcategoria', 'Can enable subcategoria'),
            ('disable_subcategoria', 'Can disable subcategoria'),
        )