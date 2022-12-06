# -*- coding: utf-8 -*-
from django import forms

from nomencladores.models.entidad import Entidad, TipoEntidad


class EntidadForm(forms.ModelForm):

    almacen = forms.ChoiceField(choices=(('', "Seleccione una opción..."), (True, "Sí"), (False, "No"),),
                                       widget=forms.Select(attrs={"class": "form-control"}), required=True,
                                       label='¿Tiene almacén?')

    entidad_importadora = forms.ChoiceField(choices=(('', "Seleccione una opción..."), (True, "Sí"), (False, "No"),),
                                       widget=forms.Select(attrs={"class": "form-control"}), required=True,
                                       label='¿Es entidad importadora?')


    class Meta:
        model = Entidad

        fields = [
            'nombre',
            'cod_reeup',
            'num_contrato',
            'pais',
            'municipio',
            'telefono',
            'direccion',
            'direccion_web',
            'correo',
            'num_lic_comercial_camara_comercio',
            'num_acta_protocolizacion',
            'identificacion_fiscal',
            'num_escritura_publica',
            'nombre_representante',
            'cargo_representante',
            'tipo_entidad_nacional',
            'tipo_entidad_extranjera',
            'entidad_importadora',
            'almacen',
            'observaciones',

        ]

        widgets = {
            'cod_reeup': forms.TextInput(attrs={'class': 'form-control'}),
            'num_contrato': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_web': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'num_lic_comercial_camara_comercio': forms.TextInput(attrs={'class': 'form-control'}),
            'num_acta_protocolizacion': forms.TextInput(attrs={'class': 'form-control'}),
            'identificacion_fiscal': forms.TextInput(attrs={'class': 'form-control'}),
            'num_escritura_publica': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_representante': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo_representante': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_entidad_nacional': forms.Select(attrs={'class': 'form-control'}),
            'tipo_entidad_extranjera': forms.Select(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),

        }

        labels = {
            'cod_reeup': 'Código REEUP (Para entidades nacionales)',
            'num_contrato': 'Número de Contrato',
            'nombre': 'Nombre de la entidad',
            'pais': 'País',
            'municipio': 'Municipio',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'direccion_web': 'Dirección web',
            'correo': 'Correo',
            'num_lic_comercial_camara_comercio': 'No.Lic.Comercial (Para sucursales comerciales extranjeras)',
            'num_acta_protocolizacion': 'No. Acta de Protocolización (Para entidades que operan desde el exterior)',
            'identificacion_fiscal': 'Identificación Fiscal Única (Para TPCP y DPL)',
            'num_escritura_publica': 'No. Escritura Pública Notarial (Para CNA Y MIPYMES)',
            'nombre_representante': 'Nombre del representante, gerente o director',
            'cargo_representante': 'Cargo del representante, gerente o director',
            'tipo_entidad_nacional': 'Tipo entidad nacional',
            'tipo_entidad_extranjera': 'Tipo entidad extranjera',
            'observaciones': 'Observaciones',

        }

    def __init__(self, *args, **kwargs):
        super(EntidadForm, self).__init__(*args, **kwargs)
        tipo_entidad_nacional = 'Nacional'
        tipo_entidad_extranjera = 'Extranjera'
        self.fields['tipo_entidad_nacional'].queryset = TipoEntidad.objects.filter(tipo__icontains=tipo_entidad_nacional, activo=True).order_by('nombre')
        self.fields['tipo_entidad_extranjera'].queryset = TipoEntidad.objects.filter(tipo__icontains=tipo_entidad_extranjera, activo=True).order_by('nombre')