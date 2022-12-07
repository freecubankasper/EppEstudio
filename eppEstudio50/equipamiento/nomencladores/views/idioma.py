# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_idioma import IdiomaForm
from nomencladores.models.idioma import Idioma


class ListadoIdiomasView(PermissionRequiredMixin, ListView):
    model = Idioma
    template_name = 'idioma/listado_idiomas.html'
    paginate_by = 10
    permission = 'nomencladores.view_idioma'

    def get_queryset(self):
        idiomas = Idioma.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            idiomas = idiomas.filter(nombre__icontains=q)

        return idiomas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de idiomas'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Idiomas', 'href': reverse_lazy('idiomas')}
        ]
        return context


class RegistrarIdiomaView(PermissionRequiredMixin, CreateView):
    model = Idioma
    template_name = "idioma/idioma_form.html"
    form_class = IdiomaForm
    success_url = reverse_lazy('idiomas')
    permission = 'nomencladores.add_idioma'

    def get_context_data(self, **kwargs):
        context = super(RegistrarIdiomaView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar idioma'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'idioma'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Idioma', 'href': reverse_lazy('idiomas')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_idioma')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Idioma agregado con éxito.")
        return super(RegistrarIdiomaView, self).form_valid(form)


class ModificarIdiomaView(PermissionRequiredMixin, UpdateView):
    model = Idioma
    template_name = "idioma/idioma_form.html"
    form_class = IdiomaForm
    success_url = reverse_lazy('idiomas')
    permission = 'nomencladores.change_idioma'

    def get_context_data(self, **kwargs):
        context = super(ModificarIdiomaView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar idioma'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "idioma"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Idioma', 'href': reverse_lazy('idiomas')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_idioma', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Idioma modificado con éxito.")
        return super(ModificarIdiomaView, self).form_valid(form)


class HabilitarIdiomaView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_idioma'

    def get(self, request, *args, **kwargs):
        idioma = Idioma.objects.get(id=self.kwargs['pk'])
        idioma.activo = True
        idioma.save()
        messages.add_message(request, messages.SUCCESS, "Idioma habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarIdiomaView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_idioma'

    def get(self, request, *args, **kwargs):
        idioma = Idioma.objects.get(id=self.kwargs['pk'])
        idioma.activo = False
        idioma.save()
        messages.add_message(request, messages.SUCCESS, "Idioma deshabilitado con éxito.")
        return JsonResponse({})


