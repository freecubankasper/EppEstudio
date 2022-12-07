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


from core.utiles.permission_required import PermissionRequiredMixin
from epp import settings
from equipo_proteccion_personal.utiles.pdfs import to_base64
from evento.forms.form_evento_especialista import EventoEspecialistaForm
from evento.models.evento_especialista import EventoEspecialista


class ListadoEventosEspecialistaView(PermissionRequiredMixin, ListView):
    model = EventoEspecialista
    template_name = 'evento_especialista/listado_evento_especialista.html'
    permission = 'evento.view_eventoespecialista'

    def get_queryset(self):
        especialista_id = self.kwargs['especialista_id']
        eventos = EventoEspecialista.objects.filter(especialista_id=especialista_id).order_by('id')

        return eventos

    def get_context_data(self, **kwargs):
        especialista_id = self.kwargs['especialista_id']
        eventos = EventoEspecialista.objects.filter(especialista_id=especialista_id).order_by('id')
        context = super().get_context_data(**kwargs)
        context['eventos'] = eventos
        context['titulo'] = 'Eventos'
        context['especialista_id'] = especialista_id
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Especialistas', 'href': reverse_lazy('especialistas')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_especialista', kwargs={'especialista_id': self.kwargs['especialista_id']})}
        ]

        return context


class RegistrarEventoEspecialistaView(PermissionRequiredMixin, CreateView):
    model = EventoEspecialista
    template_name = "evento_especialista/form_evento_especialista.html"
    form_class = EventoEspecialistaForm
    permission = 'evento.add_eventoespecialista'

    def get_success_url(self):
        return reverse_lazy('eventos_especialista', kwargs={'especialista_id': self.kwargs['especialista_id']})

    def get_context_data(self, **kwargs):
        especialista_id = self.kwargs['especialista_id']
        context = super(RegistrarEventoEspecialistaView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar evento'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'evento'
        context['especialista_id'] = especialista_id
        context['icono_form'] = 'plus'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Especialistas', 'href': reverse_lazy('especialistas')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_especialista', kwargs={'especialista_id': self.kwargs['especialista_id']})},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_evento_especialista', kwargs={'especialista_id': especialista_id})}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        evento = form.save(commit=False)
        especialista_id = self.kwargs['especialista_id']
        evento.especialista_id = especialista_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento agregado con éxito.")
        return super(RegistrarEventoEspecialistaView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no agregado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarEventoEspecialistaView(PermissionRequiredMixin, UpdateView):
    model = EventoEspecialista
    template_name = "evento_especialista/form_evento_especialista.html"
    form_class = EventoEspecialistaForm
    permission = 'evento.change_eventoespecialista'

    def get_success_url(self):
        return reverse_lazy('eventos_especialista', kwargs={'especialista_id': self.kwargs['especialista_id']})

    def get_context_data(self, **kwargs):
        especialista_id = self.kwargs['especialista_id']
        pk = self.kwargs['pk']
        context = super(ModificarEventoEspecialistaView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar evento'
        context['titulo_tabla'] = "Modificar"
        context['especialista_id'] = especialista_id
        context['subtitulo_tabla'] = "evento"
        context['icono_form'] = 'edit'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Especialistas', 'href': reverse_lazy('especialistas')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_especialista', kwargs={'especialista_id': self.kwargs['especialista_id']})},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_evento_especialista', kwargs={'especialista_id': especialista_id, 'pk': pk})},
        ]
        return context

    def form_valid(self, form):
        evento = form.save(commit=False)
        especialista_id = self.kwargs['especialista_id']
        evento.especialista_id = especialista_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento modificado con éxito.")
        return super(ModificarEventoEspecialistaView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no modificado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarEventoEspecialistaView(PermissionRequiredMixin, DeleteView):
    permission = 'evento.delete_eventoespecialista'

    def get(self, request, *args, **kwargs):
        evento = EventoEspecialista.objects.get(id=self.kwargs['pk'])
        evento.delete()
        messages.add_message(request, messages.SUCCESS, "Evento eliminado con éxito.")
        return JsonResponse({})


class HabilitarEventoEspecialistaView(PermissionRequiredMixin, View):
    permission = 'evento.enable_eventoespecialista'

    def get(self, request, *args, **kwargs):
        evento = EventoEspecialista.objects.get(id=self.kwargs['pk'])
        evento.activo = True
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarEventoEspecialistaView(PermissionRequiredMixin, View):
    permission = 'evento.disable_eventoespecialista'

    def get(self, request, *args, **kwargs):
        evento = EventoEspecialista.objects.get(id=self.kwargs['pk'])
        evento.activo = False
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento deshabilitado con éxito.")
        return JsonResponse({})


class DetallesEventoEspecialistaView(PermissionRequiredMixin, DetailView):
        template_name = 'evento_especialista/detalles_evento_especialista.html'
        model = EventoEspecialista
        permission = 'evento.view_eventoespecialista'

        def get_context_data(self, **kwargs):
            especialista_id = self.kwargs['especialista_id']
            context = super(DetallesEventoEspecialistaView, self).get_context_data(**kwargs)
            context['titulo'] = 'Detalles del evento'
            context['especialista_id'] = especialista_id
            context['titulo_tabla'] = 'Detalles'
            context['activar_eventos'] = True
            context['path'] = [
                {'name': 'Especialistas', 'href': reverse_lazy('especialistas')},
                {'name': 'Eventos', 'href': reverse_lazy('eventos_especialista', kwargs={'especialista_id': self.kwargs['especialista_id']})},
                {'name': 'Detalles', 'href': reverse_lazy('detalles_evento_especialista', kwargs={'especialista_id': self.kwargs['especialista_id'], 'pk': self.kwargs['pk']})},
            ]
            return context


class EventosEspecialistaPDFView(PermissionRequiredMixin, View):
    permission = 'evento.export_eventosespecialista'

    def get(self, request, *args, **kwargs):
        especialista_id = self.kwargs['especialista_id']
        eventos = EventoEspecialista.objects.filter(especialista_id=especialista_id).order_by('id')
        template_path = 'pdfs/eventos_especialista_pdf.html'
        if not request.user.has_perm('evento.export_eventosespecialista'):
            raise PermissionDenied
        for evento in eventos:
            title = f'Listado de Eventos del Especialista {evento.especialista.primer_nombre} {evento.especialista.segundo_nombre if evento.especialista.segundo_nombre else ""} {evento.especialista.primer_apellido} {evento.especialista.segundo_apellido}'
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

