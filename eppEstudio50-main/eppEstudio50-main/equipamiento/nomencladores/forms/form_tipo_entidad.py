# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.entidad import TipoEntidad


class TipoEntidadForm(forms.ModelForm):

    class Meta:
        model = TipoEntidad

        fields = [
            'nombre',
            'tipo',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',
            'tipo': 'Tipo',

        }


