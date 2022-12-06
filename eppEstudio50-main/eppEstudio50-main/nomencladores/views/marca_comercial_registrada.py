# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_marca_comercial_registrada import MarcaComercialRegistradaForm
from nomencladores.models.marca_comercial_registrada import MarcaComercialRegistrada


class ListadoMarcasComercialesRegistradasView(PermissionRequiredMixin, ListView):
    model = MarcaComercialRegistrada
    template_name = 'marca_comercial_registrada/listado_marcas_comercial_registrada.html'
    paginate_by = 10
    permission = 'nomencladores.view_marcacomercialregistrada'

    def get_queryset(self):
        mracas_comercial = MarcaComercialRegistrada.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            mracas_comercial = mracas_comercial.filter(nombre__icontains=q)

        return mracas_comercial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de marcas comerciales registradas'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Marcas comerciales registradas', 'href': reverse_lazy('marcas_comercial_registrada')}
        ]
        return context


class RegistrarMarcaComercialRegistradaView(PermissionRequiredMixin, CreateView):
    model = MarcaComercialRegistrada
    template_name = "marca_comercial_registrada/marca_comercial_registrada_form.html"
    form_class = MarcaComercialRegistradaForm
    success_url = reverse_lazy('marcas_comercial_registrada')
    permission = 'nomencladores.add_marcacomercialregistrada'

    def get_context_data(self, **kwargs):
        context = super(RegistrarMarcaComercialRegistradaView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar marca comercial registrada'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'marca comercial registrada'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Marca comercial registrada', 'href': reverse_lazy('marcas_comercial_registrada')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_marca_comercial_registrada')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Marca comercial registrada agregada con éxito.")
        return super(RegistrarMarcaComercialRegistradaView, self).form_valid(form)


class ModificarMarcaComercialRegistradaView(PermissionRequiredMixin, UpdateView):
    model = MarcaComercialRegistrada
    template_name = "marca_comercial_registrada/marca_comercial_registrada_form.html"
    form_class = MarcaComercialRegistradaForm
    success_url = reverse_lazy('marcas_comercial_registrada')
    permission = 'nomencladores.change_marcacomercialregistrada'

    def get_context_data(self, **kwargs):
        context = super(ModificarMarcaComercialRegistradaView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar marca comercial registrada'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "marca comercial registrada"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Marca comercial registrada', 'href': reverse_lazy('marcas_comercial_registrada')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_marca_comercial_registrada', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Marca comercial registrada modificada con éxito.")
        return super(ModificarMarcaComercialRegistradaView, self).form_valid(form)


class HabilitarMarcaComercialRegistradaView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_marca_comercial_registrada'

    def get(self, request, *args, **kwargs):
        marca_comercial = MarcaComercialRegistrada.objects.get(id=self.kwargs['pk'])
        marca_comercial.activo = True
        marca_comercial.save()
        messages.add_message(request, messages.SUCCESS, "Marca comercial registrada habilitada con éxito.")
        return JsonResponse({})


class DeshabilitarMarcaComercialRegistradaView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_marca_comercial_registrada'

    def get(self, request, *args, **kwargs):
        marca_comercial = MarcaComercialRegistrada.objects.get(id=self.kwargs['pk'])
        marca_comercial.activo = False
        marca_comercial.save()
        messages.add_message(request, messages.SUCCESS, "Marca comercial registrada deshabilitada con éxito.")
        return JsonResponse({})


