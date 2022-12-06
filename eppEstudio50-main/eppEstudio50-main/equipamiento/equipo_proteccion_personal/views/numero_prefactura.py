# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, ListView
from django.views.generic.base import View
from core.utiles.permission_required import PermissionRequiredMixin
from equipo_proteccion_personal.forms.form_numero_prefactura import NumeroPrefacturaForm
from equipo_proteccion_personal.models.numero_prefactura import NumeroPrefactura
from nomencladores.models import Entidad


class ListadoNumerosPrefacturaView(PermissionRequiredMixin, ListView):
    model = NumeroPrefactura
    template_name = 'numero_prefactura/listado_numero_prefactura.html'
    paginate_by = 10
    permission = 'equipo_proteccion_personal.view_numeroprefactura'

    def get_queryset(self):
        numeros_prefactura = NumeroPrefactura.objects.all().order_by('-id')

        numero_prefactura = self.request.GET.get('numero_prefactura')
        if numero_prefactura is not None and numero_prefactura != "":
            numeros_prefactura = numeros_prefactura.filter(numero_prefactura__exact=numero_prefactura)

        entidad = self.request.GET.get('entidad')
        if entidad is not None and entidad != "":
            numeros_prefactura = numeros_prefactura.filter(entidad_id=entidad)

        return numeros_prefactura

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de números de prefactura'
        context['activar_equipos_proteccion_personal'] = True
        context['path'] = [
            {'name': 'Equipos de prtección personal'},
            {'name': 'Números de prefactura', 'href': reverse_lazy('numeros_prefactura')}
        ]

        # Filtros
        context['entidades'] = Entidad.objects.filter(activo=True).order_by('nombre')
        #

        return context


class RegistrarNumeroPrefacturaView(PermissionRequiredMixin, CreateView):
    model = NumeroPrefactura
    template_name = "numero_prefactura/form_numero_prefactura.html"
    form_class = NumeroPrefacturaForm
    success_url = reverse_lazy('numeros_prefactura')
    permission = 'equipo_proteccion_personal.add_numeroprefactura'

    def get_context_data(self, **kwargs):
        context = super(RegistrarNumeroPrefacturaView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar número de prefactura'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'número de prefactura'
        context['icono_form'] = 'plus'
        context['activar_equipos_proteccion_personal'] = True
        context['path'] = [
            {'name': 'Equipos de prtección personal'},
            {'name': 'Número de prefactura', 'href': reverse_lazy('numeros_prefactura')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_numero_prefactura')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Número de prefactura agregado con éxito.")
        return super(RegistrarNumeroPrefacturaView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Número de prefactura no agregado con éxito, revisar campos")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarNumeroPrefacturaView(PermissionRequiredMixin, UpdateView):
    model = NumeroPrefactura
    template_name = "numero_prefactura/form_numero_prefactura.html"
    form_class = NumeroPrefacturaForm
    success_url = reverse_lazy('numeros_prefactura')
    permission = 'equipo_proteccion_personal.change_numeroprefactura'

    def get_context_data(self, **kwargs):
        context = super(ModificarNumeroPrefacturaView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar número de prefactura'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "número de prefactura"
        context['icono_form'] = 'edit'
        context['activar_equipos_proteccion_personal'] = True
        context['path'] = [
            {'name': 'Equipos de prtección personal'},
            {'name': 'Número de prefactura', 'href': reverse_lazy('numeros_prefactura')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_numero_prefactura', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Número de prefactura modificado con éxito.")
        return super(ModificarNumeroPrefacturaView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Número de prefactura no modificado con éxito, revisar campos")
        return render(self.request, self.template_name, self.get_context_data())


class HabilitarNumeroPrefacturaView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.enable_numero_prefactura'

    def get(self, request, *args, **kwargs):
        numero_prefactura = NumeroPrefactura.objects.get(id=self.kwargs['pk'])
        numero_prefactura.activo = True
        numero_prefactura.save()
        messages.add_message(request, messages.SUCCESS, "Número de prefactura habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarNumeroPrefacturaView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.disable_numero_prefactura'

    def get(self, request, *args, **kwargs):
        numero_prefactura = NumeroPrefactura.objects.get(id=self.kwargs['pk'])
        numero_prefactura.activo = False
        numero_prefactura.save()
        messages.add_message(request, messages.SUCCESS, "Número de prefactura deshabilitado con éxito.")
        return JsonResponse({})


class EliminarNumeroPrefacturaView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.delete_numeroprefactura'

    def get(self, request, *args, **kwargs):
        numero_prefactura = NumeroPrefactura.objects.get(id=self.kwargs['pk'])
        numero_prefactura.delete()
        messages.add_message(request, messages.SUCCESS, "Número de prefactura eliminado con éxito.")
        return JsonResponse({})

