from __future__ import unicode_literals
from django.db import models

from actor.models.actor import Actor
from equipamiento.models.equipamiento import Equipamiento
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.sub_categoria import SubCategoria
from proyecto.models import Proyecto


class Evento(models.Model):

    titulo = models.CharField(max_length=250)

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, blank=True, null=True)

    subcategoria_servicio = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    categoria_servicio = models.ForeignKey(CategoriaServicio, on_delete=models.CASCADE)

    actor = models.ManyToManyField(Actor, related_name="actor", blank=True)

    equipamiento = models.ManyToManyField(Equipamiento, related_name="equipamiento", blank=True)

    fecha_inicio_evento = models.DateTimeField()

    fecha_fin_evento = models.DateTimeField()

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'evento'
        db_table = 'evento'
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'
        ordering = ['id']
        permissions = (
            ('enable_evento', 'Can enable evento'),
            ('disable_evento', 'Can disable evento'),
            ('view_menu_evento', 'Can view menu evento'),
            ('export_eventos', 'Can export eventos'),
        )


