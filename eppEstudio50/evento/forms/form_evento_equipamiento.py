from django import forms

from evento.models.evento_equipamiento import EventoEquipamiento


class EventoEquipamientoForm(forms.ModelForm):

    class Meta:
        model = EventoEquipamiento
        fields = [
            'titulo',
            'cantidad',
            'descripcion',
            'fecha_inicio_evento',
            'fecha_fin_evento',

        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'fecha_inicio_evento': forms.TextInput(attrs={'class': 'form-control', 'id': 'fecha_inicio_evento', 'readonly': True}),
            'fecha_fin_evento': forms.TextInput(attrs={'class': 'form-control', 'id': 'fecha_fin_evento', 'readonly': True}),

        }

        labels = {
            'titulo': 'Título',
            'cantidad': 'Cantidad',
            'descripcion': 'Descripción',
            'fecha_inicio_evento': 'Fecha de inicio',
            'fecha_fin_evento': 'Fecha de finalización',

        }
