from __future__ import unicode_literals
from django.db import models

from locacion.models.locacion import Locacion


class EventoLocacion(models.Model):

    titulo = models.CharField(max_length=250)

    locacion = models.ForeignKey(Locacion, on_delete=models.CASCADE, blank=True, null=True)

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
        db_table = 'evento_de_locacion'
        verbose_name = 'evento de locacion'
        verbose_name_plural = 'eventos de locacion'
        ordering = ['id']
        permissions = (
            ('enable_eventolocacion', 'Can enable evento locacion'),
            ('disable_eventolocacion', 'Can disable evento locacion'),
            ('export_eventoslocacion', 'Can export eventos locacion'),
        )

