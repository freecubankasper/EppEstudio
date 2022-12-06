from __future__ import unicode_literals
from django.db import models

from actor.models.actor import Actor


class EventoActor(models.Model):

    titulo = models.CharField(max_length=250)

    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, blank=True, null=True)

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
        db_table = 'evento_del_actor'
        verbose_name = 'evento del actor'
        verbose_name_plural = 'eventos del actor'
        ordering = ['id']
        permissions = (
            ('enable_eventoactor', 'Can enable eventoactor'),
            ('disable_eventoactor', 'Can disable eventoactor'),
            ('export_eventosactor', 'Can export eventosactor'),
        )

