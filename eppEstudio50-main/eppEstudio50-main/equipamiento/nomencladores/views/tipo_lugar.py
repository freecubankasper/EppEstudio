# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_tipo_lugar import TipoLugarForm
from nomencladores.models.tipo_lugar import TipoLugar


class ListadoTiposLugaresView(PermissionRequiredMixin, ListView):
    model = TipoLugar
    template_name = 'tipo_lugar/listado_tipos_lugar.html'
    paginate_by = 10
    permission = 'nomencladores.view_tipolugar'

    def get_queryset(self):
        tipos_lugar = TipoLugar.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            tipos_lugar = tipos_lugar.filter(nombre__icontains=q)

        return tipos_lugar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de tipos de lugares'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipos de lugares', 'href': reverse_lazy('tipos_lugar')}
        ]
        return context


class RegistrarTipoLugarView(PermissionRequiredMixin, CreateView):
    model = TipoLugar
    template_name = "tipo_lugar/tipo_lugar_form.html"
    form_class = TipoLugarForm
    success_url = reverse_lazy('tipos_lugar')
    permission = 'nomencladores.add_tipolugar'

    def get_context_data(self, **kwargs):
        context = super(RegistrarTipoLugarView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar tipo de lugar'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'tipo de lugar'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de lugar', 'href': reverse_lazy('tipos_lugar')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_tipo_lugar')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de lugar agregado con éxito.")
        return super(RegistrarTipoLugarView, self).form_valid(form)


class ModificarTipoLugarView(PermissionRequiredMixin, UpdateView):
    model = TipoLugar
    template_name = "tipo_lugar/tipo_lugar_form.html"
    form_class = TipoLugarForm
    success_url = reverse_lazy('tipos_lugar')
    permission = 'nomencladores.change_tipolugar'

    def get_context_data(self, **kwargs):
        context = super(ModificarTipoLugarView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar tipo de lugar'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "tipo de lugar"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de lugar', 'href': reverse_lazy('tipos_lugar')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_tipo_lugar', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de lugar modificado con éxito.")
        return super(ModificarTipoLugarView, self).form_valid(form)


class HabilitarTipoLugarView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_tipolugar'

    def get(self, request, *args, **kwargs):
        tipo_lugar = TipoLugar.objects.get(id=self.kwargs['pk'])
        tipo_lugar.activo = True
        tipo_lugar.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de lugar habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarTipoLugarView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_tipolugar'

    def get(self, request, *args, **kwargs):
        tipo_lugar = TipoLugar.objects.get(id=self.kwargs['pk'])
        tipo_lugar.activo = False
        tipo_lugar.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de lugar deshabilitado con éxito.")
        return JsonResponse({})


