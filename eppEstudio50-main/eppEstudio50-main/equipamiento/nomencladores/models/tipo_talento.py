# -*- coding: utf-8 -*-
from django.db import models


class TipoTalento(models.Model):

    nombre = models.CharField(max_length=250)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_tipo_talento'
        verbose_name = 'tipo_talento'
        verbose_name_plural = 'tipos de talento'
        ordering = ['id']
        permissions = (
            ('enable_tipotalento', 'Can enable tipo talento'),
            ('disable_tipotalento', 'Can disable tipo talento'),
        )