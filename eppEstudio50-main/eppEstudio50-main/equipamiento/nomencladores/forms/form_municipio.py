from django import forms

from nomencladores.models import Provincia
from nomencladores.models.municipio import Municipio


class MunicipioForm(forms.ModelForm):

    class Meta:
        model = Municipio

        fields = [
            'nombre',
            'provincia',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'provincia': forms.Select(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',
            'provincia': 'Provincia',

        }
