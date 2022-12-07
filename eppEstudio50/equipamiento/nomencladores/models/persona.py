from django.db import models
from datetime import datetime
from nomencladores.models.municipio import Municipio
from nomencladores.models.pais import Pais
from nomencladores.models.sexo import Sexo

class Persona(models.Model):
    ci = models.CharField(max_length=11, blank=True, null=True, unique=True)
    nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, blank=True, null=True, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=250)
    direccion_web = models.CharField(max_length=250, blank=True, null=True)
    direccion_facebook = models.CharField(max_length=250, blank=True, null=True)
    direccion_instagram = models.CharField(max_length=250, blank=True, null=True)
    direccion_twitter = models.CharField(max_length=250, blank=True, null=True)
    correo = models.EmailField(max_length=100, blank=True, null=True)
    observaciones = models.TextField()
    fecha_registro = models.DateTimeField(default=datetime.today())
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'persona'
        verbose_name = 'persona'
        verbose_name_plural = 'personas'
        ordering = ['id']

