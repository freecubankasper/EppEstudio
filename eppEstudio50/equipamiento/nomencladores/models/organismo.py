# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Organismo(models.Model):

    nombre = models.CharField(max_length=255, unique=True)

    siglas = models.CharField(max_length=20)

    hijode = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_organismo'
        verbose_name = 'organismo'
        verbose_name_plural = 'organismos'
        ordering = ['id']
        permissions = (
            ('enable_organismo', 'Can enable organismo'),
            ('disable_organismo', 'Can disable organismo'),
        )
