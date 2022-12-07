# -*- coding: utf-8 -*-
from django.db import models

from proyecto.models import Proyecto

TIPOLLAMADO = (
    ("Medio LLamado", 'medio_llamado'),
    ("Llamado Completo", 'llamado_completo'),
)
class LlamadoProyecto(models.Model):

    titulo = models.CharField(max_length=250)

    centro_emergencia = models.CharField(max_length=250)

    tipo_pago = models.CharField(choices=TIPOLLAMADO, max_length=25, default='medio_llamado')

    direccion_centro_emergencia = models.CharField(max_length=250)

    precio_mlc_acumulado = models.IntegerField(blank=True, null=True)

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, blank=True, null=True)

    production_call = models.DateTimeField()

    courtesy_meal = models.DateTimeField()

    crew_call = models.DateTimeField()

    artist_call = models.DateTimeField()

    ready_to_shoot = models.DateTimeField()

    first_meal = models.DateTimeField(blank=True, null=True)

    second_meal = models.DateTimeField(blank=True, null=True)

    third_meal = models.DateTimeField(blank=True, null=True)

    estimated_camera_wrap = models.DateTimeField()

    observaciones = models.CharField(max_length=250)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_fin_llamado = models.DateTimeField(blank=True, null=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'llamado'
        db_table = 'llamado_proyecto'
        verbose_name = 'llamado proyecto'
        verbose_name_plural = 'llamados proyecto'
        ordering = ['id']
        permissions = (
            ('enable_llamadoproyecto', 'Can enable llamado proyecto'),
            ('disable_llamadoproyecto', 'Can disable llamado proyecto'),
            ('delete_llamadosproyecto_seleccionados', 'Can delete llamados proyecto seleccionados'),
        )