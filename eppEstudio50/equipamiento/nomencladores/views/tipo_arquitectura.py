# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_tipo_arquitectura import TipoArquitecturaForm
from nomencladores.models.tipo_arquitectura import TipoArquitectura


class ListadoTiposArquitecturasView(PermissionRequiredMixin, ListView):
    model = TipoArquitectura
    template_name = 'tipo_arquitectura/listado_tipos_arquitectura.html'
    paginate_by = 10
    permission = 'nomencladores.view_tipoarquitectura'

    def get_queryset(self):
        tipos_arquitectura = TipoArquitectura.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            tipos_arquitectura = tipos_arquitectura.filter(nombre__icontains=q)

        return tipos_arquitectura

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de tipos de arquitecturas'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipos de arquitecturas', 'href': reverse_lazy('tipos_arquitectura')}
        ]
        return context


class RegistrarTipoArquitecturaView(PermissionRequiredMixin, CreateView):
    model = TipoArquitectura
    template_name = "tipo_arquitectura/tipo_arquitectura_form.html"
    form_class = TipoArquitecturaForm
    success_url = reverse_lazy('tipos_arquitectura')
    permission = 'nomencladores.add_tipoarquitectura'

    def get_context_data(self, **kwargs):
        context = super(RegistrarTipoArquitecturaView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar tipo de arquitectura'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'tipo de arquitectura'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de arquitectura', 'href': reverse_lazy('tipos_arquitectura')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_tipo_arquitectura')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de arquitectura agregado con éxito.")
        return super(RegistrarTipoArquitecturaView, self).form_valid(form)


class ModificarTipoArquitecturaView(PermissionRequiredMixin, UpdateView):
    model = TipoArquitectura
    template_name = "tipo_arquitectura/tipo_arquitectura_form.html"
    form_class = TipoArquitecturaForm
    success_url = reverse_lazy('tipos_arquitectura')
    permission = 'nomencladores.change_tipoarquitectura'

    def get_context_data(self, **kwargs):
        context = super(ModificarTipoArquitecturaView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar tipo de arquitectura'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "tipo de arquitectura"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de arquitectura', 'href': reverse_lazy('tipos_arquitectura')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_tipo_arquitectura', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de arquitectura modificado con éxito.")
        return super(ModificarTipoArquitecturaView, self).form_valid(form)


class HabilitarTipoArquitecturaView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_tipoarquitectura'

    def get(self, request, *args, **kwargs):
        tipo_arquitectura = TipoArquitectura.objects.get(id=self.kwargs['pk'])
        tipo_arquitectura.activo = True
        tipo_arquitectura.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de arquitectura habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarTipoArquitecturaView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_tipoarquitectura'

    def get(self, request, *args, **kwargs):
        tipo_arquitectura = TipoArquitectura.objects.get(id=self.kwargs['pk'])
        tipo_arquitectura.activo = False
        tipo_arquitectura.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de arquitectura deshabilitado con éxito.")
        return JsonResponse({})


