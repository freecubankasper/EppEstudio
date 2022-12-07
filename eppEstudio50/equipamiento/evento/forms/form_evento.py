from django import forms
from evento.models.evento import Evento


class EventoForm(forms.ModelForm):

    class Meta:
        model = Evento
        fields = [
            'titulo',
            'subcategoria_servicio',
            'categoria_servicio',
            'actor',
            'equipamiento',
            'fecha_inicio_evento',
            'fecha_fin_evento',

        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subcategoria_servicio': forms.Select(attrs={'class': 'form-control'}),
            'categoria_servicio': forms.Select(attrs={'class': 'form-control'}),
            'actor': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'equipamiento': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'fecha_inicio_evento': forms.TextInput(attrs={'class': 'form-control', 'id': 'fecha_inicio_evento', 'readonly': True}),
            'fecha_fin_evento': forms.TextInput(attrs={'class': 'form-control', 'id': 'fecha_fin_evento', 'readonly': True}),

        }

        labels = {
            'titulo': 'Título',
            'subcategoria_servicio': 'Subcategoría de servicio',
            'categoria_servicio': 'Categoría de servicio',
            'actor': 'Actor',
            'equipamiento': 'Equipamiento',
            'fecha_inicio_evento': 'Fecha de inicio',
            'fecha_fin_evento': 'Fecha de finalización',

        }
