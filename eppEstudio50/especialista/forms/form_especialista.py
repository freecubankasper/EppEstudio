from django import forms
from especialista.models.especialista import Especialista
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.sub_categoria import SubCategoria


class EspecialistaForm(forms.ModelForm):

    class Meta:
        model = Especialista

        fields = [
            'ci',
            'num_pasaporte',
            'otro_documento',
            'primer_nombre',
            'segundo_nombre',
            'primer_apellido',
            'segundo_apellido',
            'apodo',
            'sexo',
            'fecha_nacimiento',
            'pais',
            'municipio',
            'direccion',
            'correo',
            'telefono',
            'telefono_movil',
            'facebook',
            'subcategoria_servicio',
            'idioma',
            'habilidades',
            'precio_cup',
            'precio_mlc',
            'especialista_img',

        ]

        widgets = {
            'ci': forms.TextInput(attrs={'class': 'form-control'}),
            'num_pasaporte': forms.TextInput(attrs={'class': 'form-control'}),
            'otro_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'apodo': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control date date-picker fecha_nacimiento', 'readonly': True}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_movil': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'subcategoria_servicio': forms.Select(attrs={'class': 'form-control'}),
            'idioma': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'habilidades': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'precio_mlc': forms.TextInput(attrs={'class': 'form-control', 'min': 0}),
            'precio_cup': forms.TextInput(attrs={'class': 'form-control', 'min': 0}),

        }

        labels = {
            'ci': 'Número de CI',
            'num_pasaporte': 'Número de pasaporte',
            'otro_documento': 'Otro documento',
            'primer_nombre': 'Primer nombre',
            'segundo_nombre': 'Segundo nombre',
            'primer_apellido': 'Primer apellido',
            'segundo_apellido': 'Segundo apellido',
            'apodo': 'Apodo',
            'sexo': 'Sexo',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'pais': 'País',
            'municipio': 'Municipio',
            'direccion': 'Dirección',
            'correo': 'Correo',
            'telefono': 'Teléfono',
            'telefono_movil': 'Teléfono móvil',
            'facebook': 'Facebook',
            'subcategoria_servicio': 'Subcategoría de servicio',
            'idioma': 'Idioma',
            'habilidades': 'Habilidades',
            'precio_mlc': 'Precio en MLC',
            'precio_cup': 'Precio en CUP',

        }

    especialista_img = forms.ImageField(required=False, label='Especialista Imagen')

    def __init__(self, *args, **kwargs):
        super(EspecialistaForm, self).__init__(*args, **kwargs)
        categoria_servicio = CategoriaServicio.objects.get(id=2)
        categoria_servicio_id = categoria_servicio.id
        self.fields['subcategoria_servicio'].queryset = SubCategoria.objects.filter(categoria_servicio_id=categoria_servicio_id, activo=True).order_by('nombre')

