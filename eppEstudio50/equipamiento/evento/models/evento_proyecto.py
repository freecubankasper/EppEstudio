from __future__ import unicode_literals
from django.db import models

from actor.models.actor import Actor
from equipamiento.models.equipamiento import Equipamiento
from llamado.models.llamado_proyecto import LlamadoProyecto
from nomencladores.models.sub_categoria import SubCategoria


class EventoProyecto(models.Model):

    titulo = models.CharField(max_length=250)

    llamado = models.ForeignKey(LlamadoProyecto, on_delete=models.CASCADE, blank=True, null=True)

    subcategoria_servicio = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    actor = models.ManyToManyField(Actor, related_name="actor", blank=True)

    equipamiento = models.ManyToManyField(Equipamiento, related_name="equipamiento", blank=True)

    descripcion = models.TextField()

    precio_mlc_acumulado = models.IntegerField(blank=True, null=True)

    fecha_inicio_evento = models.DateTimeField()

    fecha_fin_evento = models.DateTimeField()

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'evento'
        db_table = 'evento_proyecto'
        verbose_name = 'evento proyecto'
        verbose_name_plural = 'eventos proyecto'
        ordering = ['id']
        permissions = (
            ('enable_eventoproyecto', 'Can enable eventoproyecto'),
            ('disable_eventoproyecto', 'Can disable eventoproyecto'),
            ('export_eventosproyecto', 'Can export eventosproyecto'),
        )

