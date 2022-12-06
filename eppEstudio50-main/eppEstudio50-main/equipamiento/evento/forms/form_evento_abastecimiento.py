from django import forms

from evento.models.evento_abastecimiento import EventoAbastecimiento


class EventoAbastecimientoForm(forms.ModelForm):

    class Meta:
        model = EventoAbastecimiento
        fields = [
            'titulo',
            'descripcion',
            'fecha_inicio_evento',
            'fecha_fin_evento',

        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'fecha_inicio_evento': forms.TextInput(attrs={'class': 'form-control', 'id': 'fecha_inicio_evento', 'readonly': True}),
            'fecha_fin_evento': forms.TextInput(attrs={'class': 'form-control', 'id': 'fecha_fin_evento', 'readonly': True}),

        }

        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'fecha_inicio_evento': 'Fecha de inicio',
            'fecha_fin_evento': 'Fecha de finalización',

        }
