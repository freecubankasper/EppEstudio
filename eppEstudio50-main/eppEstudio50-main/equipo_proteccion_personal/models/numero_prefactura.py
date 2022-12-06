# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from nomencladores.models import Entidad


class NumeroPrefactura(models.Model):

    numero_prefactura = models.CharField(max_length=15, unique=True)

    entidad = models.ForeignKey(Entidad, related_name="%(class)s_entidad", on_delete=models.CASCADE)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.numero_prefactura

    class Meta:
        app_label = 'equipo_proteccion_personal'
        db_table = 'epp_numero_prefactura'
        verbose_name = 'numero prefactura'
        verbose_name_plural = 'numeros prefactura'
        ordering = ['id']
        permissions = (
            ('enable_numero_prefactura', 'Can enable numero prefactura'),
            ('disable_numero_prefactura', 'Can disable numero prefactura'),
        )
