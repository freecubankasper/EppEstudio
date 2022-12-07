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
from evento.forms.form_evento_abastecimiento import EventoAbastecimientoForm
from evento.models.evento_abastecimiento import EventoAbastecimiento


class ListadoEventosAbastecimientoView(PermissionRequiredMixin, ListView):
    model = EventoAbastecimiento
    template_name = 'evento_abastecimiento/listado_evento_abastecimiento.html'
    permission = 'evento.view_eventoabastecimiento'

    def get_queryset(self):
        abastecimiento_id = self.kwargs['abastecimiento_id']
        eventos = EventoAbastecimiento.objects.filter(abastecimiento_id=abastecimiento_id).order_by('id')

        return eventos

    def get_context_data(self, **kwargs):
        abastecimiento_id = self.kwargs['abastecimiento_id']
        eventos = EventoAbastecimiento.objects.filter(abastecimiento_id=abastecimiento_id).order_by('id')
        context = super().get_context_data(**kwargs)
        context['eventos'] = eventos
        context['titulo'] = 'Eventos'
        context['abastecimiento_id'] = abastecimiento_id
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Abastecimientos', 'href': reverse_lazy('abastecimientos')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_abastecimiento', kwargs={'abastecimiento_id': self.kwargs['abastecimiento_id']})}
        ]

        return context


class RegistrarEventoAbastecimientoView(PermissionRequiredMixin, CreateView):
    model = EventoAbastecimiento
    template_name = "evento_abastecimiento/form_evento_abastecimiento.html"
    form_class = EventoAbastecimientoForm
    permission = 'evento.add_eventoabastecimiento'

    def get_success_url(self):
        return reverse_lazy('eventos_abastecimiento', kwargs={'abastecimiento_id': self.kwargs['abastecimiento_id']})

    def get_context_data(self, **kwargs):
        abastecimiento_id = self.kwargs['abastecimiento_id']
        context = super(RegistrarEventoAbastecimientoView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar evento'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'evento'
        context['abastecimiento_id'] = abastecimiento_id
        context['icono_form'] = 'plus'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Abastecimientos', 'href': reverse_lazy('abastecimientos')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_abastecimiento', kwargs={'abastecimiento_id': self.kwargs['abastecimiento_id']})},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_evento_abastecimiento', kwargs={'abastecimiento_id': abastecimiento_id})}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        evento = form.save(commit=False)
        abastecimiento_id = self.kwargs['abastecimiento_id']
        evento.abastecimiento_id = abastecimiento_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento agregado con éxito.")
        return super(RegistrarEventoAbastecimientoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no agregado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarEventoAbastecimientoView(PermissionRequiredMixin, UpdateView):
    model = EventoAbastecimiento
    template_name = "evento_abastecimiento/form_evento_abastecimiento.html"
    form_class = EventoAbastecimientoForm
    permission = 'evento.change_eventoabastecimiento'

    def get_success_url(self):
        return reverse_lazy('eventos_abastecimiento', kwargs={'abastecimiento_id': self.kwargs['abastecimiento_id']})

    def get_context_data(self, **kwargs):
        abastecimiento_id = self.kwargs['abastecimiento_id']
        pk = self.kwargs['pk']
        context = super(ModificarEventoAbastecimientoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar evento'
        context['titulo_tabla'] = "Modificar"
        context['abastecimiento_id'] = abastecimiento_id
        context['subtitulo_tabla'] = "evento"
        context['icono_form'] = 'edit'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Abastecimientos', 'href': reverse_lazy('abastecimientos')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_abastecimiento', kwargs={'abastecimiento_id': self.kwargs['abastecimiento_id']})},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_evento_abastecimiento', kwargs={'abastecimiento_id': abastecimiento_id, 'pk': pk})},
        ]
        return context

    def form_valid(self, form):
        evento = form.save(commit=False)
        abastecimiento_id = self.kwargs['abastecimiento_id']
        evento.abastecimiento_id = abastecimiento_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento modificado con éxito.")
        return super(ModificarEventoAbastecimientoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no modificado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarEventoAbastecimientoView(PermissionRequiredMixin, DeleteView):
    permission = 'evento.delete_eventoabastecimiento'

    def get(self, request, *args, **kwargs):
        evento = EventoAbastecimiento.objects.get(id=self.kwargs['pk'])
        evento.delete()
        messages.add_message(request, messages.SUCCESS, "Evento eliminado con éxito.")
        return JsonResponse({})


class HabilitarEventoAbastecimientoView(PermissionRequiredMixin, View):
    permission = 'evento.enable_eventoabastecimiento'

    def get(self, request, *args, **kwargs):
        evento = EventoAbastecimiento.objects.get(id=self.kwargs['pk'])
        evento.activo = True
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarEventoAbastecimientoView(PermissionRequiredMixin, View):
    permission = 'evento.disable_eventoabastecimiento'

    def get(self, request, *args, **kwargs):
        evento = EventoAbastecimiento.objects.get(id=self.kwargs['pk'])
        evento.activo = False
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento deshabilitado con éxito.")
        return JsonResponse({})


class DetallesEventoAbastecimientoView(PermissionRequiredMixin, DetailView):
        template_name = 'evento_abastecimiento/detalles_evento_abastecimiento.html'
        model = EventoAbastecimiento
        permission = 'evento.view_eventoabastecimiento'

        def get_context_data(self, **kwargs):
            abastecimiento_id = self.kwargs['abastecimiento_id']
            context = super(DetallesEventoAbastecimientoView, self).get_context_data(**kwargs)
            context['titulo'] = 'Detalles del evento'
            context['abastecimiento_id'] = abastecimiento_id
            context['titulo_tabla'] = 'Detalles'
            context['activar_eventos'] = True
            context['path'] = [
                {'name': 'Abastecimientos', 'href': reverse_lazy('abastecimientos')},
                {'name': 'Eventos', 'href': reverse_lazy('eventos_abastecimiento', kwargs={'abastecimiento_id': self.kwargs['abastecimiento_id']})},
                {'name': 'Detalles', 'href': reverse_lazy('detalles_evento_abastecimiento', kwargs={'abastecimiento_id': self.kwargs['abastecimiento_id'], 'pk': self.kwargs['pk']})},
            ]
            return context


class EventosAbastecimientoPDFView(PermissionRequiredMixin, View):
    permission = 'evento.export_eventosabastecimiento'

    def get(self, request, *args, **kwargs):
        abastecimiento_id = self.kwargs['abastecimiento_id']
        eventos = EventoAbastecimiento.objects.filter(abastecimiento_id=abastecimiento_id).order_by('id')
        template_path = 'pdfs/eventos_abastecimiento_pdf.html'
        if not request.user.has_perm('evento.export_eventosabastecimiento'):
            raise PermissionDenied
        for evento in eventos:
            title = f'Listado de Eventos del Abastecimiento {evento.abastecimiento.nombre}'
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

