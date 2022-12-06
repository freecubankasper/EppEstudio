# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_categoria import CategoriaForm
from nomencladores.models.categoria import Categoria


class ListadoCategoriasView(PermissionRequiredMixin, ListView):
    model = Categoria
    template_name = 'categoria/listado_categorias.html'
    paginate_by = 10
    permission = 'nomencladores.view_categoria'

    def get_queryset(self):
        categoria = Categoria.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            categoria = categoria.filter(nombre__icontains=q)

        return categoria

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de categorías'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Categorías', 'href': reverse_lazy('categorias')}
        ]
        return context


class RegistrarCategoriaView(PermissionRequiredMixin, CreateView):
    model = Categoria
    template_name = "categoria/categoria_form.html"
    form_class = CategoriaForm
    success_url = reverse_lazy('categorias')
    permission = 'nomencladores.add_categoria'

    def get_context_data(self, **kwargs):
        context = super(RegistrarCategoriaView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar categoría'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'categoría'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Categoría', 'href': reverse_lazy('categorias')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_categoria')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Categoría agregada con éxito.")
        return super(RegistrarCategoriaView, self).form_valid(form)


class ModificarCategoriaView(PermissionRequiredMixin, UpdateView):
    model = Categoria
    template_name = "categoria/categoria_form.html"
    form_class = CategoriaForm
    success_url = reverse_lazy('categorias')
    permission = 'nomencladores.change_categoria'

    def get_context_data(self, **kwargs):
        context = super(ModificarCategoriaView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar categoría'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "categoría"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Categoría', 'href': reverse_lazy('categorias')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_categoria', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Categoría modificada con éxito.")
        return super(ModificarCategoriaView, self).form_valid(form)


class HabilitarCategoriaView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_categoria'

    def get(self, request, *args, **kwargs):
        categoria = Categoria.objects.get(id=self.kwargs['pk'])
        categoria.activo = True
        categoria.save()
        messages.add_message(request, messages.SUCCESS, "Categoría habilitada con éxito.")
        return JsonResponse({})


class DeshabilitarCategoriaView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_categoria'

    def get(self, request, *args, **kwargs):
        categoria = Categoria.objects.get(id=self.kwargs['pk'])
        categoria.activo = False
        categoria.save()
        messages.add_message(request, messages.SUCCESS, "Categoría deshabilitada con éxito.")
        return JsonResponse({})


