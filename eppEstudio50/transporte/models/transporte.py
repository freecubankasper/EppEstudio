# -*- coding: utf-8 -*-
from django.db import models

from nomencladores.models.marca_transporte import MarcaTransporte
from nomencladores.models.modelo_transporte import Modelo
from nomencladores.models.sub_categoria import SubCategoria
from nomencladores.models.tipo_vehiculo import TipoVehiculo


class Transporte(models.Model):

    tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE)

    marca = models.ForeignKey(MarcaTransporte, on_delete=models.CASCADE)

    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    color = models.CharField(max_length=250)

    sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    peso_maximo = models.CharField(max_length=250)

    cantidad_persona = models.IntegerField()

    persona_chofer = models.CharField(max_length=250)

    anno_fabricacion = models.IntegerField()

    precio_mlc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    precio_cup = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    transporte_img = models.ImageField(upload_to='transporte_img/', blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo_vehiculo.nombre

    class Meta:
        app_label = 'transporte'
        db_table = 'transporte'
        verbose_name = 'transporte'
        verbose_name_plural = 'transportees'
        ordering = ['id']
        permissions = (
            ('enable_transporte', 'Can enable transporte'),
            ('disable_transporte', 'Can disable transporte'),
            ('delete_transportes_seleccionados', 'Can delete transportes seleccionados'),
            ('view_menu_transporte', 'Can view menu transporte')
        )
