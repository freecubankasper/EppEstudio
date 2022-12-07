# -*- coding: utf-8 -*-
from datetime import timedelta

from django.http import HttpResponseRedirect
from django.utils.dateparse import parse_datetime
from django.views import View
from django.views.generic import TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from equipo_proteccion_personal.models.documento import Documento
from evento.models.evento_proyecto import EventoProyecto
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView, DeleteView

from llamado.models.llamado_proyecto import LlamadoProyecto
from nomencladores.models.categoria import Categoria
from proyecto.models import Proyecto
from proyecto.templatetags.serializer_proyectos import proyecto_serializer


class LlamadoView(View):
    def get(self, request, *args, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        eventos = Proyecto.objects.filter(id=proyecto_id).first()
        titulo = request.GET.get('id_call_nombre')
        centro_emergencia = request.GET.get('id_centro_emergencia')
        direccion_centro_emergencia = request.GET.get('id_direccion_centro_emergencia')
        production_call = request.GET.get('id_production_call')
        courtesy_meal = request.GET.get('id_courtesy_meal')
        crew_call = request.GET.get('id_crew_call')
        artist_call = request.GET.get('id_artist_call')
        ready_to_shoot = request.GET.get('id_ready_to_shoot')
        tipo_llamdo = request.GET.get('id_call_type')
        estimated_camera_wrap = request.GET.get('id_estimated_camera_wrap')
        observaciones = request.GET.get('id_observaciones')
        fecha = parse_datetime(production_call)
        if tipo_llamdo == 'medio_llamado':
            fecha_fin_llamado = fecha + timedelta(hours=6)
        else:
            fecha_fin_llamado = fecha + timedelta(hours=12)
        llamado = LlamadoProyecto.objects.create(titulo=titulo, centro_emergencia=centro_emergencia, proyecto=eventos,
                                                 tipo_pago=tipo_llamdo, fecha_fin_llamado=fecha_fin_llamado,
                                                 direccion_centro_emergencia=direccion_centro_emergencia,
                                                 production_call=production_call, courtesy_meal=courtesy_meal,
                                                 crew_call=crew_call, artist_call=artist_call,
                                                 ready_to_shoot=ready_to_shoot,
                                                 estimated_camera_wrap=estimated_camera_wrap,
                                                 observaciones=observaciones)

        return HttpResponseRedirect(reverse_lazy('calendario', kwargs={'proyecto_id': eventos.id}))
class CalendarioView(ListView):
    model = EventoProyecto
    template_name = 'calendario.html'


    def get_queryset(self):
        proyecto_id = self.kwargs['proyecto_id']
        llamados = LlamadoProyecto.objects.filter(proyecto_id=proyecto_id).order_by('id')
        eventos = llamados
        proyecto = Proyecto.objects.filter(id=proyecto_id).first()

        return llamados

    def get_context_data(self, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        eventos = LlamadoProyecto.objects.filter(proyecto_id=proyecto_id).order_by('id')
        proyecto = Proyecto.objects.filter(id=proyecto_id).first()

        context = super().get_context_data(**kwargs)
        context['eventos'] = eventos
        context['proyecto'] = proyecto
        context['inicio'] = str(proyecto.fecha_inicio)
        context['fin'] = str(proyecto.fecha_fin)
        context['titulo'] = 'Eventos'
        context['proyecto_id'] = proyecto_id
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_proyecto', kwargs={'proyecto_id': self.kwargs['proyecto_id']})}
        ]

        return context
