# -*- coding: utf-8 -*-
from django import forms
from nomencladores.models.sub_categoria import SubCategoria


class SubCategoriaForm(forms.ModelForm):

    class Meta:
        model = SubCategoria

        fields = [
            'nombre',
            'categoria_servicio',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria_servicio': forms.Select(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',
            'categoria_servicio': 'Categoría de servicio',


        }