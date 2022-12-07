from django.db import models
from datetime import datetime
from nomencladores.models.municipio import Municipio
from nomencladores.models.organismo import Organismo
from nomencladores.models.pais import Pais

TIPO = (
    ("Nacional", 'Nacional'),
    ("Extranjera", 'Extranjera'),
)


class TipoEntidad(models.Model):

    nombre = models.CharField(max_length=250)

    tipo = models.CharField(choices=TIPO, max_length=30)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_tipo_entidad'
        verbose_name = 'tipo_entidad'
        verbose_name_plural = 'tipos de entidad'
        ordering = ['id']
        permissions = (
            ('enable_tipo_entidad', 'Can enable tipo entidad'),
            ('disable_tipo_entidad', 'Can disable tipo entidad'),
        )


class Entidad(models.Model):

    cod_reeup = models.CharField(max_length=15, blank=True, null=True)

    num_contrato = models.CharField(max_length=15, blank=True, null=True, unique=True)

    nombre = models.CharField(max_length=250)

    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    organismo = models.ForeignKey(Organismo, blank=True, null=True, on_delete=models.CASCADE)

    municipio = models.ForeignKey(Municipio, blank=True, null=True, on_delete=models.CASCADE)

    telefono = models.CharField(max_length=20)

    direccion = models.CharField(max_length=250)

    direccion_web = models.CharField(max_length=250, blank=True, null=True)

    correo = models.EmailField(max_length=100)

    num_lic_comercial_camara_comercio = models.CharField(max_length=15, blank=True, null=True)

    num_acta_protocolizacion = models.CharField(max_length=15, blank=True, null=True)

    identificacion_fiscal = models.CharField(max_length=15, blank=True, null=True)

    num_escritura_publica = models.CharField(max_length=15, blank=True, null=True)

    nombre_representante = models.CharField(max_length=250)

    cargo_representante = models.CharField(max_length=250)

    tipo_entidad_nacional = models.ForeignKey(TipoEntidad, related_name="%(class)s_tipo_entidad_nacional", blank=True, null=True, on_delete=models.CASCADE)

    tipo_entidad_extranjera = models.ForeignKey(TipoEntidad, related_name="%(class)s_tipo_entidad_extranjera", blank=True, null=True, on_delete=models.CASCADE)

    entidad_importadora = models.BooleanField()

    almacen = models.BooleanField()

    observaciones = models.TextField()

    fecha_registro = models.DateTimeField(default=datetime.today())

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'nomencladores'
        db_table = 'nomencladores_entidad'
        verbose_name = 'entidad'
        verbose_name_plural = 'entidades'
        ordering = ['id']
        permissions = (
            ('enable_entidad', 'Can enable entidad'),
            ('disable_entidad', 'Can disable entidad'),
            ('view_menu_nomencladores', 'Can view menu nomencladores'),
            ('view_reporte_entidad', 'Can view view reporte entidad'),
            ('export_certificado_entidad', 'Can export certificado entidad'),
        )
