# -*- coding: utf-8 -*-
from django.db import models


class Categoria(models.Model):

    nombre = models.CharField(max_length=250)

    precio_cup = models.IntegerField()

    precio_mlc = models.IntegerField()

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_categoria'
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['id']
        permissions = (
            ('enable_categoria', 'Can enable categoria'),
            ('disable_categoria', 'Can disable categoria'),
        )