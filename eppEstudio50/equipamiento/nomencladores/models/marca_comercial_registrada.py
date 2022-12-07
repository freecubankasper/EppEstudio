# -*- coding: utf-8 -*-
from django.db import models


class MarcaComercialRegistrada(models.Model):

    nombre = models.CharField(max_length=250)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_marca_comercial_registrada'
        verbose_name = 'marca_comercial_registrada'
        verbose_name_plural = 'marcas comercial registrada'
        ordering = ['id']
        permissions = (
            ('enable_marca_comercial_registrada', 'Can enable marca comercial registrada'),
            ('disable_marca_comercial_registrada', 'Can disable marca comercial registrada'),
        )