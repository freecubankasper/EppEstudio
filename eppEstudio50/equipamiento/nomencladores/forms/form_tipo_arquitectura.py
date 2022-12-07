# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.tipo_arquitectura import TipoArquitectura


class TipoArquitecturaForm(forms.ModelForm):

    class Meta:
        model = TipoArquitectura

        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',

        }
