import datetime
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView

from abastecimiento.forms.form_abastecimiento import AbastecimientoForm
from abastecimiento.models.abastecimiento import Abastecimiento
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.marca_comercial_registrada import MarcaComercialRegistrada
from nomencladores.models.sub_categoria import SubCategoria


class ListadoAbastecimientosView(PermissionRequiredMixin, ListView):
    model = Abastecimiento
    template_name = 'abastecimiento/listado_abastecimiento.html'
    paginate_by = 10
    permission = 'abastecimiento.view_abastecimiento'

    def get_queryset(self):

        abastecimientos = Abastecimiento.objects.all().order_by('id')

        nombre = self.request.GET.get('nombre')
        if nombre is not None and nombre != "":
            abastecimientos = abastecimientos.filter(nombre__icontains=nombre)

        subcategoria_servicio = self.request.GET.get('subcategoria_servicio')
        if subcategoria_servicio is not None and subcategoria_servicio != "":
            abastecimientos = abastecimientos.filter(sub_categoria_id=subcategoria_servicio)

        nombre_producto = self.request.GET.get('nombre_producto')
        if nombre_producto is not None and nombre_producto != "":
            abastecimientos = abastecimientos.filter(nombre_producto__icontains=nombre_producto)

        return abastecimientos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de abastecimientos'
        context['activar_abastecimientos'] = True
        context['path'] = [
            {'name': 'Abastecimientos', 'href': reverse_lazy('abastecimientos')}
        ]

        # Filtros
        categoria_servicio = CategoriaServicio.objects.get(id=5)
        categoria_servicio_id = categoria_servicio.id
        context['subcategorias_servicio'] = SubCategoria.objects.filter(categoria_servicio_id=categoria_servicio_id, activo=True).order_by('nombre')
        #

        return context


class RegistrarAbastecimientoView(PermissionRequiredMixin, CreateView):
    model = Abastecimiento
    template_name = "abastecimiento/abastecimiento_form.html"
    form_class = AbastecimientoForm
    success_url = reverse_lazy('abastecimientos')
    permission = 'abastecimiento.add_abastecimiento'

    def get_context_data(self, **kwargs):
        context = super(RegistrarAbastecimientoView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar abastecimiento'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'abastecimiento'
        context['icono_form'] = 'plus'
        context['activar_abastecimientos'] = True
        context['path'] = [
            {'name': 'Abastecimientos'},
            {'name': 'Abastecimiento', 'href': reverse_lazy('abastecimientos')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_abastecimiento')}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Abastecimiento agregado con éxito.")
        return super(RegistrarAbastecimientoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Abastecimiento no agregado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarAbastecimientoView(PermissionRequiredMixin, UpdateView):
    model = Abastecimiento
    template_name = "abastecimiento/abastecimiento_form.html"
    form_class = AbastecimientoForm
    success_url = reverse_lazy('abastecimientos')
    permission = 'abastecimiento.change_abastecimiento'

    def get_context_data(self, **kwargs):
        context = super(ModificarAbastecimientoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar abastecimiento'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "abastecimiento"
        context['icono_form'] = 'edit'
        context['activar_abastecimientos'] = True
        context['path'] = [
            {'name': 'Abastecimientos'},
            {'name': 'Abastecimiento', 'href': reverse_lazy('abastecimientos')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_abastecimiento', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Abastecimiento modificado con éxito.")
        return super(ModificarAbastecimientoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Abastecimiento no modificado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarAbastecimientoView(PermissionRequiredMixin, View):
    permission = 'abastecimiento.delete_abastecimiento'

    def get(self, request, *args, **kwargs):
        abastecimiento = Abastecimiento.objects.get(id=self.kwargs['pk'])
        abastecimiento.delete()
        messages.add_message(request, messages.SUCCESS, "Abastecimiento eliminado con éxito.")
        return JsonResponse({})


class HabilitarAbastecimientoView(PermissionRequiredMixin, View):
    permission = 'abastecimiento.enable_abastecimiento'

    def get(self, request, *args, **kwargs):
        abastecimiento = Abastecimiento.objects.get(id=self.kwargs['pk'])
        abastecimiento.activo = True
        abastecimiento.save()
        messages.add_message(request, messages.SUCCESS, "Abastecimiento habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarAbastecimientoView(PermissionRequiredMixin, View):
    permission = 'abastecimiento.disable_abastecimiento'

    def get(self, request, *args, **kwargs):
        abastecimiento = Abastecimiento.objects.get(id=self.kwargs['pk'])
        abastecimiento.activo = False
        abastecimiento.save()
        messages.add_message(request, messages.SUCCESS, "Abastecimiento deshabilitado con éxito.")
        return JsonResponse({})


class EliminarAbastecimientosSeleccionadosView(PermissionRequiredMixin, TemplateView):
    permission = 'abastecimiento.delete_abastecimientos_seleccionados'

    def get(self, request, *args, **kwargs):

        try:
            ids = request.GET.get('ids').split(',')
            Abastecimiento.objects.filter(id__in=ids).delete()

            mensaje = "Abastecimientos eliminados con éxito." if ids.__len__() > 1 else "Abastecimiento eliminado con éxito."
            messages.add_message(request, messages.SUCCESS, mensaje)

        except Exception as e:
            print(e.args)
            messages.add_message(request, messages.ERROR, "Ocurrió un error durante la operación.")

        return JsonResponse({})


class DetallesAbastecimientoView(PermissionRequiredMixin, DetailView):
    template_name = 'abastecimiento/detalles_abastecimiento.html'
    model = Abastecimiento
    permission = 'abastecimiento.view_abastecimiento'

    def get_context_data(self, **kwargs):
        context = super(DetallesAbastecimientoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Detalles del abastecimiento'
        context['titulo_tabla'] = 'Detalles'
        context['activar_abastecimientos'] = True
        context['path'] = [
            {'name': 'Abastecimientos'},
            {'name': 'Abastecimiento', 'href': reverse_lazy('abastecimientos')},
            {'name': 'Detalles', 'href': reverse_lazy('detalles_abastecimiento', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context
