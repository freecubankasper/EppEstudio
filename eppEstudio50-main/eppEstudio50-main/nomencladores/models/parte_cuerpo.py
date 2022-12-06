# -*- coding: utf-8 -*-
from django.db import models


class ParteCuerpo(models.Model):

    nombre = models.CharField(max_length=250)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_parte_cuerpo'
        verbose_name = 'parte_cuerpo'
        verbose_name_plural = 'partes del cuerpo'
        ordering = ['id']
        permissions = (
            ('enable_parte_cuerpo', 'Can enable parte cuerpo'),
            ('disable_parte_cuerpo', 'Can disable parte cuerpo'),
        )