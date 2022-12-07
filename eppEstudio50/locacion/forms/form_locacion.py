# -*- coding: utf-8 -*-
from django import forms

from locacion.models.locacion import Locacion
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.sub_categoria import SubCategoria


class LocacionForm(forms.ModelForm):
    class Meta:
        model = Locacion

        fields = [
            'nombre',
            'sub_categoria',
            'direccion',
            'municipio',
            'tipo_suelo',
            'tipo_arquitectura',
            'tipo_lugar',
            'amanecer_img',
            'mediodia_img',
            'anochecer_img',
            'noche_img',
            'perfil_lugar_img',
            'propietario_lugar',
            'precio_cup',
            'precio_mlc',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_categoria': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'tipo_suelo': forms.Select(attrs={'class': 'form-control'}),
            'tipo_arquitectura': forms.Select(attrs={'class': 'form-control'}),
            'tipo_lugar': forms.Select(attrs={'class': 'form-control'}),
            'propietario_lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_mlc': forms.TextInput(attrs={'class': 'form-control', 'min': 0}),
            'precio_cup': forms.TextInput(attrs={'class': 'form-control', 'min': 0}),

        }

        labels = {
            'nombre': 'Nombre',
            'sub_categoria': 'Subcategoría de servicio',
            'direccion': 'Dirección',
            'municipio': 'Municipio',
            'tipo_suelo': 'Tipo de suelo',
            'tipo_arquitectura': 'Tipo de arquitectura',
            'tipo_lugar': 'Tipo de lugar',
            'propietario_lugar': 'Propietario del lugar',
            'precio_cup': 'Precio en CUP',
            'precio_mlc': 'Precio en MLC',

        }

    amanecer_img = forms.ImageField(required=False, label='Foto amanecer')
    mediodia_img = forms.ImageField(required=False, label='Foto mediodia')
    anochecer_img = forms.ImageField(required=False, label='Foto anochecer')
    noche_img = forms.ImageField(required=False, label='Foto noche')
    perfil_lugar_img = forms.ImageField(required=False, label='Foto perfil del lugar')

    def __init__(self, *args, **kwargs):
        super(LocacionForm, self).__init__(*args, **kwargs)
        categoria_servicio = CategoriaServicio.objects.get(id=6)
        categoria_servicio_id = categoria_servicio.id
        self.fields['sub_categoria'].queryset = SubCategoria.objects.filter(categoria_servicio_id=categoria_servicio_id, activo=True).order_by('nombre')
