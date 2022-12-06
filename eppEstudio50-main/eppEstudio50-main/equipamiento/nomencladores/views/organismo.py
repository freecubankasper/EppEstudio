# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_organismo import OrganismoForm
from nomencladores.models.organismo import Organismo


class ListadoOrganismosView(PermissionRequiredMixin, ListView):
    model = Organismo
    template_name = 'organismo/listado_organismos.html'
    paginate_by = 10
    permission = 'nomencladores.view_organismo'

    def get_queryset(self):
        organismos = Organismo.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            organismos = organismos.filter(nombre__icontains=q)

        return organismos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de organismos'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Organismos', 'href': reverse_lazy('organismos')}
        ]
        return context


class RegistrarOrganismoView(PermissionRequiredMixin, CreateView):
    model = Organismo
    template_name = "organismo/organismo_form.html"
    form_class = OrganismoForm
    success_url = reverse_lazy('organismos')
    permission = 'nomencladores.add_organismo'

    def get_context_data(self, **kwargs):
        context = super(RegistrarOrganismoView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar organismo'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'organismo'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Organismo', 'href': reverse_lazy('organismos')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_organismo')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Organismo agregado con éxito.")
        return super(RegistrarOrganismoView, self).form_valid(form)


class ModificarOrganismoView(PermissionRequiredMixin, UpdateView):
    model = Organismo
    template_name = "organismo/organismo_form.html"
    form_class = OrganismoForm
    success_url = reverse_lazy('organismos')
    permission = 'nomencladores.change_organismo'

    def get_context_data(self, **kwargs):
        context = super(ModificarOrganismoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar organismo'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "organismo"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Organismo', 'href': reverse_lazy('organismos')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_organismo', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Organismo modificado con éxito.")
        return super(ModificarOrganismoView, self).form_valid(form)


class HabilitarOrganismoView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_organismo'

    def get(self, request, *args, **kwargs):
        organismo = Organismo.objects.get(id=self.kwargs['pk'])
        organismo.activo = True
        organismo.save()
        messages.add_message(request, messages.SUCCESS, "Organismo habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarOrganismoView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_organismo'

    def get(self, request, *args, **kwargs):
        organismo = Organismo.objects.get(id=self.kwargs['pk'])
        organismo.activo = False
        organismo.save()
        messages.add_message(request, messages.SUCCESS, "Organismo deshabilitado con éxito.")
        return JsonResponse({})


