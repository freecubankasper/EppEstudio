# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from equipo_proteccion_personal.models.numero_prefactura import NumeroPrefactura
from nomencladores.models import Entidad
from usuario.models import User

TIPOPAGO = (
    ("CUP", 'CUP'),
    ("MLC", 'MLC'),
)


class Factura(models.Model):

    numero_prefactura = models.ForeignKey(NumeroPrefactura, on_delete=models.CASCADE)

    tipo_pago = models.CharField(choices=TIPOPAGO, max_length=15)

    cantidad_cup = models.IntegerField()

    cantidad_mlc = models.IntegerField()

    cantidad_equipos = models.IntegerField()

    estado_pago = models.BooleanField(default=False)

    fecha_pago = models.DateField(blank=True, null=True)

    fecha_limite_pago = models.DateField()

    elaborado_nombre = models.CharField(max_length=250)

    elaborado_cargo = models.CharField(max_length=250)

    revisado_nombre = models.CharField(max_length=250)

    revisado_cargo = models.CharField(max_length=250)

    entregado_registrado_nombre = models.CharField(max_length=250)

    entregado_registrado_cargo = models.CharField(max_length=250)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.numero_prefactura

    def tipo_pago_(self):
        return dict(TIPOPAGO).get(self.tipo_pago)

    class Meta:
        app_label = 'equipo_proteccion_personal'
        db_table = 'epp_factura'
        verbose_name = 'factura'
        verbose_name_plural = 'facturas'
        ordering = ['id']
        permissions = (
            ('enable_factura', 'Can enable factura'),
            ('disable_factura', 'Can disable factura'),
            ('delete_factura_seleccionadas', 'Can delete factura seleccionadas'),
            ('pagar_factura', 'Can pagar factura'),
            ('view_reporte_factura', 'Can view reporte factura'),
        )
