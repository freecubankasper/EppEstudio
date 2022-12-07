
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.template.context_processors import request
from django.views.generic import TemplateView
from core.utiles.permission_required import PermissionRequiredMixin

from core.utiles.filters import EquipamientoFilter, MisproyectosFilter
from equipamiento.models.equipamiento import Equipamiento
from nomencladores.models.categoria import Categoria
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.marca_comercial_registrada import MarcaComercialRegistrada
from nomencladores.models.sub_categoria import SubCategoria
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from django.template.loader import get_template


from django import template

from proyecto.models import Proyecto

register = template.Library()

class MisProyectosView(PermissionRequiredMixin,ListView):
    template_name = 'misproyectos.html'
    model = Proyecto
    permission = 'evento.view_eventoequipamiento'


    def get_context_data(self, **kwargs):
        usuario = self.request.user
        context = super().get_context_data(**kwargs)
        context['misproyectos'] = MisproyectosFilter(self.request.GET,queryset=self.get_queryset().filter(usuario=usuario))
        context['categorias'] = Categoria.objects.all()

        return context