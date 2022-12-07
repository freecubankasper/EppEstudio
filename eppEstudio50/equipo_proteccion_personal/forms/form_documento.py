import os

from django import forms

from equipo_proteccion_personal.models.documento import Documento


class DocumentoForm(forms.ModelForm):

    class Meta:
        model = Documento

        fields = [
            'nombre',
            'documento',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'nombre': 'Nombre',
        }

    documento = forms.FileField(required=True, label='Documento (Solo admite formato pdf)')

