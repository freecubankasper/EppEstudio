from __future__ import unicode_literals
from django.db import models

from nomencladores.models.categoria import Categoria
from usuario.models import User


class Proyecto(models.Model):

    nombre = models.CharField(max_length=250)

    cliente = models.CharField(max_length=250)

    emergencia = models.CharField(max_length=250)

    observaciones_aprobacion = models.CharField(max_length=250, blank=True, null=True)

    precio_aprobacion = models.IntegerField(blank=True, null=True)

    fecha_inicio = models.DateField()

    fecha_fin = models.DateField()

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)

    estado_proyecto = models.CharField(max_length=100, default="Creado")

    fecha_estado_proyecto = models.DateTimeField(blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    def callcount_(self):
        from llamado.models.llamado_proyecto import LlamadoProyecto
        return LlamadoProyecto.objects.filter(proyecto_id=self.id).count()
    class Meta:
        app_label = 'proyecto'
        db_table = 'proyecto'
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['id']
        permissions = (
            ('enable_proyecto', 'Can enable proyecto'),
            ('disable_proyecto', 'Can disable proyecto'),
            ('delete_proyecto_seleccionados', 'Can delete proyecto seleccionados'),
            ('view_menu_proyecto', 'Can view_menu_proyecto'),
            ('update_estado_proyecto', 'Can update estado proyecto'),
        )


class HistorialEstadoProyecto(models.Model):

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    estado_proyecto = models.CharField(max_length=100)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'proyecto'
        db_table = 'proyecto_historial_estado_proyecto'
        ordering = ['-id']

