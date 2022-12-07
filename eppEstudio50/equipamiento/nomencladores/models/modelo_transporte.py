# -*- coding: utf-8 -*-
from django.db import models


class Modelo(models.Model):

    nombre = models.CharField(max_length=250)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_modelo'
        verbose_name = 'modelo'
        verbose_name_plural = 'modelos'
        ordering = ['id']
        permissions = (
            ('enable_modelo', 'Can enable modelo'),
            ('disable_modelo', 'Can disable modelo'),
        )