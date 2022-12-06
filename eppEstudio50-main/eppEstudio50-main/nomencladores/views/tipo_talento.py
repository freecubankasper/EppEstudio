# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_tipo_talento import TipoTalentoForm
from nomencladores.models.tipo_talento import TipoTalento


class ListadoTiposTalentosView(PermissionRequiredMixin, ListView):
    model = TipoTalento
    template_name = 'tipo_talento/listado_tipos_talento.html'
    paginate_by = 10
    permission = 'nomencladores.view_tipotalento'

    def get_queryset(self):
        tipos_talento = TipoTalento.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            tipos_talento = tipos_talento.filter(nombre__icontains=q)

        return tipos_talento

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de tipos de talentos'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipos de talentos', 'href': reverse_lazy('tipos_talento')}
        ]
        return context


class RegistrarTipoTalentoView(PermissionRequiredMixin, CreateView):
    model = TipoTalento
    template_name = "tipo_talento/tipo_talento_form.html"
    form_class = TipoTalentoForm
    success_url = reverse_lazy('tipos_talento')
    permission = 'nomencladores.add_tipotalento'

    def get_context_data(self, **kwargs):
        context = super(RegistrarTipoTalentoView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar tipo de talento'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'tipo de talento'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de talento', 'href': reverse_lazy('tipos_talento')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_tipo_talento')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de talento agregado con éxito.")
        return super(RegistrarTipoTalentoView, self).form_valid(form)


class ModificarTipoTalentoView(PermissionRequiredMixin, UpdateView):
    model = TipoTalento
    template_name = "tipo_talento/tipo_talento_form.html"
    form_class = TipoTalentoForm
    success_url = reverse_lazy('tipos_talento')
    permission = 'nomencladores.change_tipotalento'

    def get_context_data(self, **kwargs):
        context = super(ModificarTipoTalentoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar tipo de talento'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "tipo de talento"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Tipo de talento', 'href': reverse_lazy('tipos_talento')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_tipo_talento', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Tipo de talento modificado con éxito.")
        return super(ModificarTipoTalentoView, self).form_valid(form)


class HabilitarTipoTalentoView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_tipotalento'

    def get(self, request, *args, **kwargs):
        tipo_talento = TipoTalento.objects.get(id=self.kwargs['pk'])
        tipo_talento.activo = True
        tipo_talento.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de talento habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarTipoTalentoView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_tipotalento'

    def get(self, request, *args, **kwargs):
        tipo_talento = TipoTalento.objects.get(id=self.kwargs['pk'])
        tipo_talento.activo = False
        tipo_talento.save()
        messages.add_message(request, messages.SUCCESS, "Tipo de talento deshabilitado con éxito.")
        return JsonResponse({})


