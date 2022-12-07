# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_tipo_entidad import TipoEntidadForm
from nomencladores.models.entidad import TipoEntidad


class ListadoTiposEntidadesView(PermissionRequiredMixin, ListView):
    model = TipoEntidad
    template_name = 'tipo_entidad/listado_tipos_entidad.html'
    paginate_by = 10
    permission = 'nomencladores.view_tipoentidad'

    def get_queryset(self):
        tipos_entidad = TipoEntidad.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            tipos_entidad = tipos_entidad.filter(nombre__icontains=q)

        return tipos_entidad

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de tipos de entidades'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipos de entidades', 'href': reverse_lazy('tipos_entidad')}
        ]
        return context


class RegistrarTipoEntidadView(PermissionRequiredMixin, CreateView):
    model = TipoEntidad
    template_name = "tipo_entidad/tipo_entidad_form.html"
    form_class = TipoEntidadForm
    success_url = reverse_lazy('tipos_entidad')
    permission = 'nomencladores.add_tipoentidad'

    def get_context_data(self, **kwargs):
        context = super(RegistrarTipoEntidadView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar tipo de entidad'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'tipo de entidad'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de entidad', 'href': reverse_lazy('tipos_entidad')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_tipo_entidad')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de entidad agregada con éxito.")
        return super(RegistrarTipoEntidadView, self).form_valid(form)


class ModificarTipoEntidadView(PermissionRequiredMixin, UpdateView):
    model = TipoEntidad
    template_name = "tipo_entidad/tipo_entidad_form.html"
    form_class = TipoEntidadForm
    success_url = reverse_lazy('tipos_entidad')
    permission = 'nomencladores.change_tipoentidad'

    def get_context_data(self, **kwargs):
        context = super(ModificarTipoEntidadView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar tipo de entidad'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "tipo de entidad"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de entidad', 'href': reverse_lazy('tipos_entidad')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_tipo_entidad', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de entidad modificada con éxito.")
        return super(ModificarTipoEntidadView, self).form_valid(form)


class HabilitarTipoEntidadView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_tipo_entidad'

    def get(self, request, *args, **kwargs):
        tipo_entidad = TipoEntidad.objects.get(id=self.kwargs['pk'])
        tipo_entidad.activo = True
        tipo_entidad.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de entidad habilitada con éxito.")
        return JsonResponse({})


class DeshabilitarTipoEntidadView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_tipo_entidad'

    def get(self, request, *args, **kwargs):
        tipo_entidad = TipoEntidad.objects.get(id=self.kwargs['pk'])
        tipo_entidad.activo = False
        tipo_entidad.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de entidad deshabilitada con éxito.")
        return JsonResponse({})


