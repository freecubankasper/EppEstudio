# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_tipo_articulo import TipoArticuloForm
from nomencladores.models.tipo_articulo import TipoArticulo


class ListadoTiposArticulosView(PermissionRequiredMixin, ListView):
    model = TipoArticulo
    template_name = 'tipo_articulo/listado_tipos_articulo.html'
    paginate_by = 10
    permission = 'nomencladores.view_tipoarticulo'

    def get_queryset(self):
        tipos_articulo = TipoArticulo.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            tipos_articulo = tipos_articulo.filter(nombre__icontains=q)

        return tipos_articulo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de tipos de artículos'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipos de artículos', 'href': reverse_lazy('tipos_articulo')}
        ]
        return context


class RegistrarTipoArticuloView(PermissionRequiredMixin, CreateView):
    model = TipoArticulo
    template_name = "tipo_articulo/tipo_articulo_form.html"
    form_class = TipoArticuloForm
    success_url = reverse_lazy('tipos_articulo')
    permission = 'nomencladores.add_tipoarticulo'

    def get_context_data(self, **kwargs):
        context = super(RegistrarTipoArticuloView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar tipo de artículo'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'tipo de artículo'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de artículo', 'href': reverse_lazy('tipos_articulo')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_tipo_articulo')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de artículo agregado con éxito.")
        return super(RegistrarTipoArticuloView, self).form_valid(form)


class ModificarTipoArticuloView(PermissionRequiredMixin, UpdateView):
    model = TipoArticulo
    template_name = "tipo_articulo/tipo_articulo_form.html"
    form_class = TipoArticuloForm
    success_url = reverse_lazy('tipos_articulo')
    permission = 'nomencladores.change_tipoarticulo'

    def get_context_data(self, **kwargs):
        context = super(ModificarTipoArticuloView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar tipo de artículo'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "tipo de artículo"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de artículo', 'href': reverse_lazy('tipos_articulo')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_tipo_articulo', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de artículo modificado con éxito.")
        return super(ModificarTipoArticuloView, self).form_valid(form)


class HabilitarTipoArticuloView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_tipoarticulo'

    def get(self, request, *args, **kwargs):
        tipo_articulo = TipoArticulo.objects.get(id=self.kwargs['pk'])
        tipo_articulo.activo = True
        tipo_articulo.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de artículo habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarTipoArticuloView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_tipoarticulo'

    def get(self, request, *args, **kwargs):
        tipo_articulo = TipoArticulo.objects.get(id=self.kwargs['pk'])
        tipo_articulo.activo = False
        tipo_articulo.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de artículo deshabilitado con éxito.")
        return JsonResponse({})


