# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.forrm_tipo_vehiculo import TipoVehiculoForm
from nomencladores.models.tipo_vehiculo import TipoVehiculo


class ListadoTiposVehiculosView(PermissionRequiredMixin, ListView):
    model = TipoVehiculo
    template_name = 'tipo_vehiculo/listado_tipos_vehiculo.html'
    paginate_by = 10
    permission = 'nomencladores.view_tipovehiculo'

    def get_queryset(self):
        tipos_vehiculo = TipoVehiculo.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            tipos_vehiculo = tipos_vehiculo.filter(nombre__icontains=q)

        return tipos_vehiculo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de tipos de vehículos'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipos de vehículos', 'href': reverse_lazy('tipos_vehiculo')}
        ]
        return context


class RegistrarTipoVehiculoView(PermissionRequiredMixin, CreateView):
    model = TipoVehiculo
    template_name = "tipo_vehiculo/tipo_vehiculo_form.html"
    form_class = TipoVehiculoForm
    success_url = reverse_lazy('tipos_vehiculo')
    permission = 'nomencladores.add_tipovehiculo'

    def get_context_data(self, **kwargs):
        context = super(RegistrarTipoVehiculoView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar tipo de vehículo'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'tipo de vehículo'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de vehículo', 'href': reverse_lazy('tipos_vehiculo')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_tipo_vehiculo')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de vehículo agregado con éxito.")
        return super(RegistrarTipoVehiculoView, self).form_valid(form)


class ModificarTipoVehiculoView(PermissionRequiredMixin, UpdateView):
    model = TipoVehiculo
    template_name = "tipo_vehiculo/tipo_vehiculo_form.html"
    form_class = TipoVehiculoForm
    success_url = reverse_lazy('tipos_vehiculo')
    permission = 'nomencladores.change_tipovehiculo'

    def get_context_data(self, **kwargs):
        context = super(ModificarTipoVehiculoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar tipo de vehículo'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "tipo de vehículo"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de vehículo', 'href': reverse_lazy('tipos_vehiculo')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_tipo_vehiculo', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de vehículo modificado con éxito.")
        return super(ModificarTipoVehiculoView, self).form_valid(form)


class HabilitarTipoVehiculoView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_tipovehiculo'

    def get(self, request, *args, **kwargs):
        tipo_vehiculo = TipoVehiculo.objects.get(id=self.kwargs['pk'])
        tipo_vehiculo.activo = True
        tipo_vehiculo.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de vehículo habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarTipoVehiculoView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_tipovehiculo'

    def get(self, request, *args, **kwargs):
        tipo_vehiculo = TipoVehiculo.objects.get(id=self.kwargs['pk'])
        tipo_vehiculo.activo = False
        tipo_vehiculo.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de vehículo deshabilitado con éxito.")
        return JsonResponse({})


