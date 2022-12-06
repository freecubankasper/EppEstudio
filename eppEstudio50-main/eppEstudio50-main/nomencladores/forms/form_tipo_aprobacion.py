# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.tipo_aprobacion import TipoAprobacion


class TipoAprobacionForm(forms.ModelForm):

    class Meta:
        model = TipoAprobacion

        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',

        }
