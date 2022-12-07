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
from evento.forms.form_evento_transporte import EventoTransporteForm
from evento.models.evento_transporte import EventoTransporte


class ListadoEventosTransporteView(PermissionRequiredMixin, ListView):
    model = EventoTransporte
    template_name = 'evento_transporte/listado_evento_transporte.html'
    permission = 'evento.view_eventotransporte'

    def get_queryset(self):
        transporte_id = self.kwargs['transporte_id']
        eventos = EventoTransporte.objects.filter(transporte_id=transporte_id).order_by('id')

        return eventos

    def get_context_data(self, **kwargs):
        transporte_id = self.kwargs['transporte_id']
        eventos = EventoTransporte.objects.filter(transporte_id=transporte_id).order_by('id')
        context = super().get_context_data(**kwargs)
        context['eventos'] = eventos
        context['titulo'] = 'Eventos'
        context['transporte_id'] = transporte_id
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Transportes', 'href': reverse_lazy('transportes')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_transporte', kwargs={'transporte_id': self.kwargs['transporte_id']})}
        ]

        return context


class RegistrarEventoTransporteView(PermissionRequiredMixin, CreateView):
    model = EventoTransporte
    template_name = "evento_transporte/form_evento_transporte.html"
    form_class = EventoTransporteForm
    permission = 'evento.add_eventotransporte'

    def get_success_url(self):
        return reverse_lazy('eventos_transporte', kwargs={'transporte_id': self.kwargs['transporte_id']})

    def get_context_data(self, **kwargs):
        transporte_id = self.kwargs['transporte_id']
        context = super(RegistrarEventoTransporteView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar evento'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'evento'
        context['transporte_id'] = transporte_id
        context['icono_form'] = 'plus'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Transportes', 'href': reverse_lazy('transportes')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_transporte', kwargs={'transporte_id': self.kwargs['transporte_id']})},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_evento_transporte', kwargs={'transporte_id': transporte_id})}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        evento = form.save(commit=False)
        transporte_id = self.kwargs['transporte_id']
        evento.transporte_id = transporte_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento agregado con éxito.")
        return super(RegistrarEventoTransporteView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no agregado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarEventoTransporteView(PermissionRequiredMixin, UpdateView):
    model = EventoTransporte
    template_name = "evento_transporte/form_evento_transporte.html"
    form_class = EventoTransporteForm
    permission = 'evento.change_eventotransporte'

    def get_success_url(self):
        return reverse_lazy('eventos_transporte', kwargs={'transporte_id': self.kwargs['transporte_id']})

    def get_context_data(self, **kwargs):
        transporte_id = self.kwargs['transporte_id']
        pk = self.kwargs['pk']
        context = super(ModificarEventoTransporteView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar evento'
        context['titulo_tabla'] = "Modificar"
        context['transporte_id'] = transporte_id
        context['subtitulo_tabla'] = "evento"
        context['icono_form'] = 'edit'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Transportes', 'href': reverse_lazy('transportes')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_transporte', kwargs={'transporte_id': self.kwargs['transporte_id']})},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_evento_transporte', kwargs={'transporte_id': transporte_id, 'pk': pk})},
        ]
        return context

    def form_valid(self, form):
        evento = form.save(commit=False)
        transporte_id = self.kwargs['transporte_id']
        evento.transporte_id = transporte_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento modificado con éxito.")
        return super(ModificarEventoTransporteView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no modificado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarEventoTransporteView(PermissionRequiredMixin, DeleteView):
    permission = 'evento.delete_eventotransporte'

    def get(self, request, *args, **kwargs):
        evento = EventoTransporte.objects.get(id=self.kwargs['pk'])
        evento.delete()
        messages.add_message(request, messages.SUCCESS, "Evento eliminado con éxito.")
        return JsonResponse({})


class HabilitarEventoTransporteView(PermissionRequiredMixin, View):
    permission = 'evento.enable_eventotransporte'

    def get(self, request, *args, **kwargs):
        evento = EventoTransporte.objects.get(id=self.kwargs['pk'])
        evento.activo = True
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarEventoTransporteView(PermissionRequiredMixin, View):
    permission = 'evento.disable_eventotransporte'

    def get(self, request, *args, **kwargs):
        evento = EventoTransporte.objects.get(id=self.kwargs['pk'])
        evento.activo = False
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento deshabilitado con éxito.")
        return JsonResponse({})


class DetallesEventoTransporteView(PermissionRequiredMixin, DetailView):
        template_name = 'evento_transporte/detalles_evento_transporte.html'
        model = EventoTransporte
        permission = 'evento.view_eventotransporte'

        def get_context_data(self, **kwargs):
            transporte_id = self.kwargs['transporte_id']
            context = super(DetallesEventoTransporteView, self).get_context_data(**kwargs)
            context['titulo'] = 'Detalles del evento'
            context['transporte_id'] = transporte_id
            context['titulo_tabla'] = 'Detalles'
            context['activar_eventos'] = True
            context['path'] = [
                {'name': 'Transportes', 'href': reverse_lazy('transportes')},
                {'name': 'Eventos', 'href': reverse_lazy('eventos_transporte', kwargs={'transporte_id': self.kwargs['transporte_id']})},
                {'name': 'Detalles', 'href': reverse_lazy('detalles_evento_transporte', kwargs={'transporte_id': self.kwargs['transporte_id'], 'pk': self.kwargs['pk']})},
            ]
            return context


class EventosTransportePDFView(PermissionRequiredMixin, View):
    permission = 'evento.export_eventostransporte'

    def get(self, request, *args, **kwargs):
        transporte_id = self.kwargs['transporte_id']
        eventos = EventoTransporte.objects.filter(transporte_id=transporte_id).order_by('id')
        template_path = 'pdfs/eventos_transporte_pdf.html'
        if not request.user.has_perm('evento.export_eventostransporte'):
            raise PermissionDenied
        for evento in eventos:
            title = f'Listado de Eventos del Transporte: {evento.transporte.tipo_vehiculo.nombre} de Marca {evento.transporte.marca.nombre}, Modelo {evento.transporte.modelo.nombre} y Color {evento.transporte.color}'
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

