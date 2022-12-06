# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.tipo_lugar import TipoLugar


class TipoLugarForm(forms.ModelForm):

    class Meta:
        model = TipoLugar

        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',

        }
