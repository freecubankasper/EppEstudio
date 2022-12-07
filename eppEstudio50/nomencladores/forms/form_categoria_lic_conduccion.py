# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.categoria_lic_conduccion import CategoriaLicenciaConduccion


class CategoriaLicenciaConduccionForm(forms.ModelForm):

    class Meta:
        model = CategoriaLicenciaConduccion

        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',


        }
