# -*- coding: utf-8 -*-
from django import forms

from equipamiento.models.equipamiento import Equipamiento
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.sub_categoria import SubCategoria


class EquipamientoForm(forms.ModelForm):
    class Meta:
        model = Equipamiento

        fields = [
            'nombre',
            'sub_categoria',
            'marca',
            'cantidad',
            'descripcion',
            'equipamiento_img',
            'precio_cup',
            'precio_mlc',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_categoria': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'precio_mlc': forms.TextInput(attrs={'class': 'form-control', 'min': 0}),
            'precio_cup': forms.TextInput(attrs={'class': 'form-control', 'min': 0}),

        }

        labels = {
            'nombre': 'Nombre',
            'sub_categoria': 'Subcategoría de servicio',
            'marca': 'Marca comercial',
            'descripcion': 'Descripción',
            'precio_mlc': 'Precio en MLC',
            'precio_cup': 'Precio en CUP',

        }

    equipamiento_img = forms.ImageField(required=False, label='Imagen del equipamiento')

    def __init__(self, *args, **kwargs):
        super(EquipamientoForm, self).__init__(*args, **kwargs)
        categoria_servicio = CategoriaServicio.objects.get(id=1)
        categoria_servicio_id = categoria_servicio.id
        self.fields['sub_categoria'].queryset = SubCategoria.objects.filter(categoria_servicio_id=categoria_servicio_id, activo=True).order_by('nombre')
