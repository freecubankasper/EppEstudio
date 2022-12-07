# -*- coding: utf-8 -*-
from django.db import models


class Idioma(models.Model):

    nombre = models.CharField(max_length=250)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_idioma'
        verbose_name = 'idioma'
        verbose_name_plural = 'idioma'
        ordering = ['id']
        permissions = (
            ('enable_idioma', 'Can enable idioma'),
            ('disable_idioma', 'Can disable idioma'),
        )