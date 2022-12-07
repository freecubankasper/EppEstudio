# -*- coding: utf-8 -*-
from django import forms

from llamado.models.llamado_proyecto import LlamadoProyecto


class LlamadoProyectoForm(forms.ModelForm):
    class Meta:
        model = LlamadoProyecto

        fields = [
            'titulo',
            'centro_emergencia',
            'direccion_centro_emergencia',
            'production_call',
            'courtesy_meal',
            'crew_call',
            'artist_call',
            'ready_to_shoot',
            'first_meal',
            'second_meal',
            'third_meal',
            'estimated_camera_wrap',
            'observaciones',

        ]

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'centro_emergencia': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_centro_emergencia': forms.TextInput(attrs={'class': 'form-control'}),
            'production_call': forms.TextInput(attrs={'class': 'form-control', 'id': 'production_call', 'readonly': True}),
            'courtesy_meal': forms.TextInput(attrs={'class': 'form-control', 'id': 'courtesy_meal', 'readonly': True}),
            'crew_call': forms.TextInput(attrs={'class': 'form-control', 'id': 'crew_call', 'readonly': True}),
            'artist_call': forms.TextInput(attrs={'class': 'form-control', 'id': 'artist_call', 'readonly': True}),
            'ready_to_shoot': forms.TextInput(attrs={'class': 'form-control', 'id': 'ready_to_shoot', 'readonly': True}),
            'first_meal': forms.TextInput(attrs={'class': 'form-control', 'id': 'first_meal', 'readonly': True}),
            'second_meal': forms.TextInput(attrs={'class': 'form-control', 'id': 'second_meal', 'readonly': True}),
            'third_meal': forms.TextInput(attrs={'class': 'form-control', 'id': 'third_meal', 'readonly': True}),
            'estimated_camera_wrap': forms.TextInput(attrs={'class': 'form-control', 'id': 'estimated_camera_wrap', 'readonly': True}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),

        }

        labels = {
            'titulo': 'Título',
            'centro_emergencia': 'Centro de emergencia',
            'direccion_centro_emergencia': 'Dirección centro de emergencia',
            'production_call': 'Llamada de producción',
            'courtesy_meal': 'Comida de cortesía',
            'crew_call': 'Llamada de tripulación',
            'artist_call': 'Llamada de artista',
            'ready_to_shoot': 'Listo para disparar',
            'first_meal': 'Primera comida',
            'second_meal': 'Segunda comida',
            'third_meal': 'Tercera comida',
            'estimated_camera_wrap': 'Envoltura de cámara estimada',
            'observaciones': 'Observaciones',

        }
