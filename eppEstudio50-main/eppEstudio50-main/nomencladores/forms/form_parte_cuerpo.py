# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.parte_cuerpo import ParteCuerpo


class ParteCuerpoForm(forms.ModelForm):

    class Meta:
        model = ParteCuerpo

        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',

        }
