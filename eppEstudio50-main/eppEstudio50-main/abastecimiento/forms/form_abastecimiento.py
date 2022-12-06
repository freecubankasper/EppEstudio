# -*- coding: utf-8 -*-
from django import forms

from abastecimiento.models.abastecimiento import Abastecimiento
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.sub_categoria import SubCategoria


class AbastecimientoForm(forms.ModelForm):
    class Meta:
        model = Abastecimiento

        fields = [
            'nombre',
            'sub_categoria',
            'direccion_domicilio',
            'nombre_producto',
            'descripcion',
            'abastecimiento_img',
            'precio_cup',
            'precio_mlc',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_categoria': forms.Select(attrs={'class': 'form-control'}),
            'direccion_domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'precio_mlc': forms.TextInput(attrs={'class': 'form-control', 'min': 0}),
            'precio_cup': forms.TextInput(attrs={'class': 'form-control', 'min': 0}),

        }

        labels = {
            'nombre': 'Nombre',
            'sub_categoria': 'Subcategoría de servicio',
            'direccion_domicilio': 'Dirección de domicilio',
            'nombre_producto': 'Nombre del producto',
            'descripcion': 'Descripción',
            'precio_mlc': 'Precio en MLC',
            'precio_cup': 'Precio en CUP',

        }

    abastecimiento_img = forms.ImageField(required=False, label='Imagen del abastecimiento')

    def __init__(self, *args, **kwargs):
        super(AbastecimientoForm, self).__init__(*args, **kwargs)
        categoria_servicio = CategoriaServicio.objects.get(id=5)
        categoria_servicio_id = categoria_servicio.id
        self.fields['sub_categoria'].queryset = SubCategoria.objects.filter(categoria_servicio_id=categoria_servicio_id, activo=True).order_by('nombre')
