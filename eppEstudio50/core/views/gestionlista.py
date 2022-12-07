from datetime import timedelta

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.dateparse import parse_datetime
from django.views import View

from llamado.models.llamado_proyecto import LlamadoProyecto
from proyecto.models import Proyecto


class Adicionarmilista(View):

    def get_context_data(self, **kwargs):
        producto_id = self.kwargs['producto_id']
        subcategoria = self.kwargs['subcategoria']
        nombre = self.kwargs['nombre']
        cantidad = self.kwargs['cantidad']
        lista = []
        lista.append(nombre)
        return render(self.request)
