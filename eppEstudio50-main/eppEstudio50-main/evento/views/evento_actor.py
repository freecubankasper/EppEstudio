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
from evento.forms.form_evento_actor import EventoActorForm
from evento.models.evento_actor import EventoActor


class ListadoEventosActorView(PermissionRequiredMixin, ListView):
    model = EventoActor
    template_name = 'evento_actor/listado_evento_actor.html'
    permission = 'evento.view_eventoactor'

    def get_queryset(self):
        actor_id = self.kwargs['actor_id']
        eventos = EventoActor.objects.filter(actor_id=actor_id).order_by('id')

        return eventos

    def get_context_data(self, **kwargs):
        actor_id = self.kwargs['actor_id']
        eventos = EventoActor.objects.filter(actor_id=actor_id).order_by('id')
        context = super().get_context_data(**kwargs)
        context['eventos'] = eventos
        context['titulo'] = 'Eventos'
        context['actor_id'] = actor_id
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Actores', 'href': reverse_lazy('actores')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_actor', kwargs={'actor_id': self.kwargs['actor_id']})}
        ]

        return context


class RegistrarEventoActorView(PermissionRequiredMixin, CreateView):
    model = EventoActor
    template_name = "evento_actor/form_evento_actor.html"
    form_class = EventoActorForm
    permission = 'evento.add_eventoactor'

    def get_success_url(self):
        return reverse_lazy('eventos_actor', kwargs={'actor_id': self.kwargs['actor_id']})

    def get_context_data(self, **kwargs):
        actor_id = self.kwargs['actor_id']
        context = super(RegistrarEventoActorView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar evento'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'evento'
        context['actor_id'] = actor_id
        context['icono_form'] = 'plus'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Actores', 'href': reverse_lazy('actores')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_actor', kwargs={'actor_id': self.kwargs['actor_id']})},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_evento_actor', kwargs={'actor_id': actor_id})}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        evento = form.save(commit=False)
        actor_id = self.kwargs['actor_id']
        evento.actor_id = actor_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento agregado con éxito.")
        return super(RegistrarEventoActorView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no agregado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarEventoActorView(PermissionRequiredMixin, UpdateView):
    model = EventoActor
    template_name = "evento_actor/form_evento_actor.html"
    form_class = EventoActorForm
    permission = 'evento.change_eventoactor'

    def get_success_url(self):
        return reverse_lazy('eventos_actor', kwargs={'actor_id': self.kwargs['actor_id']})

    def get_context_data(self, **kwargs):
        actor_id = self.kwargs['actor_id']
        pk = self.kwargs['pk']
        context = super(ModificarEventoActorView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar evento'
        context['titulo_tabla'] = "Modificar"
        context['actor_id'] = actor_id
        context['subtitulo_tabla'] = "evento"
        context['icono_form'] = 'edit'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Actores', 'href': reverse_lazy('actores')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_actor', kwargs={'actor_id': self.kwargs['actor_id']})},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_evento_actor', kwargs={'actor_id': actor_id, 'pk': pk})},
        ]
        return context

    def form_valid(self, form):
        evento = form.save(commit=False)
        actor_id = self.kwargs['actor_id']
        evento.actor_id = actor_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento modificado con éxito.")
        return super(ModificarEventoActorView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no modificado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarEventoActorView(PermissionRequiredMixin, DeleteView):
    permission = 'evento.delete_eventoactor'

    def get(self, request, *args, **kwargs):
        evento = EventoActor.objects.get(id=self.kwargs['pk'])
        evento.delete()
        messages.add_message(request, messages.SUCCESS, "Evento eliminado con éxito.")
        return JsonResponse({})


class HabilitarEventoActorView(PermissionRequiredMixin, View):
    permission = 'evento.enable_eventoactor'

    def get(self, request, *args, **kwargs):
        evento = EventoActor.objects.get(id=self.kwargs['pk'])
        evento.activo = True
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarEventoActorView(PermissionRequiredMixin, View):
    permission = 'evento.disable_eventoactor'

    def get(self, request, *args, **kwargs):
        evento = EventoActor.objects.get(id=self.kwargs['pk'])
        evento.activo = False
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento deshabilitado con éxito.")
        return JsonResponse({})


class DetallesEventoActorView(PermissionRequiredMixin, DetailView):
        template_name = 'evento_actor/detalles_evento_actor.html'
        model = EventoActor
        permission = 'evento.view_eventoactor'

        def get_context_data(self, **kwargs):
            actor_id = self.kwargs['actor_id']
            context = super(DetallesEventoActorView, self).get_context_data(**kwargs)
            context['titulo'] = 'Detalles del evento'
            context['actor_id'] = actor_id
            context['titulo_tabla'] = 'Detalles'
            context['activar_eventos'] = True
            context['path'] = [
                {'name': 'Actores', 'href': reverse_lazy('actores')},
                {'name': 'Eventos', 'href': reverse_lazy('eventos_actor', kwargs={'actor_id': self.kwargs['actor_id']})},
                {'name': 'Detalles', 'href': reverse_lazy('detalles_evento_actor', kwargs={'actor_id': self.kwargs['actor_id'], 'pk': self.kwargs['pk']})},
            ]
            return context


class EventosActorPDFView(PermissionRequiredMixin, View):
    permission = 'evento.export_eventosactor'

    def get(self, request, *args, **kwargs):
        actor_id = self.kwargs['actor_id']
        eventos = EventoActor.objects.filter(actor_id=actor_id).order_by('id')
        template_path = 'pdfs/eventos_actor_pdf.html'
        if not request.user.has_perm('evento.export_eventosactor'):
            raise PermissionDenied
        for evento in eventos:
            title = f'Listado de Eventos del Actor {evento.actor.primer_nombre} {evento.actor.segundo_nombre if evento.actor.segundo_nombre else ""} {evento.actor.primer_apellido} {evento.actor.segundo_apellido}'
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

