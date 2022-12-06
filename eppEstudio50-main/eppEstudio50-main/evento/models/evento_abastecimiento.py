from __future__ import unicode_literals
from django.db import models

from abastecimiento.models.abastecimiento import Abastecimiento


class EventoAbastecimiento(models.Model):

    titulo = models.CharField(max_length=250)

    abastecimiento = models.ForeignKey(Abastecimiento, on_delete=models.CASCADE, blank=True, null=True)

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
        db_table = 'evento_de_abastecimiento'
        verbose_name = 'evento de abastecimiento'
        verbose_name_plural = 'eventos de abastecimiento'
        ordering = ['id']
        permissions = (
            ('enable_eventoabastecimiento', 'Can enable evento abastecimiento'),
            ('disable_eventoabastecimiento', 'Can disable evento abastecimiento'),
            ('export_eventosabastecimiento', 'Can export eventos abastecimiento'),
        )

