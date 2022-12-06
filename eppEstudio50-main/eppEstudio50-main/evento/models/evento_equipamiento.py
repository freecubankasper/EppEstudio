from __future__ import unicode_literals
from django.db import models

from equipamiento.models.equipamiento import Equipamiento
from llamado.models.llamado_proyecto import LlamadoProyecto


class EventoEquipamiento(models.Model):

    titulo = models.CharField(max_length=250)

    equipamiento = models.ForeignKey(Equipamiento, on_delete=models.CASCADE, blank=True, null=True)

    llamado = models.ForeignKey(LlamadoProyecto, on_delete=models.CASCADE, blank=True, null=True)

    cantidad = models.IntegerField()

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
        db_table = 'evento_del_equipamiento'
        verbose_name = 'evento del equipamiento'
        verbose_name_plural = 'eventos del equipamiento'
        ordering = ['id']
        permissions = (
            ('enable_eventoequipamiento', 'Can enable eventoequipamiento'),
            ('disable_eventoequipamiento', 'Can disable eventoequipamiento'),
            ('export_eventosequipamiento', 'Can export eventosequipamiento'),
        )

