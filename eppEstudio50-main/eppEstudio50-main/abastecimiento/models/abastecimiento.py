# -*- coding: utf-8 -*-
from django.db import models
from nomencladores.models.sub_categoria import SubCategoria


class Abastecimiento(models.Model):

    nombre = models.CharField(max_length=250)

    direccion_domicilio = models.CharField(max_length=250, blank=True, null=True)

    sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    nombre_producto = models.CharField(max_length=250)

    descripcion = models.TextField()

    precio_mlc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    precio_cup = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    abastecimiento_img = models.ImageField(upload_to='abastecimiento_img/', blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'abastecimiento'
        db_table = 'abastecimiento'
        verbose_name = 'abastecimiento'
        verbose_name_plural = 'abastecimientos'
        ordering = ['id']
        permissions = (
            ('enable_abastecimiento', 'Can enable abastecimiento'),
            ('disable_abastecimiento', 'Can disable abastecimiento'),
            ('delete_abastecimientos_seleccionados', 'Can delete abastecimientos seleccionados'),
            ('view_menu_abastecimiento', 'Can view menu abastecimiento')
        )