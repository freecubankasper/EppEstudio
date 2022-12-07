import asyncio
import json
from django.http import HttpResponse

from actor.models.actor import Actor
from equipamiento.models.equipamiento import Equipamiento
from django.views.generic import TemplateView

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

def serializer_equipamiento(equipamiento):
    return {
        'id': equipamiento.id,
        'nombre': equipamiento.nombre,
        'descripcion': equipamiento.descripcion,
        'marca': equipamiento.marca.nombre,
        'categoria': equipamiento.sub_categoria.nombre,
        'cantidad': equipamiento.cantidad,
        'fecha_actualizacion': str(equipamiento.fecha_actualizacion.strftime("%d-%m-%Y")),
        'imagen': str(equipamiento.equipamiento_img),
    }

class DetallesEquipamientoAjaxView(TemplateView):

    def get(self, request, *args, **kwargs):
        element_id = request.GET.get('element_id')
        llamado = request.GET.get('llamado_id')
        element = serializer_equipamiento(Equipamiento.objects.get(id=element_id))
        return HttpResponse(json.dumps(element), content_type='application/json')


def serializer_talento(equipamiento):
    return {
        'id': equipamiento.id,
        'nombre': equipamiento.primer_nombre+' '+equipamiento.primer_apellido+' '+equipamiento.segundo_apellido,
        'sexo': equipamiento.sexo,
        'municipio': equipamiento.municipio.nombre,
        'descripcion': equipamiento.habilidades,
        'apodo': equipamiento.apodo,
        'estatura': equipamiento.estatura,
        'cadera': equipamiento.cadera,
        'calzado': equipamiento.calzado,
        'cintura': equipamiento.cintura,
        'hombro': equipamiento.hombro,
        'color_piel': equipamiento.color_piel,
        'color_ojos': equipamiento.color_ojos,
        'tipo_pelo': equipamiento.tipo_pelo,
        'categoria': equipamiento.subcategoria_servicio.nombre,
        'fecha_actualizacion': str(equipamiento.fecha_actualizacion.strftime("%d-%m-%Y")),
        'imagen': str(equipamiento.primera_img),
        'imagen2': str(equipamiento.segunda_img),
        'imagen3': str(equipamiento.tercera_img),
        'imagen4': str(equipamiento.cuarta_img),
        'imagen5': str(equipamiento.quinta_img),
    }

class DetallesTalentoAjaxView(TemplateView):

    def get(self, request, *args, **kwargs):
        element_id = request.GET.get('element_id')
        element = serializer_talento(Actor.objects.get(id=element_id))
        return HttpResponse(json.dumps(element), content_type='application/json')
