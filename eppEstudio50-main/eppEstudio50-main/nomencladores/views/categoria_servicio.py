# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_categoria_servicio import CategoriaServicioForm
from nomencladores.models.categoria_servicio import CategoriaServicio


class ListadoCategoriasServicioView(PermissionRequiredMixin, ListView):
    model = CategoriaServicio
    template_name = 'categoria_servicio/listado_categorias_servicio.html'
    paginate_by = 10
    permission = 'nomencladores.view_categoriaservicio'

    def get_queryset(self):
        categoria_servicio = CategoriaServicio.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            categoria_servicio = categoria_servicio.filter(nombre__icontains=q)

        return categoria_servicio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado categorías de servicio'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Categorías de servicio', 'href': reverse_lazy('categorias_servicio')}
        ]
        return context


class RegistrarCategoriaServicioView(PermissionRequiredMixin, CreateView):
    model = CategoriaServicio
    template_name = "categoria_servicio/categoria_servicio_form.html"
    form_class = CategoriaServicioForm
    success_url = reverse_lazy('categorias_servicio')
    permission = 'nomencladores.add_categoriaservicio'

    def get_context_data(self, **kwargs):
        context = super(RegistrarCategoriaServicioView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar categoría de servicio'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'categoría de servicio'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Categoría de servicio', 'href': reverse_lazy('categorias_servicio')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_categoria_servicio')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Categoría de servicio agregada con éxito.")
        return super(RegistrarCategoriaServicioView, self).form_valid(form)


class ModificarCategoriaServicioView(PermissionRequiredMixin, UpdateView):
    model = CategoriaServicio
    template_name = "categoria_servicio/categoria_servicio_form.html"
    form_class = CategoriaServicioForm
    success_url = reverse_lazy('categorias_servicio')
    permission = 'nomencladores.change_categoriaservicio'

    def get_context_data(self, **kwargs):
        context = super(ModificarCategoriaServicioView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar categoría de servicio'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "categoría de servicio"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Categoría de servicio', 'href': reverse_lazy('categorias_servicio')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_categoria_servicio', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Categoría de servicio modificada con éxito.")
        return super(ModificarCategoriaServicioView, self).form_valid(form)


class HabilitarCategoriaServicioView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_categoriaservicio'

    def get(self, request, *args, **kwargs):
        categoria_servicio = CategoriaServicio.objects.get(id=self.kwargs['pk'])
        categoria_servicio.activo = True
        categoria_servicio.save()
        messages.add_message(request, messages.SUCCESS, "Categoría de servicio habilitada con éxito.")
        return JsonResponse({})


class DeshabilitarCategoriaServicioView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_categoriaservicio'

    def get(self, request, *args, **kwargs):
        categoria_servicio = CategoriaServicio.objects.get(id=self.kwargs['pk'])
        categoria_servicio.activo = False
        categoria_servicio.save()
        messages.add_message(request, messages.SUCCESS, "Categoría de servicio deshabilitada con éxito.")
        return JsonResponse({})


