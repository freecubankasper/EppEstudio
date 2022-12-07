import datetime
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.marca_transporte import MarcaTransporte
from nomencladores.models.modelo_transporte import Modelo
from nomencladores.models.sub_categoria import SubCategoria
from nomencladores.models.tipo_vehiculo import TipoVehiculo
from transporte.forms.form_transporte import TransporteForm
from transporte.models.transporte import Transporte


class ListadoTransportesView(PermissionRequiredMixin, ListView):
    model = Transporte
    template_name = 'transporte/listado_transportes.html'
    paginate_by = 10
    permission = 'transporte.view_transporte'

    def get_queryset(self):

        transportes = Transporte.objects.all().order_by('id')

        color = self.request.GET.get('color')
        if color is not None and color != "":
            transportes = transportes.filter(color__icontains=color)

        subcategoria_servicio = self.request.GET.get('subcategoria_servicio')
        if subcategoria_servicio is not None and subcategoria_servicio != "":
            transportes = transportes.filter(sub_categoria_id=subcategoria_servicio)

        tipo_vehiculo = self.request.GET.get('tipo_vehiculo')
        if tipo_vehiculo is not None and tipo_vehiculo != "":
            transportes = transportes.filter(tipo_vehiculo_id=tipo_vehiculo)

        marca = self.request.GET.get('marca')
        if marca is not None and marca != "":
            transporte = transportes.filter(marca_id=marca)

        modelo = self.request.GET.get('modelo')
        if marca is not None and modelo != "":
            transportes = transportes.filter(modelo_id=modelo)

        return transportes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de transportes'
        context['activar_transportes'] = True
        context['path'] = [
            {'name': 'Transportes', 'href': reverse_lazy('transportes')}
        ]

        # Filtros
        categoria_servicio = CategoriaServicio.objects.get(id=9)
        categoria_servicio_id = categoria_servicio.id
        context['subcategorias_servicio'] = SubCategoria.objects.filter(categoria_servicio_id=categoria_servicio_id, activo=True).order_by('nombre')
        context['modelos'] = Modelo.objects.filter(activo=True).order_by('nombre')
        context['marcas'] = MarcaTransporte.objects.filter(activo=True).order_by('nombre')
        context['tipos_vehiculo'] = TipoVehiculo.objects.filter(activo=True).order_by('nombre')
        #

        return context


class RegistrarTransporteView(PermissionRequiredMixin, CreateView):
    model = Transporte
    template_name = "transporte/transporte_form.html"
    form_class = TransporteForm
    success_url = reverse_lazy('transportes')
    permission = 'transporte.add_transporte'

    def get_context_data(self, **kwargs):
        context = super(RegistrarTransporteView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar transporte'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'transporte'
        context['icono_form'] = 'plus'
        context['activar_transportes'] = True
        context['path'] = [
            {'name': 'Transportes'},
            {'name': 'Transporte', 'href': reverse_lazy('transportes')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_transporte')}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Transporte agregado con éxito.")
        return super(RegistrarTransporteView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Transporte no agregado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarTransporteView(PermissionRequiredMixin, UpdateView):
    model = Transporte
    template_name = "transporte/transporte_form.html"
    form_class = TransporteForm
    success_url = reverse_lazy('transportes')
    permission = 'transporte.change_transporte'

    def get_context_data(self, **kwargs):
        context = super(ModificarTransporteView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar transporte'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "transporte"
        context['icono_form'] = 'edit'
        context['activar_transportes'] = True
        context['path'] = [
            {'name': 'Transportes'},
            {'name': 'Transporte', 'href': reverse_lazy('transportes')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_transporte', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Transporte modificado con éxito.")
        return super(ModificarTransporteView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Transporte no modificado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarTransporteView(PermissionRequiredMixin, View):
    permission = 'transporte.delete_transporte'

    def get(self, request, *args, **kwargs):
        transporte = Transporte.objects.get(id=self.kwargs['pk'])
        transporte.delete()
        messages.add_message(request, messages.SUCCESS, "Transporte eliminado con éxito.")
        return JsonResponse({})


class HabilitarTransporteView(PermissionRequiredMixin, View):
    permission = 'transporte.enable_transporte'

    def get(self, request, *args, **kwargs):
        transporte = Transporte.objects.get(id=self.kwargs['pk'])
        transporte.activo = True
        transporte.save()
        messages.add_message(request, messages.SUCCESS, "Transporte habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarTransporteView(PermissionRequiredMixin, View):
    permission = 'transporte.disable_transporte'

    def get(self, request, *args, **kwargs):
        transporte = Transporte.objects.get(id=self.kwargs['pk'])
        transporte.activo = False
        transporte.save()
        messages.add_message(request, messages.SUCCESS, "Transporte deshabilitado con éxito.")
        return JsonResponse({})


class EliminarTransportesSeleccionadosView(PermissionRequiredMixin, TemplateView):
    permission = 'transporte.delete_transportes_seleccionados'

    def get(self, request, *args, **kwargs):

        try:
            ids = request.GET.get('ids').split(',')
            Transporte.objects.filter(id__in=ids).delete()

            mensaje = "Transportes eliminados con éxito." if ids.__len__() > 1 else "Transporte eliminado con éxito."
            messages.add_message(request, messages.SUCCESS, mensaje)

        except Exception as e:
            print(e.args)
            messages.add_message(request, messages.ERROR, "Ocurrió un error durante la operación.")

        return JsonResponse({})


class DetallesTransporteView(PermissionRequiredMixin, DetailView):
    template_name = 'transporte/detalles_transporte.html'
    model = Transporte
    permission = 'transporte.view_transporte'

    def get_context_data(self, **kwargs):
        context = super(DetallesTransporteView, self).get_context_data(**kwargs)
        context['titulo'] = 'Detalles de transporte'
        context['titulo_tabla'] = 'Detalles'
        context['activar_transportes'] = True
        context['path'] = [
            {'name': 'Transportes'},
            {'name': 'Transporte', 'href': reverse_lazy('transportes')},
            {'name': 'Detalles', 'href': reverse_lazy('detalles_transporte', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context
