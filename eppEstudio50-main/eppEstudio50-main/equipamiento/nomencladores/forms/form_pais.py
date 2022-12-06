from django import forms

from nomencladores.models.pais import Pais


class PaisForm(forms.ModelForm):

    class Meta:
        model = Pais

        fields = [
            'nombre',
            'nacionalidad',
            'siglas',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'siglas': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',
            'nacionalidad': 'Nacionalidad',
            'siglas': 'Siglas',


        }
