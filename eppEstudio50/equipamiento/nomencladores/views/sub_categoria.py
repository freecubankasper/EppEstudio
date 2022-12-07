# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_sub_categoria import SubCategoriaForm
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.sub_categoria import SubCategoria


class ListadoSubsCategoriaView(PermissionRequiredMixin, ListView):
    model = SubCategoria
    template_name = 'sub_categoria/listado_subs_categoria.html'
    paginate_by = 10
    permission = 'nomencladores.view_subcategoria'

    def get_queryset(self):

        subs_categoria = SubCategoria.objects.all().order_by('nombre')

        nombre = self.request.GET.get('nombre')
        if nombre is not None and nombre != "":
            subs_categoria = subs_categoria.filter(nombre__icontains=nombre)

        categoria_servicio = self.request.GET.get('categoria_servicio')
        if categoria_servicio is not None and categoria_servicio != "":
            subs_categoria = subs_categoria.filter(categoria_servicio_id=categoria_servicio)

        return subs_categoria

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de subcategoría de servicio'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Subcategoría de servicio', 'href': reverse_lazy('subs_categoria')}
        ]

        # Filtros
        context['categorias_servicio'] = CategoriaServicio.objects.filter(activo=True).order_by('nombre')

        return context


class RegistrarSubCategoriaView(PermissionRequiredMixin, CreateView):
    model = SubCategoria
    template_name = "sub_categoria/sub_categoria_form.html"
    form_class = SubCategoriaForm
    success_url = reverse_lazy('subs_categoria')
    permission = 'nomencladores.add_subcategoria'

    def get_context_data(self, **kwargs):
        context = super(RegistrarSubCategoriaView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar subcategoría de servicio'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'subcategoría de servicio'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Subcategoría de servicio', 'href': reverse_lazy('subs_categoria')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_sub_categoria')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Subcategoría de servicio agregada con éxito.")
        return super(RegistrarSubCategoriaView, self).form_valid(form)


class ModificarSubCategoriaView(PermissionRequiredMixin, UpdateView):
    model = SubCategoria
    template_name = "sub_categoria/sub_categoria_form.html"
    form_class = SubCategoriaForm
    success_url = reverse_lazy('subs_categoria')
    permission = 'nomencladores.change_subcategoria'

    def get_context_data(self, **kwargs):
        context = super(ModificarSubCategoriaView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar subcategoría de servicio'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "subcategoría de servicio"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Subcategoría de servicio', 'href': reverse_lazy('subs_categoria')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_sub_categoria', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Subcategoría de servicio modificada con éxito.")
        return super(ModificarSubCategoriaView, self).form_valid(form)


class HabilitarSubCategoriaView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_subcategoria'

    def get(self, request, *args, **kwargs):
        sub_categoria = SubCategoria.objects.get(id=self.kwargs['pk'])
        sub_categoria.activo = True
        sub_categoria.save()
        messages.add_message(request, messages.SUCCESS, "Subcategoría de servicio habilitada con éxito.")
        return JsonResponse({})


class DeshabilitarSubCategoriaView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_subcategoria'

    def get(self, request, *args, **kwargs):
        sub_categoria = SubCategoria.objects.get(id=self.kwargs['pk'])
        sub_categoria.activo = False
        sub_categoria.save()
        messages.add_message(request, messages.SUCCESS, "Subcategoría de servicio deshabilitada con éxito.")
        return JsonResponse({})


