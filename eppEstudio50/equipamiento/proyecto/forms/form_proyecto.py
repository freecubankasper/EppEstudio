from django import forms
from proyecto.models import Proyecto


class ProyectoForm(forms.ModelForm):

    class Meta:
        model = Proyecto
        fields = [
            'nombre',
            'categoria',
            'fecha_inicio',
            'fecha_fin',

        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.TextInput(attrs={'class': 'form-control date date-picker fecha_inicio', 'readonly': True}),
            'fecha_fin': forms.TextInput(attrs={'class': 'form-control date date-picker fecha_fin', 'readonly': True}),

        }

        labels = {
            'nombre': 'Nombre del Proyecto',
            'categoria': 'Tipo de Proyecto',
            'fecha_inicio': 'Fecha de Inicio',
            'fecha_fin': 'Fecha Final',

        }
