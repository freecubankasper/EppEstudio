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
from evento.forms.form_evento_locacion import EventoLocacionForm
from evento.models.evento_locacion import EventoLocacion


class ListadoEventosLocacionView(PermissionRequiredMixin, ListView):
    model = EventoLocacion
    template_name = 'evento_locacion/listado_evento_locacion.html'
    permission = 'evento.view_eventolocacion'

    def get_queryset(self):
        locacion_id = self.kwargs['locacion_id']
        eventos = EventoLocacion.objects.filter(locacion_id=locacion_id).order_by('id')

        return eventos

    def get_context_data(self, **kwargs):
        locacion_id = self.kwargs['locacion_id']
        eventos = EventoLocacion.objects.filter(locacion_id=locacion_id).order_by('id')
        context = super().get_context_data(**kwargs)
        context['eventos'] = eventos
        context['titulo'] = 'Eventos'
        context['locacion_id'] = locacion_id
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Locaciones', 'href': reverse_lazy('locaciones')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_locacion', kwargs={'locacion_id': self.kwargs['locacion_id']})}
        ]

        return context


class RegistrarEventoLocacionView(PermissionRequiredMixin, CreateView):
    model = EventoLocacion
    template_name = "evento_locacion/form_evento_locacion.html"
    form_class = EventoLocacionForm
    permission = 'evento.add_eventolocacion'

    def get_success_url(self):
        return reverse_lazy('eventos_locacion', kwargs={'locacion_id': self.kwargs['locacion_id']})

    def get_context_data(self, **kwargs):
        locacion_id = self.kwargs['locacion_id']
        context = super(RegistrarEventoLocacionView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar evento'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'evento'
        context['locacion_id'] = locacion_id
        context['icono_form'] = 'plus'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Locaciones', 'href': reverse_lazy('locaciones')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_locacion', kwargs={'locacion_id': self.kwargs['locacion_id']})},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_evento_locacion', kwargs={'locacion_id': locacion_id})}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        evento = form.save(commit=False)
        locacion_id = self.kwargs['locacion_id']
        evento.locacion_id = locacion_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento agregado con éxito.")
        return super(RegistrarEventoLocacionView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no agregado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarEventoLocacionView(PermissionRequiredMixin, UpdateView):
    model = EventoLocacion
    template_name = "evento_locacion/form_evento_locacion.html"
    form_class = EventoLocacionForm
    permission = 'evento.change_eventolocacion'

    def get_success_url(self):
        return reverse_lazy('eventos_locacion', kwargs={'locacion_id': self.kwargs['locacion_id']})

    def get_context_data(self, **kwargs):
        locacion_id = self.kwargs['locacion_id']
        pk = self.kwargs['pk']
        context = super(ModificarEventoLocacionView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar evento'
        context['titulo_tabla'] = "Modificar"
        context['locacion_id'] = locacion_id
        context['subtitulo_tabla'] = "evento"
        context['icono_form'] = 'edit'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Locaciones', 'href': reverse_lazy('locaciones')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_locacion', kwargs={'locacion_id': self.kwargs['locacion_id']})},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_evento_locacion', kwargs={'locacion_id': locacion_id, 'pk': pk})},
        ]
        return context

    def form_valid(self, form):
        evento = form.save(commit=False)
        locacion_id = self.kwargs['locacion_id']
        evento.locacion_id = locacion_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento modificado con éxito.")
        return super(ModificarEventoLocacionView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no modificado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarEventoLocacionView(PermissionRequiredMixin, DeleteView):
    permission = 'evento.delete_eventolocacion'

    def get(self, request, *args, **kwargs):
        evento = EventoLocacion.objects.get(id=self.kwargs['pk'])
        evento.delete()
        messages.add_message(request, messages.SUCCESS, "Evento eliminado con éxito.")
        return JsonResponse({})


class HabilitarEventoLocacionView(PermissionRequiredMixin, View):
    permission = 'evento.enable_eventolocacion'

    def get(self, request, *args, **kwargs):
        evento = EventoLocacion.objects.get(id=self.kwargs['pk'])
        evento.activo = True
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarEventoLocacionView(PermissionRequiredMixin, View):
    permission = 'evento.disable_eventolocacion'

    def get(self, request, *args, **kwargs):
        evento = EventoLocacion.objects.get(id=self.kwargs['pk'])
        evento.activo = False
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento deshabilitado con éxito.")
        return JsonResponse({})


class DetallesEventoLocacionView(PermissionRequiredMixin, DetailView):
        template_name = 'evento_locacion/detalles_evento_locacion.html'
        model = EventoLocacion
        permission = 'evento.view_eventolocacion'

        def get_context_data(self, **kwargs):
            locacion_id = self.kwargs['locacion_id']
            context = super(DetallesEventoLocacionView, self).get_context_data(**kwargs)
            context['titulo'] = 'Detalles del evento'
            context['locacion_id'] = locacion_id
            context['titulo_tabla'] = 'Detalles'
            context['activar_eventos'] = True
            context['path'] = [
                {'name': 'Locaciones', 'href': reverse_lazy('locaciones')},
                {'name': 'Eventos', 'href': reverse_lazy('eventos_locacion', kwargs={'locacion_id': self.kwargs['locacion_id']})},
                {'name': 'Detalles', 'href': reverse_lazy('detalles_evento_locacion', kwargs={'locacion_id': self.kwargs['locacion_id'], 'pk': self.kwargs['pk']})},
            ]
            return context


class EventosLocacionPDFView(PermissionRequiredMixin, View):
    permission = 'evento.export_eventoslocacion'

    def get(self, request, *args, **kwargs):
        locacion_id = self.kwargs['locacion_id']
        eventos = EventoLocacion.objects.filter(locacion_id=locacion_id).order_by('id')
        template_path = 'pdfs/eventos_locacion_pdf.html'
        if not request.user.has_perm('evento.export_eventoslocacion'):
            raise PermissionDenied
        for evento in eventos:
            title = f'Listado de Eventos de la Locación {evento.locacion.nombre}'
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

