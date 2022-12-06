import datetime
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from core.utiles.permission_required import PermissionRequiredMixin
from locacion.forms.form_locacion import LocacionForm
from locacion.models.locacion import Locacion
from nomencladores.models import Municipio
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.sub_categoria import SubCategoria
from nomencladores.models.tipo_arquitectura import TipoArquitectura
from nomencladores.models.tipo_lugar import TipoLugar
from nomencladores.models.tipo_suelo import TipoSuelo


class ListadoLocacionesView(PermissionRequiredMixin, ListView):
    model = Locacion
    template_name = 'locacion/listado_locaciones.html'
    paginate_by = 10
    permission = 'locacion.view_locacion'

    def get_queryset(self):

        locaciones = Locacion.objects.all().order_by('id')

        nombre = self.request.GET.get('nombre')
        if nombre is not None and nombre != "":
            locaciones = locaciones.filter(nombre__icontains=nombre)

        subcategoria_servicio = self.request.GET.get('subcategoria_servicio')
        if subcategoria_servicio is not None and subcategoria_servicio != "":
            locaciones = locaciones.filter(sub_categoria_id=subcategoria_servicio)

        municipio = self.request.GET.get('municipio')
        if municipio is not None and municipio != "":
            locaciones = locaciones.filter(municipio_id=municipio)

        tipo_suelo = self.request.GET.get('tipo_suelo')
        if tipo_suelo is not None and tipo_suelo != "":
            locaciones = locaciones.filter(tipo_suelo_id=tipo_suelo)

        tipo_arquitectura = self.request.GET.get('tipo_arquitectura')
        if tipo_arquitectura is not None and tipo_arquitectura != "":
            locaciones = locaciones.filter(tipo_arquitectura_id=tipo_arquitectura)

        tipo_lugar = self.request.GET.get('tipo_lugar')
        if tipo_lugar is not None and tipo_lugar != "":
            locaciones = locaciones.filter(tipo_lugar_id=tipo_lugar)

        return locaciones

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de locaciones'
        context['activar_locaciones'] = True
        context['path'] = [
            {'name': 'Locaciones', 'href': reverse_lazy('locaciones')}
        ]

        # Filtros
        categoria_servicio = CategoriaServicio.objects.get(id=6)
        categoria_servicio_id = categoria_servicio.id
        context['subcategorias_servicio'] = SubCategoria.objects.filter(categoria_servicio_id=categoria_servicio_id, activo=True).order_by('nombre')
        context['municipios'] = Municipio.objects.filter(activo=True).order_by('nombre')
        context['tipos_suelo'] = TipoSuelo.objects.filter(activo=True).order_by('nombre')
        context['tipos_arquitectura'] = TipoArquitectura.objects.filter(activo=True).order_by('nombre')
        context['tipos_lugar'] = TipoLugar.objects.filter(activo=True).order_by('nombre')
        #

        return context


class RegistrarLocacionView(PermissionRequiredMixin, CreateView):
    model = Locacion
    template_name = "locacion/locacion_form.html"
    form_class = LocacionForm
    success_url = reverse_lazy('locaciones')
    permission = 'locacion.add_locacion'

    def get_context_data(self, **kwargs):
        context = super(RegistrarLocacionView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar locación'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'locación'
        context['icono_form'] = 'plus'
        context['activar_locaciones'] = True
        context['path'] = [
            {'name': 'Locaciones'},
            {'name': 'Locación', 'href': reverse_lazy('locaciones')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_locacion')}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Locación agregada con éxito.")
        return super(RegistrarLocacionView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Locación no agregada con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarLocacionView(PermissionRequiredMixin, UpdateView):
    model = Locacion
    template_name = "locacion/locacion_form.html"
    form_class = LocacionForm
    success_url = reverse_lazy('locaciones')
    permission = 'locacion.change_locacion'

    def get_context_data(self, **kwargs):
        context = super(ModificarLocacionView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar locación'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "locación"
        context['icono_form'] = 'edit'
        context['activar_locaciones'] = True
        context['path'] = [
            {'name': 'Locaciones'},
            {'name': 'Locación', 'href': reverse_lazy('locaciones')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_locacion', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Locación modificada con éxito.")
        return super(ModificarLocacionView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Locación no modificada con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarLocacionView(PermissionRequiredMixin, View):
    permission = 'locacion.delete_locacion'

    def get(self, request, *args, **kwargs):
        locacion = Locacion.objects.get(id=self.kwargs['pk'])
        locacion.delete()
        messages.add_message(request, messages.SUCCESS, "Locación eliminada con éxito.")
        return JsonResponse({})


class HabilitarLocacionView(PermissionRequiredMixin, View):
    permission = 'locacion.enable_locacion'

    def get(self, request, *args, **kwargs):
        locacion = Locacion.objects.get(id=self.kwargs['pk'])
        locacion.activo = True
        locacion.save()
        messages.add_message(request, messages.SUCCESS, "Locación habilitada con éxito.")
        return JsonResponse({})


class DeshabilitarLocacionView(PermissionRequiredMixin, View):
    permission = 'locacion.disable_locacion'

    def get(self, request, *args, **kwargs):
        locacion = Locacion.objects.get(id=self.kwargs['pk'])
        locacion.activo = False
        locacion.save()
        messages.add_message(request, messages.SUCCESS, "Locación deshabilitada con éxito.")
        return JsonResponse({})


class EliminarLocacionesSeleccionadosView(PermissionRequiredMixin, TemplateView):
    permission = 'locacion.delete_locaciones_seleccionados'

    def get(self, request, *args, **kwargs):

        try:
            ids = request.GET.get('ids').split(',')
            Locacion.objects.filter(id__in=ids).delete()

            mensaje = "Locaciones eliminadas con éxito." if ids.__len__() > 1 else "Locación eliminada con éxito."
            messages.add_message(request, messages.SUCCESS, mensaje)

        except Exception as e:
            print(e.args)
            messages.add_message(request, messages.ERROR, "Ocurrió un error durante la operación.")

        return JsonResponse({})


class DetallesLocacionView(PermissionRequiredMixin, DetailView):
    template_name = 'locacion/detalles_locacion.html'
    model = Locacion
    permission = 'locacion.view_locacion'

    def get_context_data(self, **kwargs):
        context = super(DetallesLocacionView, self).get_context_data(**kwargs)
        context['titulo'] = 'Detalles de locación'
        context['titulo_tabla'] = 'Detalles'
        context['activar_locaciones'] = True
        context['path'] = [
            {'name': 'Locaciones'},
            {'name': 'Locación', 'href': reverse_lazy('locaciones')},
            {'name': 'Detalles', 'href': reverse_lazy('detalles_locacion', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context
