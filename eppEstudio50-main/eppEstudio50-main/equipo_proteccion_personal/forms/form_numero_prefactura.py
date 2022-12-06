from django import forms

from equipo_proteccion_personal.models.numero_prefactura import NumeroPrefactura


class NumeroPrefacturaForm(forms.ModelForm):

    class Meta:
        model = NumeroPrefactura

        fields = [
            'numero_prefactura',
            'entidad',
        ]

        widgets = {
            'numero_prefactura': forms.TextInput(attrs={'class': 'form-control'}),
            'entidad': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'numero_prefactura': 'Número de prefactura',
            'entidad': 'Entidad',
        }
