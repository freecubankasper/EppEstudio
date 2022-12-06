# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_categoria_lic_conduccion import CategoriaLicenciaConduccionForm
from nomencladores.models.categoria_lic_conduccion import CategoriaLicenciaConduccion


class ListadoCategoriasLicenciasConduccionView(PermissionRequiredMixin, ListView):
    model = CategoriaLicenciaConduccion
    template_name = 'categoria_lic_conduccion/listado_categorias_lic_conduccion.html'
    paginate_by = 10
    permission = 'nomencladores.view_categorialicencia_conduccion'

    def get_queryset(self):
        categoria_licencia = CategoriaLicenciaConduccion.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            categoria_licencia = categoria_licencia.filter(nombre__icontains=q)

        return categoria_licencia

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de categorías de licencias de conducción'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Categorías de licencias de conducción', 'href': reverse_lazy('categorias_lic_conduccion')}
        ]
        return context


class RegistrarCategoriaLicenciaConduccionView(PermissionRequiredMixin, CreateView):
    model = CategoriaLicenciaConduccion
    template_name = "categoria_lic_conduccion/categoria_lic_conduccion_form.html"
    form_class = CategoriaLicenciaConduccionForm
    success_url = reverse_lazy('categorias_lic_conduccion')
    permission = 'nomencladores.add_categorialicenciaconduccion'

    def get_context_data(self, **kwargs):
        context = super(RegistrarCategoriaLicenciaConduccionView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar categoría de licencia de conducción'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'categoría de licencia de conducción'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Categoría de licencia de conducción', 'href': reverse_lazy('categorias_lic_conduccion')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_categoria_lic_conduccion')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Categoría de licencia de conducción agregada con éxito.")
        return super(RegistrarCategoriaLicenciaConduccionView, self).form_valid(form)


class ModificarCategoriaLicenciaConduccionView(PermissionRequiredMixin, UpdateView):
    model = CategoriaLicenciaConduccion
    template_name = "categoria_lic_conduccion/categoria_lic_conduccion_form.html"
    form_class = CategoriaLicenciaConduccionForm
    success_url = reverse_lazy('categorias_lic_conduccion')
    permission = 'nomencladores.change_categorialicenciaconduccion'

    def get_context_data(self, **kwargs):
        context = super(ModificarCategoriaLicenciaConduccionView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar categoría de licencia de conducción'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "categoría de licencia de conducción"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Categoría de licencia de conducción', 'href': reverse_lazy('categorias_lic_conduccion')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_categoria_lic_conduccion', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Categoría de licencia de conducción modificada con éxito.")
        return super(ModificarCategoriaLicenciaConduccionView, self).form_valid(form)


class HabilitarCategoriaLicenciaConduccionView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_categorialicenciaconduccion'

    def get(self, request, *args, **kwargs):
        categoria_licencia = CategoriaLicenciaConduccion.objects.get(id=self.kwargs['pk'])
        categoria_licencia.activo = True
        categoria_licencia.save()
        messages.add_message(request, messages.SUCCESS, "Categoría de licencia de conducción habilitada con éxito.")
        return JsonResponse({})


class DeshabilitarCategoriaLicenciaConduccionView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_categorialicenciaconduccion'

    def get(self, request, *args, **kwargs):
        categoria_licencia = CategoriaLicenciaConduccion.objects.get(id=self.kwargs['pk'])
        categoria_licencia.activo = False
        categoria_licencia.save()
        messages.add_message(request, messages.SUCCESS, "Categoría de licencia de conducción deshabilitada con éxito.")
        return JsonResponse({})


