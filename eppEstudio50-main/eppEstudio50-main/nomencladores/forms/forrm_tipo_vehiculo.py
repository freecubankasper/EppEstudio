# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.tipo_vehiculo import TipoVehiculo


class TipoVehiculoForm(forms.ModelForm):

    class Meta:
        model = TipoVehiculo

        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',

        }
