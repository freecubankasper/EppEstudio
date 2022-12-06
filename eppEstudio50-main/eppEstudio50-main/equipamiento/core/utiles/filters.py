import django_filters

from actor.models.actor import Actor
from equipamiento.models.equipamiento import Equipamiento
from especialista.models.especialista import Especialista
from locacion.models.locacion import Locacion
from nomencladores.models.categoria import Categoria
from nomencladores.models.sub_categoria import SubCategoria
from proyecto.models import Proyecto
from transporte.models.transporte import Transporte


class EquipamientoFilter(django_filters.FilterSet):
    marca__nombre = django_filters
    sub_categoria = django_filters.ModelChoiceFilter(queryset=SubCategoria.objects.filter(categoria_servicio=1))
    precio_mlc__gt = django_filters.NumberFilter(field_name='precio_mlc', lookup_expr='gte')
    precio_mlc__lt = django_filters.NumberFilter(field_name='precio_mlc', lookup_expr='lt')
    class Meta:
        model = Equipamiento
        fields = ['nombre', 'marca','sub_categoria','cantidad','precio_mlc']

class ActorFilter(django_filters.FilterSet):
    municipio__nombre = django_filters
    # municipio__provincia__nombre = django_filters
    subcategoria_servicio = django_filters.ModelChoiceFilter(queryset=SubCategoria.objects.filter(categoria_servicio=3))
    class Meta:
        model = Actor
        fields = ['primer_nombre', 'apodo','sexo','municipio','subcategoria_servicio']

class EspecialidadesFilter(django_filters.FilterSet):
    primer_nombre = django_filters
    # municipio__provincia__nombre = django_filters
    subcategoria_servicio = django_filters.ModelChoiceFilter(queryset=SubCategoria.objects.filter(categoria_servicio=2))
    class Meta:
        model = Especialista
        fields = ['primer_nombre', 'apodo','sexo','municipio','subcategoria_servicio']


class LocacionFilter(django_filters.FilterSet):
    marca__nombre = django_filters
    subcategoria__nombre = django_filters
    precio_mlc__gt = django_filters.NumberFilter(field_name='precio_mlc', lookup_expr='gte')
    precio_mlc__lt = django_filters.NumberFilter(field_name='precio_mlc', lookup_expr='lt')
    class Meta:
        model = Locacion
        fields = ['nombre','sub_categoria','precio_mlc']

class CarrosFilter(django_filters.FilterSet):
    marca__nombre = django_filters
    precio_mlc__gt = django_filters.NumberFilter(field_name='precio_mlc', lookup_expr='gte')
    precio_mlc__lt = django_filters.NumberFilter(field_name='precio_mlc', lookup_expr='lt')
    class Meta:
        model = Transporte
        fields = ['marca','color','persona_chofer']

class MisproyectosFilter(django_filters.FilterSet):
    nombre = django_filters
    categoria__nombre = django_filters
    class Meta:
        model = Proyecto
        fields = ['nombre','categoria']