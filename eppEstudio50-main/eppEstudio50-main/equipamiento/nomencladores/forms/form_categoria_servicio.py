# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.categoria_servicio import CategoriaServicio


class CategoriaServicioForm(forms.ModelForm):

    class Meta:
        model = CategoriaServicio

        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',


        }
