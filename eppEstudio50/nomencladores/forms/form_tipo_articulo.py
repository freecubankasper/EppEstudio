# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.tipo_articulo import TipoArticulo


class TipoArticuloForm(forms.ModelForm):

    class Meta:
        model = TipoArticulo

        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',

        }
