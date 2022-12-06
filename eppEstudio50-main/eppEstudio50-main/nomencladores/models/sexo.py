from django.db import models

class Sexo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_sexo'
        verbose_name = 'sexo'
        verbose_name_plural = 'sexos'
        ordering = ['id']

