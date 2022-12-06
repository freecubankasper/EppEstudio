import datetime
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from core.utiles.permission_required import PermissionRequiredMixin
from equipamiento.forms.form_equipamiento import EquipamientoForm
from equipamiento.models.equipamiento import Equipamiento
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.marca_comercial_registrada import MarcaComercialRegistrada
from nomencladores.models.sub_categoria import SubCategoria


class ListadoEquipamientosView(PermissionRequiredMixin, ListView):
    model = Equipamiento
    template_name = 'equipamiento/listado_equipamiento.html'
    paginate_by = 10
    permission = 'equipamiento.view_equipamiento'

    def get_queryset(self):

        equipamientos = Equipamiento.objects.all().order_by('id')

        nombre = self.request.GET.get('nombre')
        if nombre is not None and nombre != "":
            equipamientos = equipamientos.filter(nombre__icontains=nombre)

        subcategoria_servicio = self.request.GET.get('subcategoria_servicio')
        if subcategoria_servicio is not None and subcategoria_servicio != "":
            equipamientos = equipamientos.filter(sub_categoria_id=subcategoria_servicio)

        marca_comercial = self.request.GET.get('marca_comercial')
        if marca_comercial is not None and marca_comercial != "":
            equipamientos = equipamientos.filter(marca_id=marca_comercial)

        return equipamientos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de equipamientos'
        context['activar_equipamientos'] = True
        context['path'] = [
            {'name': 'Equipamientos', 'href': reverse_lazy('equipamientos')}
        ]

        # Filtros
        categoria_servicio = CategoriaServicio.objects.get(id=1)
        categoria_servicio_id = categoria_servicio.id
        context['subcategorias_servicio'] = SubCategoria.objects.filter(categoria_servicio_id=categoria_servicio_id, activo=True).order_by('nombre')
        context['marcas_comercial'] = MarcaComercialRegistrada.objects.filter(activo=True).order_by('nombre')
        #

        return context


class RegistrarEquipamientoView(PermissionRequiredMixin, CreateView):
    model = Equipamiento
    template_name = "equipamiento/equipamiento_form.html"
    form_class = EquipamientoForm
    success_url = reverse_lazy('equipamientos')
    permission = 'equipamiento.add_equipamiento'

    def get_context_data(self, **kwargs):
        context = super(RegistrarEquipamientoView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar equipamiento'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'equipamiento'
        context['icono_form'] = 'plus'
        context['activar_equipamientos'] = True
        context['path'] = [
            {'name': 'Equipamientos'},
            {'name': 'Equipamiento', 'href': reverse_lazy('equipamientos')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_equipamiento')}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Equipamiento agregado con éxito.")
        return super(RegistrarEquipamientoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Equipamiento no agregado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarEquipamientoView(PermissionRequiredMixin, UpdateView):
    model = Equipamiento
    template_name = "equipamiento/equipamiento_form.html"
    form_class = EquipamientoForm
    success_url = reverse_lazy('equipamientos')
    permission = 'equipamiento.change_equipamiento'

    def get_context_data(self, **kwargs):
        context = super(ModificarEquipamientoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar equipamiento'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "equipamiento"
        context['icono_form'] = 'edit'
        context['activar_equipamientos'] = True
        context['path'] = [
            {'name': 'Equipamientos'},
            {'name': 'Equipamiento', 'href': reverse_lazy('equipamientos')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_equipamiento', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Equipamiento modificado con éxito.")
        return super(ModificarEquipamientoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Equipamiento no modificado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarEquipamientoView(PermissionRequiredMixin, View):
    permission = 'equipamiento.delete_equipamiento'

    def get(self, request, *args, **kwargs):
        equipamiento = Equipamiento.objects.get(id=self.kwargs['pk'])
        equipamiento.delete()
        messages.add_message(request, messages.SUCCESS, "Equipamiento eliminado con éxito.")
        return JsonResponse({})


class HabilitarEquipamientoView(PermissionRequiredMixin, View):
    permission = 'equipamiento.enable_equipamiento'

    def get(self, request, *args, **kwargs):
        equipamiento = Equipamiento.objects.get(id=self.kwargs['pk'])
        equipamiento.activo = True
        equipamiento.save()
        messages.add_message(request, messages.SUCCESS, "Equipamiento habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarEquipamientoView(PermissionRequiredMixin, View):
    permission = 'equipamiento.disable_equipamiento'

    def get(self, request, *args, **kwargs):
        equipamiento = Equipamiento.objects.get(id=self.kwargs['pk'])
        equipamiento.activo = False
        equipamiento.save()
        messages.add_message(request, messages.SUCCESS, "Equipamiento deshabilitado con éxito.")
        return JsonResponse({})


class EliminarEquipamientosSeleccionadosView(PermissionRequiredMixin, TemplateView):
    permission = 'equipamiento.delete_equipamientos_seleccionados'

    def get(self, request, *args, **kwargs):

        try:
            ids = request.GET.get('ids').split(',')
            Equipamiento.objects.filter(id__in=ids).delete()

            mensaje = "Equipamientos eliminados con éxito." if ids.__len__() > 1 else "Equipamiento eliminado con éxito."
            messages.add_message(request, messages.SUCCESS, mensaje)

        except Exception as e:
            print(e.args)
            messages.add_message(request, messages.ERROR, "Ocurrió un error durante la operación.")

        return JsonResponse({})


class DetallesEquipamientoView(PermissionRequiredMixin, DetailView):
    template_name = 'equipamiento/detalles_equipamiento.html'
    model = Equipamiento
    permission = 'equipamiento.view_equipamiento'

    def get_context_data(self, **kwargs):
        context = super(DetallesEquipamientoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Detalles del equipamiento'
        context['titulo_tabla'] = 'Detalles'
        context['activar_equipamientos'] = True
        context['path'] = [
            {'name': 'Equipamientos'},
            {'name': 'Equipamiento', 'href': reverse_lazy('equipamientos')},
            {'name': 'Detalles', 'href': reverse_lazy('detalles_equipamiento', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context
