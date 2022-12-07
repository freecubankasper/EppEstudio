# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_parte_cuerpo import ParteCuerpoForm
from nomencladores.models.parte_cuerpo import ParteCuerpo


class ListadoPartesCuerpoView(PermissionRequiredMixin, ListView):
    model = ParteCuerpo
    template_name = 'parte_cuerpo/listado_partes_cuerpo.html'
    paginate_by = 10
    permission = 'nomencladores.view_partecuerpo'

    def get_queryset(self):
        parte_cuerpo = ParteCuerpo.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            parte_cuerpo = parte_cuerpo.filter(nombre__icontains=q)

        return parte_cuerpo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de partes del cuerpo'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Partes del cuerpo', 'href': reverse_lazy('partes_cuerpo')}
        ]
        return context


class RegistrarParteCuerpoView(PermissionRequiredMixin, CreateView):
    model = ParteCuerpo
    template_name = "parte_cuerpo/parte_cuerpo_form.html"
    form_class = ParteCuerpoForm
    success_url = reverse_lazy('partes_cuerpo')
    permission = 'nomencladores.add_partecuerpo'

    def get_context_data(self, **kwargs):
        context = super(RegistrarParteCuerpoView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar parte del cuerpo'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'parte del cuerpo'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Parte del cuerpo', 'href': reverse_lazy('partes_cuerpo')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_parte_cuerpo')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Parte del cuerpo agregada con éxito.")
        return super(RegistrarParteCuerpoView, self).form_valid(form)


class ModificarParteCuerpoView(PermissionRequiredMixin, UpdateView):
    model = ParteCuerpo
    template_name = "parte_cuerpo/parte_cuerpo_form.html"
    form_class = ParteCuerpoForm
    success_url = reverse_lazy('partes_cuerpo')
    permission = 'nomencladores.change_partecuerpo'

    def get_context_data(self, **kwargs):
        context = super(ModificarParteCuerpoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar parte del cuerpo'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "parte del cuerpo"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Parte del cuerpo', 'href': reverse_lazy('partes_cuerpo')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_parte_cuerpo', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Parte del cuerpo modificada con éxito.")
        return super(ModificarParteCuerpoView, self).form_valid(form)


class HabilitarParteCuerpoView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_parte_cuerpo'

    def get(self, request, *args, **kwargs):
        parte_cuerpo = ParteCuerpo.objects.get(id=self.kwargs['pk'])
        parte_cuerpo.activo = True
        parte_cuerpo.save()
        messages.add_message(request, messages.SUCCESS, "Parte del cuerpo habilitada con éxito.")
        return JsonResponse({})


class DeshabilitarParteCuerpoView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_parte_cuerpo'

    def get(self, request, *args, **kwargs):
        parte_cuerpo = ParteCuerpo.objects.get(id=self.kwargs['pk'])
        parte_cuerpo.activo = False
        parte_cuerpo.save()
        messages.add_message(request, messages.SUCCESS, "Parte del cuerpo deshabilitada con éxito.")
        return JsonResponse({})


