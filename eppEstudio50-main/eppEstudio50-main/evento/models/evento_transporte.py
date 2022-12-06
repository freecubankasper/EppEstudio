from __future__ import unicode_literals
from django.db import models

from transporte.models.transporte import Transporte


class EventoTransporte(models.Model):

    titulo = models.CharField(max_length=250)

    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE, blank=True, null=True)

    descripcion = models.TextField()

    fecha_inicio_evento = models.DateTimeField()

    fecha_fin_evento = models.DateTimeField()

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'evento'
        db_table = 'evento_de_transporte'
        verbose_name = 'evento de transporte'
        verbose_name_plural = 'eventos de transporte'
        ordering = ['id']
        permissions = (
            ('enable_eventotransporte', 'Can enable evento transporte'),
            ('disable_eventotransporte', 'Can disable evento transporte'),
            ('export_eventostransporte', 'Can export eventos transporte'),
        )

