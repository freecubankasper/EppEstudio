# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_tipo_aprobacion import TipoAprobacionForm
from nomencladores.models.tipo_aprobacion import TipoAprobacion


class ListadoTiposAprobacionesView(PermissionRequiredMixin, ListView):
    model = TipoAprobacion
    template_name = 'tipo_aprobacion/listado_tipos_aprobacion.html'
    paginate_by = 10
    permission = 'nomencladores.view_tipoaprobacion'

    def get_queryset(self):
        tipos_aprobacion = TipoAprobacion.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            tipos_aprobacion = tipos_aprobacion.filter(nombre__icontains=q)

        return tipos_aprobacion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de tipos de aprobaciones'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipos de aprobaciones', 'href': reverse_lazy('tipos_aprobacion')}
        ]
        return context


class RegistrarTipoAprobacionView(PermissionRequiredMixin, CreateView):
    model = TipoAprobacion
    template_name = "tipo_aprobacion/tipo_aprobacion_form.html"
    form_class = TipoAprobacionForm
    success_url = reverse_lazy('tipos_aprobacion')
    permission = 'nomencladores.add_tipoaprobacion'

    def get_context_data(self, **kwargs):
        context = super(RegistrarTipoAprobacionView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar tipo de aprobación'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'tipo de aprobación'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de aprobación', 'href': reverse_lazy('tipos_aprobacion')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_tipo_aprobacion')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de aprobación agregada con éxito.")
        return super(RegistrarTipoAprobacionView, self).form_valid(form)


class ModificarTipoAprobacionView(PermissionRequiredMixin, UpdateView):
    model = TipoAprobacion
    template_name = "tipo_aprobacion/tipo_aprobacion_form.html"
    form_class = TipoAprobacionForm
    success_url = reverse_lazy('tipos_aprobacion')
    permission = 'nomencladores.change_tipoaprobacion'

    def get_context_data(self, **kwargs):
        context = super(ModificarTipoAprobacionView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar tipo de aprobación'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "tipo de aprobación"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de aprobación', 'href': reverse_lazy('tipos_aprobacion')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_tipo_aprobacion', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de aprobación modificada con éxito.")
        return super(ModificarTipoAprobacionView, self).form_valid(form)


class HabilitarTipoAprobacionView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_tipo_aprobacion'

    def get(self, request, *args, **kwargs):
        tipo_aprobacion = TipoAprobacion.objects.get(id=self.kwargs['pk'])
        tipo_aprobacion.activo = True
        tipo_aprobacion.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de aprobación habilitada con éxito.")
        return JsonResponse({})


class DeshabilitarTipoAprobacionView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_tipo_aprobacion'

    def get(self, request, *args, **kwargs):
        tipo_aprobacion = TipoAprobacion.objects.get(id=self.kwargs['pk'])
        tipo_aprobacion.activo = False
        tipo_aprobacion.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de aprobación deshabilitada con éxito.")
        return JsonResponse({})


