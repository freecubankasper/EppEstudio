# -*- coding: utf-8 -*-
from django.db import models


class MarcaTransporte(models.Model):

    nombre = models.CharField(max_length=250)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_marca_transporte'
        verbose_name = 'marca transporte'
        verbose_name_plural = 'marcas transporte'
        ordering = ['id']
        permissions = (
            ('enable_marcatransporte', 'Can enable marca transporte'),
            ('disable_marcatransporte', 'Can disable marca transporte'),
        )