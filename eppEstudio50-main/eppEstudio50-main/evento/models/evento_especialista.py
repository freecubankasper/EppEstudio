from __future__ import unicode_literals
from django.db import models

from especialista.models.especialista import Especialista


class EventoEspecialista(models.Model):

    titulo = models.CharField(max_length=250)

    especialista = models.ForeignKey(Especialista, on_delete=models.CASCADE, blank=True, null=True)

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
        db_table = 'evento_del_especialista'
        verbose_name = 'evento del especialista'
        verbose_name_plural = 'eventos del especialista'
        ordering = ['id']
        permissions = (
            ('enable_eventoespecialista', 'Can enable eventoespecialista'),
            ('disable_eventoespecialista', 'Can disable eventoespecialista'),
            ('export_eventosespecialista', 'Can export eventosespecialista'),
        )

