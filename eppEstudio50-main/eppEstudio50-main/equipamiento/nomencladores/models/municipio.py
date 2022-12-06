from django.db import models

from nomencladores.models.provincia import Provincia


class Municipio(models.Model):

    nombre = models.CharField(max_length=150)

    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)

    plan_turquino = models.BooleanField(default=False)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def plan_turquino_(self):
        return "Sí" if self.plan_turquino == True else "No"

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_municipio'
        verbose_name = 'municipio'
        verbose_name_plural = 'municipios'
        ordering = ['id']
        permissions = (
            ('enable_municipio', 'Can enable municipio'),
            ('disable_municipio', 'Can disable municipio'),
        )

