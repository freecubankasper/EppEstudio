import datetime
import os

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView, DeleteView

from actor.models.actor import Actor
from core.utiles.filters import EquipamientoFilter, CarrosFilter, ActorFilter
from core.utiles.permission_required import PermissionRequiredMixin
from epp import settings
from equipamiento.models.equipamiento import Equipamiento
from equipo_proteccion_personal.utiles.pdfs import to_base64
from evento.forms.form_evento_proyecto import EventoProyectoForm
from evento.models.evento_actor import EventoActor
from evento.models.evento_equipamiento import EventoEquipamiento
from evento.models.evento_proyecto import EventoProyecto
from llamado.models.llamado_proyecto import LlamadoProyecto
from proyecto.models import Proyecto
from transporte.models.transporte import Transporte
from django import template
register = template.Library()
class ListadoEventosProyectoView(PermissionRequiredMixin, ListView):
    model = EventoProyecto
    template_name = 'evento_proyecto/listado_evento_proyecto.html'
    permission = 'evento.view_eventoproyecto'

    def get_queryset(self):
        llamado_id = self.kwargs['llamado_id']
        eventos = EventoProyecto.objects.filter(llamado_id=llamado_id).order_by('id')

        return eventos

    def get_context_data(self, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        llamado_id = self.kwargs['llamado_id']
        eventos = EventoProyecto.objects.filter(llamado_id=llamado_id).order_by('id')
        context = super().get_context_data(**kwargs)
        context['eventos'] = eventos
        context['titulo'] = 'Eventos'
        context['proyecto_id'] = proyecto_id
        context['llamado_id'] = llamado_id
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')},
            {'name': 'Llamados', 'href': reverse_lazy('llamados_proyecto', kwargs={'proyecto_id': proyecto_id})},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_proyecto', kwargs={'proyecto_id': proyecto_id, 'llamado_id': llamado_id})}
        ]

        return context

class RegistrarEventoProyectoCalendarioView(PermissionRequiredMixin, ListView):
    model = Equipamiento
    template_name = "evento_proyecto/form_evento_proyecto_calendario.html"
    form_class = EventoProyectoForm
    permission = 'evento.add_eventoproyecto'

    def get_context_data(self, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        elemento_id=1
        precio=0
        proyecto= Proyecto.objects.filter(id=proyecto_id).first()
        llamado_id = self.kwargs['llamado_id']
        equipamientos_seleccionados = EventoEquipamiento.objects.filter(llamado__id=llamado_id)
        talentos_seleccionados = EventoActor.objects.filter(llamado__id=llamado_id)
        contador = equipamientos_seleccionados.count()
        contador =contador + talentos_seleccionados.count()
        llamado= LlamadoProyecto.objects.filter(id=proyecto_id).first()
        context = super(RegistrarEventoProyectoCalendarioView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['talentos_seleccionados'] = talentos_seleccionados
        context['equipamientos'] = EquipamientoFilter(self.request.GET,queryset=self.get_queryset())
        context['elemento_id'] = elemento_id
        context['precio'] = precio
        context['proyecto_id'] = proyecto_id
        context['llamado_id'] = llamado_id
        context['contador'] = contador
        context['proyecto'] = proyecto
        context['llamado'] = llamado
        return context

class RegistrarEventoLlamadoCalendarioView(PermissionRequiredMixin, ListView):
    model = Equipamiento
    template_name = "evento_proyecto/form_eventos_llamado_calendario.html"
    form_class = EventoProyectoForm
    permission = 'evento.add_eventoproyecto'

    def get_context_data(self, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        elemento_id=1
        precio=0
        proyecto= Proyecto.objects.filter(id=proyecto_id).first()
        llamado_id = self.kwargs['llamado_id']
        equipamientos_seleccionados = EventoEquipamiento.objects.filter(llamado__id=llamado_id)
        talentos_seleccionados = EventoActor.objects.filter(llamado__id=llamado_id)
        contador = equipamientos_seleccionados.count()
        contador =contador + talentos_seleccionados.count()
        llamado= LlamadoProyecto.objects.filter(id=proyecto_id).first()
        for equipamientos_seleccionado in equipamientos_seleccionados:
            precio=precio+equipamientos_seleccionado.precio_mlc_acumulado
        for talentos_seleccionado in talentos_seleccionados:
            precio=precio+talentos_seleccionado.precio_mlc_acumulado
        context = super(RegistrarEventoLlamadoCalendarioView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['equipamientos_seleccionados'] = equipamientos_seleccionados
        context['talentos_seleccionados'] = talentos_seleccionados
        context['equipamientos'] = EquipamientoFilter(self.request.GET,queryset=self.get_queryset())
        context['elemento_id'] = elemento_id
        context['precio'] = precio
        context['contador'] = contador
        context['proyecto_id'] = proyecto_id
        context['llamado_id'] = llamado_id
        context['proyecto'] = proyecto
        context['llamado'] = llamado
        return context

class RegistrarEventoEquipamientoCalendarioView(PermissionRequiredMixin, ListView):
    model = Equipamiento
    template_name = "evento_proyecto/form_evento_equipamiento_calendario.html"
    form_class = EventoProyectoForm
    permission = 'evento.add_eventoproyecto'

    def get_context_data(self, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        elemento_id=1
        proyecto= Proyecto.objects.filter(id=proyecto_id).first()
        llamado_id = self.kwargs['llamado_id']
        llamado= LlamadoProyecto.objects.filter(id=proyecto_id).first()
        context = super(RegistrarEventoEquipamientoCalendarioView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['equipamientos'] = EquipamientoFilter(self.request.GET,queryset=self.get_queryset())
        context['elemento_id'] = elemento_id
        context['proyecto_id'] = proyecto_id
        context['llamado_id'] = llamado_id
        context['proyecto'] = proyecto
        context['llamado'] = llamado
        return context

class RegistrarEventoTalentCalendarioView(PermissionRequiredMixin, ListView):
    model = Actor
    template_name = "evento_proyecto/form_evento_talent_calendario.html"
    form_class = EventoProyectoForm
    permission = 'evento.add_eventoproyecto'

    def get_context_data(self, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        elemento_id=1
        proyecto= Proyecto.objects.filter(id=proyecto_id).first()
        llamado_id = self.kwargs['llamado_id']
        llamado= LlamadoProyecto.objects.filter(id=proyecto_id).first()
        context = super(RegistrarEventoTalentCalendarioView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['talento'] = ActorFilter(self.request.GET,queryset=self.get_queryset())
        context['elemento_id'] = elemento_id
        context['proyecto_id'] = proyecto_id
        context['llamado_id'] = llamado_id
        context['proyecto'] = proyecto
        context['llamado'] = llamado
        return context
class RegistrarEventoTransporteCalendarioView(PermissionRequiredMixin, ListView):
    model = Transporte
    template_name = "evento_proyecto/form_evento_transporte_calendario.html"
    form_class = EventoProyectoForm
    permission = 'evento.add_eventoproyecto'

    def get_context_data(self, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        elemento_id=1
        proyecto= Proyecto.objects.filter(id=proyecto_id).first()
        llamado_id = self.kwargs['llamado_id']
        llamado= LlamadoProyecto.objects.filter(id=proyecto_id).first()
        context = super(RegistrarEventoTransporteCalendarioView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['transporte'] = CarrosFilter(self.request.GET,queryset=self.get_queryset())
        context['elemento_id'] = elemento_id
        context['proyecto_id'] = proyecto_id
        context['llamado_id'] = llamado_id
        context['proyecto'] = proyecto
        context['llamado'] = llamado
        return context

class RegistrarEventoProyectoView(PermissionRequiredMixin, CreateView):
    model = EventoProyecto
    template_name = "evento_proyecto/form_evento_proyecto.html"
    form_class = EventoProyectoForm
    permission = 'evento.add_eventoproyecto'

    def get_success_url(self):
        return reverse_lazy('eventos_proyecto', kwargs={'proyecto_id': self.kwargs['proyecto_id'], 'llamado_id': self.kwargs['llamado_id']})

    def get_context_data(self, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        llamado_id = self.kwargs['llamado_id']
        context = super(RegistrarEventoProyectoView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar evento'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'evento'
        context['proyecto_id'] = proyecto_id
        context['llamado_id'] = llamado_id
        context['icono_form'] = 'plus'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')},
            {'name': 'Llamados', 'href': reverse_lazy('llamados_proyecto', kwargs={'proyecto_id': proyecto_id})},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_proyecto', kwargs={'proyecto_id': proyecto_id, 'llamado_id': llamado_id})},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_evento_proyecto', kwargs={'proyecto_id': proyecto_id, 'llamado_id': llamado_id})}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        evento = form.save(commit=False)
        llamado_id = self.kwargs['llamado_id']
        evento.llamado_id = llamado_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento agregado con éxito.")
        return super(RegistrarEventoProyectoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no agregado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarEventoProyectoView(PermissionRequiredMixin, UpdateView):
    model = EventoProyecto
    template_name = "evento_proyecto/form_evento_proyecto.html"
    form_class = EventoProyectoForm
    permission = 'evento.change_eventoproyecto'

    def get_success_url(self):
        return reverse_lazy('eventos_proyecto', kwargs={'proyecto_id': self.kwargs['proyecto_id'], 'llamado_id': self.kwargs['llamado_id']})

    def get_context_data(self, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        llamado_id = self.kwargs['llamado_id']
        pk = self.kwargs['pk']
        context = super(ModificarEventoProyectoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar evento'
        context['titulo_tabla'] = "Modificar"
        context['proyecto_id'] = proyecto_id
        context['llamado_id'] = llamado_id
        context['subtitulo_tabla'] = "evento"
        context['icono_form'] = 'edit'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')},
            {'name': 'Llamados', 'href': reverse_lazy('llamados_proyecto', kwargs={'proyecto_id': proyecto_id})},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_proyecto', kwargs={'proyecto_id': proyecto_id, 'llamado_id': llamado_id})},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_evento_proyecto', kwargs={'proyecto_id': proyecto_id, 'llamado_id': llamado_id, 'pk': pk})},
        ]
        return context

    def form_valid(self, form):
        evento = form.save(commit=False)
        llamado_id = self.kwargs['llamado_id']
        evento.llamado_id = llamado_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento modificado con éxito.")
        return super(ModificarEventoProyectoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no modificado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarEventoProyectoView(PermissionRequiredMixin, DeleteView):
    permission = 'evento.delete_eventoproyecto'

    def get(self, request, *args, **kwargs):
        evento = EventoProyecto.objects.get(id=self.kwargs['pk'])
        evento.delete()
        messages.add_message(request, messages.SUCCESS, "Evento eliminado con éxito.")
        return JsonResponse({})


class HabilitarEventoProyectoView(PermissionRequiredMixin, View):
    permission = 'evento.enable_eventoproyecto'

    def get(self, request, *args, **kwargs):
        evento = EventoProyecto.objects.get(id=self.kwargs['pk'])
        evento.activo = True
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarEventoProyectoView(PermissionRequiredMixin, View):
    permission = 'evento.disable_eventoproyecto'

    def get(self, request, *args, **kwargs):
        evento = EventoProyecto.objects.get(id=self.kwargs['pk'])
        evento.activo = False
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento deshabilitado con éxito.")
        return JsonResponse({})


class DetallesEventoProyectoView(PermissionRequiredMixin, DetailView):
        template_name = 'evento_proyecto/detalles_evento_proyecto.html'
        model = EventoProyecto
        permission = 'evento.view_eventoproyecto'

        def get_context_data(self, **kwargs):
            proyecto_id = self.kwargs['proyecto_id']
            llamado_id = self.kwargs['llamado_id']
            pk = self.kwargs['pk']
            context = super(DetallesEventoProyectoView, self).get_context_data(**kwargs)
            context['titulo'] = 'Detalles del evento'
            context['proyecto_id'] = proyecto_id
            context['llamado_id'] = llamado_id
            context['titulo_tabla'] = 'Detalles'
            context['activar_eventos'] = True
            context['path'] = [
                {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')},
                {'name': 'Llamados', 'href': reverse_lazy('llamados_proyecto', kwargs={'proyecto_id': proyecto_id})},
                {'name': 'Eventos', 'href': reverse_lazy('eventos_proyecto', kwargs={'proyecto_id': proyecto_id, 'llamado_id': llamado_id})},
                {'name': 'Detalles', 'href': reverse_lazy('detalles_evento_proyecto', kwargs={'proyecto_id': proyecto_id, 'llamado_id': llamado_id, 'pk': pk})},
            ]
            return context


class EventosProyectoPDFView(PermissionRequiredMixin, View):
    permission = 'evento.export_eventosproyecto'

    def get(self, request, *args, **kwargs):
        llamado_id = self.kwargs['llamado_id']
        eventos = EventoProyecto.objects.filter(llamado_id=llamado_id).order_by('id')
        template_path = 'pdfs/eventos_proyecto_pdf.html'
        if not request.user.has_perm('evento.export_eventosproyecto'):
            raise PermissionDenied
        for evento in eventos:
            title = f'Listado de Eventos del Llamado {evento.llamado.titulo}'
            data = {
                'title': title,
                'eventos': eventos,
                'header': to_base64(os.path.join(settings.BASE_DIR, 'static', 'assets', 'base', 'img', 'layout', 'logos', 'logo-5.png')),
                'PROD': settings.PRODUCTION,

            }
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{title}.pdf"'
            template = get_template(template_path)
            html = template.render(data)

            # create a pdf

            return response

