
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.template.context_processors import request
from django.views.generic import TemplateView

from core.utiles.filters import EquipamientoFilter, EspecialidadesFilter
from equipamiento.models.equipamiento import Equipamiento
from especialista.models.especialista import Especialista
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.marca_comercial_registrada import MarcaComercialRegistrada
from nomencladores.models.sub_categoria import SubCategoria
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from django.template.loader import get_template


from django import template

register = template.Library()

class EspecialidadesView(ListView):
    template_name = 'especialidades.html'
    model = Especialista

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_servicio = CategoriaServicio.objects.get(id=2)
        categoria_servicio_id = categoria_servicio.id
        context['especialidades'] = EspecialidadesFilter(self.request.GET,queryset=self.get_queryset())
        context['subcategorias_servicio'] = SubCategoria.objects.filter(categoria_servicio_id=categoria_servicio_id,
                                                                        activo=True).order_by('nombre')

        #
        return context