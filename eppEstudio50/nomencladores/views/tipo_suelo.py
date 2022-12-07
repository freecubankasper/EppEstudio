# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_tipo_suelo import TipoSueloForm
from nomencladores.models.tipo_suelo import TipoSuelo


class ListadoTiposSuelosView(PermissionRequiredMixin, ListView):
    model = TipoSuelo
    template_name = 'tipo_suelo/listado_tipos_suelo.html'
    paginate_by = 10
    permission = 'nomencladores.view_tiposuelo'

    def get_queryset(self):
        tipos_suelo = TipoSuelo.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            tipos_suelo = tipos_suelo.filter(nombre__icontains=q)

        return tipos_suelo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de tipos de suelos'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipos de suelos', 'href': reverse_lazy('tipos_suelo')}
        ]
        return context


class RegistrarTipoSueloView(PermissionRequiredMixin, CreateView):
    model = TipoSuelo
    template_name = "tipo_suelo/tipo_suelo_form.html"
    form_class = TipoSueloForm
    success_url = reverse_lazy('tipos_suelo')
    permission = 'nomencladores.add_tiposuelo'

    def get_context_data(self, **kwargs):
        context = super(RegistrarTipoSueloView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar tipo de suelo'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'tipo de suelo'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de suelo', 'href': reverse_lazy('tipos_suelo')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_tipo_suelo')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de suelo agregado con éxito.")
        return super(RegistrarTipoSueloView, self).form_valid(form)


class ModificarTipoSueloView(PermissionRequiredMixin, UpdateView):
    model = TipoSuelo
    template_name = "tipo_suelo/tipo_suelo_form.html"
    form_class = TipoSueloForm
    success_url = reverse_lazy('tipos_suelo')
    permission = 'nomencladores.change_tiposuelo'

    def get_context_data(self, **kwargs):
        context = super(ModificarTipoSueloView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar tipo de suelo'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "tipo de suelo"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de suelo', 'href': reverse_lazy('tipos_suelo')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_tipo_suelo', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de suelo modificado con éxito.")
        return super(ModificarTipoSueloView, self).form_valid(form)


class HabilitarTipoSueloView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_tipo_suelo'

    def get(self, request, *args, **kwargs):
        tipo_suelo = TipoSuelo.objects.get(id=self.kwargs['pk'])
        tipo_suelo.activo = True
        tipo_suelo.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de suelo habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarTipoSueloView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_tipo_suelo'

    def get(self, request, *args, **kwargs):
        tipo_suelo = TipoSuelo.objects.get(id=self.kwargs['pk'])
        tipo_suelo.activo = False
        tipo_suelo.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de suelo deshabilitado con éxito.")
        return JsonResponse({})


