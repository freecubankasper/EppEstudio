# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from equipo_proteccion_personal.models.factura import Factura
from equipo_proteccion_personal.models.numero_prefactura import NumeroPrefactura
from nomencladores.models import Entidad
from nomencladores.models.categoria import Categoria
from nomencladores.models.marca_comercial_registrada import MarcaComercialRegistrada
from nomencladores.models.parte_cuerpo import ParteCuerpo
from usuario.models import User


class EquipoProteccionPersonal(models.Model):

    nombre = models.CharField(max_length=250)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    tipo_aprobacion = models.CharField(max_length=250)

    entidad_importadora = models.ForeignKey(Entidad, related_name="%(class)s_entidad_importadora", null=True, blank=True, on_delete=models.CASCADE)

    fecha_vencimiento_certificado = models.DateField()

    marca_comercial_registrada = models.ForeignKey(MarcaComercialRegistrada, on_delete=models.CASCADE)

    modelo = models.CharField(max_length=250, blank=True, null=True)

    numero_referencia = models.CharField(max_length=15, blank=True, null=True)

    clientes_usuarios = models.CharField(max_length=500)

    muestras_equipo = models.BooleanField()

    renovado = models.BooleanField(default=False)

    equipo_ya_certificado = models.BooleanField(default=False)

    fecha_renovacion = models.DateTimeField(blank=True, null=True)

    numero_prefactura = models.ForeignKey(NumeroPrefactura, on_delete=models.CASCADE)

    primera_img = models.ImageField(upload_to='primeras_img_epp/', blank=True, null=True)

    segunda_img = models.ImageField(upload_to='segundas_img_epp/', blank=True, null=True)

    tercera_img = models.ImageField(upload_to='terceras_img_epp/', blank=True, null=True)

    parte_cuerpo = models.ManyToManyField(ParteCuerpo, related_name="parte_cuerpo")

    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, blank=True, null=True)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'equipo_proteccion_personal'
        db_table = 'equipo_proteccion_personal'
        verbose_name = 'equipo proteccion personal'
        verbose_name_plural = 'equipos de proteccion personal'
        ordering = ['id']
        permissions = (
            ('enable_equipo_proteccion_personal', 'Can enable equipo proteccion personal'),
            ('disable_equipo_proteccion_personal', 'Can disable equipo proteccion personal'),
            ('renew_equipo_proteccion_personal', 'Can renew equipo proteccion personal'),
            ('delete_equipo_proteccion_personal_seleccionados', 'Can delete equipo proteccion personal seleccionados'),
            ('view_menu_equipo_proteccion_personal', 'Can view menu equipo proteccion personal'),
            ('view_listado_reportes', 'Can view view listado reportes'),
            ('view_reporte_equipo_proteccion_personal_registrado', 'Can view view_reporte equipo proteccion personal registrado'),
            ('view_reporte_equipo_proteccion_personal_aprobado', 'Can view view_reporte equipo proteccion personal aprobado'),
            ('view_reporte_equipo_proteccion_personal_vencido', 'Can view view_reporte equipo proteccion personal vencido'),
            ('view_menu_reporte_principal', 'Can view view menu reporte principal'),
            ('view_menu_reporte', 'Can view view menu reporte'),
            ('export_factura', 'Can export factura'),
            ('export_prefactura', 'Can export prefactura'),
            ('export_certificado_epp', 'Can export certificado epp'),
        )


class HistorialEPPRenovado(models.Model):

    equipo = models.ForeignKey(EquipoProteccionPersonal, on_delete=models.CASCADE)

    renovado = models.BooleanField()

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def renovado_(self):
        return self.renovado

    class Meta:
        app_label = 'equipo_proteccion_personal'
        db_table = 'epp_historial_epp_renovado'
        ordering = ['-id']