# -*- coding: utf-8 -*-
from django import forms
from nomencladores.models.tipo_talento import TipoTalento


class TipoTalentoForm(forms.ModelForm):

    class Meta:
        model = TipoTalento

        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',

        }
