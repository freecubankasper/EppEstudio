# -*- coding: utf-8 -*-
from django.db import models

from nomencladores.models.marca_comercial_registrada import MarcaComercialRegistrada
from nomencladores.models.sub_categoria import SubCategoria


class Equipamiento(models.Model):

    nombre = models.CharField(max_length=250)

    sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    marca = models.ForeignKey(MarcaComercialRegistrada, on_delete=models.CASCADE)

    cantidad = models.IntegerField()

    descripcion = models.TextField()

    precio_mlc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    precio_cup = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    equipamiento_img = models.ImageField(upload_to='equipamiento_img/', blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'equipamiento'
        db_table = 'equipamiento'
        verbose_name = 'equipamiento'
        verbose_name_plural = 'equipamientos'
        ordering = ['id']
        permissions = (
            ('enable_equipamiento', 'Can enable equipamiento'),
            ('disable_equipamiento', 'Can disable equipamiento'),
            ('delete_equipamientos_seleccionados', 'Can delete equipamientos seleccionados'),
            ('view_menu_equipamiento', 'Can view menu equipamiento')
        )