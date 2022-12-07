# -*- coding: utf-8 -*-
from django.db import models

from nomencladores.models import Municipio
from nomencladores.models.sub_categoria import SubCategoria
from nomencladores.models.tipo_arquitectura import TipoArquitectura
from nomencladores.models.tipo_lugar import TipoLugar
from nomencladores.models.tipo_suelo import TipoSuelo


class Locacion(models.Model):

    nombre = models.CharField(max_length=250)

    sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    direccion = models.CharField(max_length=250)

    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    tipo_suelo = models.ForeignKey(TipoSuelo, on_delete=models.CASCADE)

    tipo_arquitectura = models.ForeignKey(TipoArquitectura, on_delete=models.CASCADE)

    tipo_lugar = models.ForeignKey(TipoLugar, on_delete=models.CASCADE)

    precio_mlc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    precio_cup = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    amanecer_img = models.ImageField(upload_to='amanecer_img/', blank=True, null=True)

    mediodia_img = models.ImageField(upload_to='mediodia_img/', blank=True, null=True)

    anochecer_img = models.ImageField(upload_to='anochecer_img/', blank=True, null=True)

    noche_img = models.ImageField(upload_to='noche_img/', blank=True, null=True)

    perfil_lugar_img = models.ImageField(upload_to='perfil_lugar_img/', blank=True, null=True)

    propietario_lugar = models.CharField(max_length=300)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'locacion'
        db_table = 'locacion'
        verbose_name = 'locacion'
        verbose_name_plural = 'locaciones'
        ordering = ['id']
        permissions = (
            ('enable_locacion', 'Can enable locacion'),
            ('disable_locacion', 'Can disable locacion'),
            ('delete_locaciones_seleccionados', 'Can delete locaciones seleccionados'),
            ('view_menu_locacion', 'Can view menu locacion')
        )
