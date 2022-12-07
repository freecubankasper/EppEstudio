from django import forms

from nomencladores.models.provincia import Provincia


class ProvinciaForm(forms.ModelForm):

    class Meta:
        model = Provincia

        fields = [
            'nombre',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',


        }
