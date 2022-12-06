# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.marca_transporte import MarcaTransporte


class MarcaTransporteForm(forms.ModelForm):

    class Meta:
        model = MarcaTransporte

        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',

        }
