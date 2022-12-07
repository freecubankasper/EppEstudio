# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.sub_categoria import SubCategoria
from transporte.models.transporte import Transporte


class TransporteForm(forms.ModelForm):
    class Meta:
        model = Transporte

        fields = [
            'tipo_vehiculo',
            'marca',
            'modelo',
            'color',
            'sub_categoria',
            'peso_maximo',
            'cantidad_persona',
            'persona_chofer',
            'anno_fabricacion',
            'precio_mlc',
            'precio_cup',
            'transporte_img',

        ]

        widgets = {
            'tipo_vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'modelo': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_categoria': forms.Select(attrs={'class': 'form-control'}),
            'peso_maximo': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_persona': forms.TextInput(attrs={'class': 'form-control', 'min': 0}),
            'persona_chofer': forms.TextInput(attrs={'class': 'form-control'}),
            'anno_fabricacion': forms.TextInput(attrs={'class': 'form-control', 'min': 0}),
            'precio_mlc': forms.TextInput(attrs={'class': 'form-control', 'min': 0}),
            'precio_cup': forms.TextInput(attrs={'class': 'form-control', 'min': 0}),

        }

        labels = {
            'tipo_vehiculo': 'Tipo de vehículo',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'color': 'Color',
            'sub_categoria': 'Subcategoría de servicio',
            'peso_maximo': 'Peso máximo',
            'cantidad_persona': 'Peso máximo',
            'persona_chofer': 'Persona (chofer)',
            'anno_fabricacion': 'Año de fabricación',
            'precio_mlc': 'Precio en MLC',
            'precio_cup': 'Precio en CUP',

        }

    transporte_img = forms.ImageField(required=False, label='Imagen del transporte')

    def __init__(self, *args, **kwargs):
        super(TransporteForm, self).__init__(*args, **kwargs)
        categoria_servicio = CategoriaServicio.objects.get(id=9)
        categoria_servicio_id = categoria_servicio.id
        self.fields['sub_categoria'].queryset = SubCategoria.objects.filter(categoria_servicio_id=categoria_servicio_id, activo=True).order_by('nombre')
