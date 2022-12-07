# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import FileExtensionValidator
from django.db import models


class Documento(models.Model):

    nombre = models.CharField(max_length=250)

    documento = models.FileField(upload_to='documentos/%Y/%m/%d', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'equipo_proteccion_personal'
        db_table = 'epp_documento'
        verbose_name = 'documento'
        verbose_name_plural = 'documentos'
        ordering = ['id']
        permissions = (
            ('enable_documento', 'Can enable documento'),
            ('disable_documento', 'Can disable documento'),
            ('download_documento', 'Can download documento'),
        )
