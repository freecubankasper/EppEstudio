# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.marca_comercial_registrada import MarcaComercialRegistrada


class MarcaComercialRegistradaForm(forms.ModelForm):

    class Meta:
        model = MarcaComercialRegistrada

        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',

        }
