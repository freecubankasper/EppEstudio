# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.idioma import Idioma


class IdiomaForm(forms.ModelForm):

    class Meta:
        model = Idioma

        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',

        }
