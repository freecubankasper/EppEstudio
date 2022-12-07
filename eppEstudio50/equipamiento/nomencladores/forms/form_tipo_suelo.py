# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.tipo_suelo import TipoSuelo


class TipoSueloForm(forms.ModelForm):

    class Meta:
        model = TipoSuelo

        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',

        }
