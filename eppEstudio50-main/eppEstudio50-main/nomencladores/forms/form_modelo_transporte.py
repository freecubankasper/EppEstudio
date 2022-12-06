# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.modelo_transporte import Modelo


class ModeloForm(forms.ModelForm):

    class Meta:
        model = Modelo

        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',

        }
