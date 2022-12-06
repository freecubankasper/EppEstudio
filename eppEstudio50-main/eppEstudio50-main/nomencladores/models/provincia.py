# -*- coding: utf-8 -*-
from django.db import models


class Provincia(models.Model):

    nombre = models.CharField(max_length=150)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_provincia'
        verbose_name = 'provincia'
        verbose_name_plural = 'provincias'
        ordering = ['id']
        permissions = (
            ('enable_provincia', 'Can enable provincia'),
            ('disable_provincia', 'Can disable provincia'),
        )