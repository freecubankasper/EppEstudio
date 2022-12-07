import datetime
import os

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView, DeleteView

from actor.models.actor import Actor
from core.utiles.permission_required import PermissionRequiredMixin
from epp import settings
from equipamiento.models.equipamiento import Equipamiento
from equipo_proteccion_personal.utiles.pdfs import to_base64
from evento.forms.form_evento_equipamiento import EventoEquipamientoForm
from evento.models.evento_actor import EventoActor
from evento.models.evento_equipamiento import EventoEquipamiento
from llamado.models.llamado_proyecto import LlamadoProyecto


class ListadoEventosEquipamientoView(PermissionRequiredMixin, ListView):
    model = EventoEquipamiento
    template_name = 'evento_equipamiento/listado_evento_equipamiento.html'
    permission = 'evento.view_eventoequipamiento'

    def get_queryset(self):
        equipamiento_id = self.kwargs['equipamiento_id']
        eventos = EventoEquipamiento.objects.filter(equipamiento_id=equipamiento_id).order_by('id')

        return eventos

    def get_context_data(self, **kwargs):
        equipamiento_id = self.kwargs['equipamiento_id']
        eventos = EventoEquipamiento.objects.filter(equipamiento_id=equipamiento_id).order_by('id')
        context = super().get_context_data(**kwargs)
        context['eventos'] = eventos
        context['titulo'] = 'Eventos'
        context['equipamiento_id'] = equipamiento_id
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Equipamientos', 'href': reverse_lazy('equipamientos')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_equipamiento', kwargs={'equipamiento_id': self.kwargs['equipamiento_id']})}
        ]

        return context


class RegistrarEventoEquipamientoView(PermissionRequiredMixin, CreateView):
    model = EventoEquipamiento
    template_name = "evento_equipamiento/form_evento_equipamiento.html"
    form_class = EventoEquipamientoForm
    permission = 'evento.add_eventoequipamiento'

    def get_success_url(self):
        return reverse_lazy('eventos_equipamiento', kwargs={'equipamiento_id': self.kwargs['equipamiento_id']})

    def get_context_data(self, **kwargs):
        equipamiento_id = self.kwargs['equipamiento_id']
        context = super(RegistrarEventoEquipamientoView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar evento'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'evento'
        context['equipamiento_id'] = equipamiento_id
        context['icono_form'] = 'plus'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Equipamientos', 'href': reverse_lazy('equipamientos')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_equipamiento', kwargs={'equipamiento_id': self.kwargs['equipamiento_id']})},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_evento_equipamiento', kwargs={'equipamiento_id': equipamiento_id})}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        evento = form.save(commit=False)
        equipamiento_id = self.kwargs['equipamiento_id']
        evento.equipamiento_id = equipamiento_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento agregado con éxito.")
        return super(RegistrarEventoEquipamientoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no agregado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class RegistrarEventoEquipamientoLlamadoView(TemplateView):
    def post(self, request, *args, **kwargs):
        if self.request.method=='POST':
            llamado_id = self.kwargs['llamado_id']
            llamado = LlamadoProyecto.objects.filter(id=llamado_id).first()
            eventos = EventoEquipamiento.objects.filter(llamado_id=llamado).first()
            nombre = request.POST.get('evento_nombre')
            equipamiento = request.POST.get('documento_seleccionado')
            equipamiento= Equipamiento.objects.filter(id=equipamiento).first()
            cantidad = request.POST.get('proyecto_cantidad')
            descripcion = request.POST.get('evento_descripcion')
            fecha_inicio_evento = request.POST.get('id_fecha_inicio')
            fecha_fin_evento = request.POST.get('id_fecha_fin')
            observaciones = ''
            precio=0
            if(llamado.tipo_pago=='medio_llamado'):
                precio=equipamiento.precio_mlc * int(cantidad)
            if (llamado.tipo_pago == 'llamado_completo'):
                precio = equipamiento.precio_mlc * 2 * int(cantidad)

            evento = EventoEquipamiento.objects.create(titulo=nombre, cantidad=cantidad,descripcion=descripcion,llamado=llamado,
                                                        fecha_inicio_evento=fecha_inicio_evento,fecha_fin_evento=fecha_fin_evento,
                                                        equipamiento=equipamiento,precio_mlc_acumulado=precio)



            return HttpResponseRedirect(reverse_lazy('registrar_evento_proyecto_calendario',
                                kwargs={'proyecto_id': evento.llamado.proyecto.id, 'llamado_id': evento.llamado.id}))

        raise PermissionDenied


class ModificarEventoEquipamientoView(PermissionRequiredMixin, UpdateView):
    model = EventoEquipamiento
    template_name = "evento_equipamiento/form_evento_equipamiento.html"
    form_class = EventoEquipamientoForm
    permission = 'evento.change_eventoequipamiento'

    def get_success_url(self):
        return reverse_lazy('eventos_equipamiento', kwargs={'equipamiento_id': self.kwargs['equipamiento_id']})

    def get_context_data(self, **kwargs):
        equipamiento_id = self.kwargs['equipamiento_id']
        pk = self.kwargs['pk']
        context = super(ModificarEventoEquipamientoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar evento'
        context['titulo_tabla'] = "Modificar"
        context['equipamiento_id'] = equipamiento_id
        context['subtitulo_tabla'] = "evento"
        context['icono_form'] = 'edit'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Equipamientos', 'href': reverse_lazy('equipamientos')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos_equipamiento', kwargs={'equipamiento_id': self.kwargs['equipamiento_id']})},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_evento_equipamiento', kwargs={'equipamiento_id': equipamiento_id, 'pk': pk})},
        ]
        return context

    def form_valid(self, form):
        evento = form.save(commit=False)
        equipamiento_id = self.kwargs['equipamiento_id']
        evento.equipamiento_id = equipamiento_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento modificado con éxito.")
        return super(ModificarEventoEquipamientoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no modificado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarEventoEquipamientoView(PermissionRequiredMixin, DeleteView):
    permission = 'evento.delete_eventoequipamiento'

    def get(self, request, *args, **kwargs):
        evento = EventoEquipamiento.objects.filter(llamado_id=self.kwargs['pk'],equipamiento=self.kwargs['equipamiento_id']).first()
        evento.delete()
        messages.add_message(request, messages.SUCCESS, "Evento eliminado con éxito.")
        return JsonResponse({})

        # return HttpResponseRedirect(reverse_lazy('registrar_evento_proyecto_calendario',
        #                                          kwargs={'proyecto_id': evento.llamado.proyecto.id,
        #                                                  'llamado_id': evento.llamado.id}))


class HabilitarEventoEquipamientoView(PermissionRequiredMixin, View):
    permission = 'evento.enable_eventoequipamiento'

    def get(self, request, *args, **kwargs):
        evento = EventoEquipamiento.objects.get(id=self.kwargs['pk'])
        evento.activo = True
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarEventoEquipamientoView(PermissionRequiredMixin, View):
    permission = 'evento.disable_eventoequipamiento'

    def get(self, request, *args, **kwargs):
        evento = EventoEquipamiento.objects.get(id=self.kwargs['pk'])
        evento.activo = False
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento deshabilitado con éxito.")
        return JsonResponse({})


class DetallesEventoEquipamientoView(PermissionRequiredMixin, DetailView):
        template_name = 'evento_equipamiento/detalles_evento_equipamiento.html'
        model = EventoEquipamiento
        permission = 'evento.view_eventoequipamiento'

        def get_context_data(self, **kwargs):
            equipamiento_id = self.kwargs['equipamiento_id']
            context = super(DetallesEventoEquipamientoView, self).get_context_data(**kwargs)
            context['titulo'] = 'Detalles del evento'
            context['equipamiento_id'] = equipamiento_id
            context['titulo_tabla'] = 'Detalles'
            context['activar_eventos'] = True
            context['path'] = [
                {'name': 'Equipamientos', 'href': reverse_lazy('equipamientos')},
                {'name': 'Eventos', 'href': reverse_lazy('eventos_equipamiento', kwargs={'equipamiento_id': self.kwargs['equipamiento_id']})},
                {'name': 'Detalles', 'href': reverse_lazy('detalles_evento_equipamiento', kwargs={'equipamiento_id': self.kwargs['equipamiento_id'], 'pk': self.kwargs['pk']})},
            ]
            return context


class EventosEquipamientoPDFView(PermissionRequiredMixin, View):
    permission = 'evento.export_eventosequipamiento'

    def get(self, request, *args, **kwargs):
        equipamiento_id = self.kwargs['equipamiento_id']
        eventos = EventoEquipamiento.objects.filter(equipamiento_id=equipamiento_id).order_by('id')
        template_path = 'pdfs/eventos_equipamiento_pdf.html'
        if not request.user.has_perm('evento.export_eventosequipamiento'):
            raise PermissionDenied
        for evento in eventos:
            title = f'Listado de Eventos del Equipamiento {evento.equipamiento.nombre}'
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

