from django import forms

from nomencladores.models.organismo import Organismo


class OrganismoForm(forms.ModelForm):

    class Meta:
        model = Organismo

        fields = [
            'nombre',
            'siglas',
            'hijode',

        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'siglas': forms.TextInput(attrs={'class': 'form-control'}),
            'hijode': forms.Select(attrs={'class': 'form-control'}),

        }

        labels = {
            'nombre': 'Nombre',
            'siglas': 'Siglas',
            'hijode': 'Pertenece al organismo',

        }
