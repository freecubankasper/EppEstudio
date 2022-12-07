from django.db import models
from especialista.utiles.validaciones import validacion_ci
from nomencladores.models import Municipio
from nomencladores.models.idioma import Idioma
from nomencladores.models.pais import Pais
from nomencladores.models.sub_categoria import SubCategoria

SEXO = (
    ("Femenino", 'F'),
    ("Masculino", 'M'),
)


class Especialista(models.Model):

    ci = models.CharField(max_length=11, validators=[validacion_ci])

    num_pasaporte = models.CharField(max_length=11, blank=True, null=True)

    otro_documento = models.CharField(max_length=200, blank=True, null=True)

    primer_nombre = models.CharField(max_length=255)

    segundo_nombre = models.CharField(max_length=255, blank=True, null=True, default="")

    primer_apellido = models.CharField(max_length=255)

    segundo_apellido = models.CharField(max_length=255)

    apodo = models.CharField(max_length=255, blank=True, null=True, default="")

    sexo = models.CharField(choices=SEXO, max_length=20)

    fecha_nacimiento = models.DateField()

    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, blank=True, null=True)

    direccion = models.CharField(max_length=255)

    correo = models.EmailField(max_length=100)

    telefono = models.CharField(max_length=20, null=True, blank=True)

    telefono_movil = models.CharField(max_length=20, blank=True, null=True)

    facebook = models.CharField(max_length=100, blank=True, null=True)

    subcategoria_servicio = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    idioma = models.ManyToManyField(Idioma, related_name="idioma_especialista")

    habilidades = models.TextField()

    precio_mlc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    precio_cup = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    especialista_img = models.ImageField(upload_to='especialista_img/', blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.primer_nombre

    def sexo_(self):
        return dict(SEXO).get(self.sexo)

    def activo_(self):
        return 'Habilitado' if self.activo else 'Deshabilitado'

    class Meta:
        app_label = 'especialista'
        db_table = 'especialista'
        verbose_name = 'especialista'
        verbose_name_plural = 'especialistas'
        ordering = ['id']
        permissions = (
            ('enable_especialista', 'Can enable especialista'),
            ('disable_especialista', 'Can disable especialista'),
            ('delete_especialistas_seleccionados', 'Can delete especialistas seleccionados'),
            ('view_menu_especialistas', 'Can view menu especialistas')
        )