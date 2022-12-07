from django import forms

from evento.models.evento_proyecto import EventoProyecto


class EventoProyectoForm(forms.ModelForm):

    class Meta:
        model = EventoProyecto
        fields = [
            'titulo',
            'subcategoria_servicio',
            'actor',
            'equipamiento',
            'descripcion',
            'fecha_inicio_evento',
            'fecha_fin_evento',

        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subcategoria_servicio': forms.Select(attrs={'class': 'form-control'}),
            'actor': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'equipamiento': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'fecha_inicio_evento': forms.TextInput(attrs={'class': 'form-control', 'id': 'fecha_inicio_evento', 'readonly': True}),
            'fecha_fin_evento': forms.TextInput(attrs={'class': 'form-control', 'id': 'fecha_fin_evento', 'readonly': True}),

        }

        labels = {
            'titulo': 'Título',
            'subcategoria_servicio': 'Subcategoría de servicio',
            'actor': 'Actor',
            'equipamiento': 'Equipamiento',
            'descripcion': 'Descripción',
            'fecha_inicio_evento': 'Fecha de inicio',
            'fecha_fin_evento': 'Fecha de finalización',

        }
