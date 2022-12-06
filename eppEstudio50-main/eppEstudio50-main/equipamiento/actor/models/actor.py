from django.db import models
from actor.utiles.validaciones import validacion_ci
from nomencladores.models import Municipio
from nomencladores.models.categoria_lic_conduccion import CategoriaLicenciaConduccion
from nomencladores.models.idioma import Idioma
from nomencladores.models.pais import Pais
from nomencladores.models.sub_categoria import SubCategoria

SEXO = (
    ("Femenino", 'F'),
    ("Masculino", 'M'),
    ("Otro", 'Otro'),
)

COLORPIEL= (
    ("Blanco", 'Blanco'),
    ("Negro", 'Negro'),
    ("Mestizo", 'Mestizo'),
)

COLOROJOS= (
    ("Negro", 'Negro'),
    ("Marron", 'Marrón'),
    ("Verde", 'Verde'),
    ("Azul", 'Azul'),
)

TIPOPELO= (
    ("Lacio", 'Lacio'),
    ("Ondulado", 'Ondulado'),
    ("Rizado", 'Rizado'),
    ("Crespo", 'Crespo'),
)

TENDENCIARACIAL= (
    ("Afro", 'Afro'),
    ("Blanca", 'Blanca'),
    ("Amarilla", 'Amarilla'),
    ("Roja", 'Roja'),
)


class Actor(models.Model):

    ci = models.CharField(max_length=11, validators=[validacion_ci])

    num_pasaporte = models.CharField(max_length=11, blank=True, null=True)

    otro_documento = models.CharField(max_length=200, blank=True, null=True)

    categoria_lic_conduccion = models.ManyToManyField(CategoriaLicenciaConduccion, related_name="categoria_lic_conduccion")

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

    correo = models.EmailField(max_length=100, blank=True, null=True)

    telefono = models.CharField(max_length=20, null=True, blank=True)

    telefono_movil = models.CharField(max_length=20, blank=True, null=True)

    instagram = models.CharField(max_length=100, blank=True, null=True)

    subcategoria_servicio = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    idioma = models.ManyToManyField(Idioma, related_name="idioma")

    habilidades = models.TextField()

    estatura = models.CharField(max_length=100)

    peso = models.CharField(max_length=100)

    color_piel = models.CharField(choices=COLORPIEL, max_length=20)

    color_ojos = models.CharField(choices=COLOROJOS, max_length=20)

    tipo_pelo = models.CharField(choices=TIPOPELO, max_length=20)

    tendencia_racial = models.CharField(choices=TENDENCIARACIAL, max_length=30)

    cadera = models.CharField(max_length=100, blank=True, null=True)

    cintura = models.CharField(max_length=100, blank=True, null=True)

    hombro = models.CharField(max_length=100, blank=True, null=True)

    calzado = models.CharField(max_length=100)

    observaciones = models.CharField(max_length=100,blank=True, null=True)

    precio_euro = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    primera_img = models.ImageField(upload_to='primeras_img_actor/', blank=True, null=True)

    segunda_img = models.ImageField(upload_to='segundas_img_actor/', blank=True, null=True)

    tercera_img = models.ImageField(upload_to='terceras_img_actor/', blank=True, null=True)

    cuarta_img = models.ImageField(upload_to='cuartas_img_actor/', blank=True, null=True)

    quinta_img = models.ImageField(upload_to='quintas_img_actor/', blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.primer_nombre

    def sexo_(self):
        return dict(SEXO).get(self.sexo)

    def color_piel_(self):
        return dict(COLORPIEL).get(self.color_piel)

    def color_ojos_(self):
        return dict(COLOROJOS).get(self.color_ojos)

    def tipo_pelo_(self):
        return dict(TIPOPELO).get(self.tipo_pelo)

    def tendencia_racial_(self):
        return dict(TENDENCIARACIAL).get(self.tendencia_racial)

    def activo_(self):
        return 'Habilitado' if self.activo else 'Deshabilitado'

    class Meta:
        app_label = 'actor'
        db_table = 'actor'
        verbose_name = 'actor'
        verbose_name_plural = 'actores'
        ordering = ['id']
        permissions = (
            ('enable_actor', 'Can enable actor'),
            ('disable_actor', 'Can disable actor'),
            ('delete_actores_seleccionados', 'Can delete actores seleccionados'),
            ('view_menu_actor', 'Can view menu actor')
        )