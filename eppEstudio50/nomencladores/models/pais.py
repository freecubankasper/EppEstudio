# -*- coding: utf-8 -*-
from django.db import models


class Pais(models.Model):

    nombre = models.CharField(max_length=150)

    nacionalidad = models.CharField(max_length=150, null=True, blank=True)

    siglas = models.CharField(max_length=150, null=True, blank=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_pais'
        verbose_name = 'pais'
        verbose_name_plural = 'paises'
        ordering = ['id']
        permissions = (
            ('enable_pais', 'Can enable pais'),
            ('disable_pais', 'Can disable pais'),
        )