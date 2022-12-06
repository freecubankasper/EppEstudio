# -*- coding: utf-8 -*-
from django.db import models


class TipoSuelo(models.Model):

    nombre = models.CharField(max_length=250)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_tipo_suelo'
        verbose_name = 'tipo_suelo'
        verbose_name_plural = 'tipos de suelo'
        ordering = ['id']
        permissions = (
            ('enable_tipo_suelo', 'Can enable tipo suelo'),
            ('disable_tipo_suelo', 'Can disable tipo suelo'),
        )