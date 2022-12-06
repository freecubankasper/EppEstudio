# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.categoria import Categoria


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria

        fields = [
            'nombre',
            'precio_cup',
            'precio_mlc',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_cup': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_mlc': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',
            'precio_cup': 'Precio en (CUP)',
            'precio_mlc': 'Precio en (MLC)',


        }
