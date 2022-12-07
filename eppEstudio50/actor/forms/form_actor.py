from django import forms

from actor.models.actor import Actor
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.sub_categoria import SubCategoria


class ActorForm(forms.ModelForm):

    class Meta:
        model = Actor

        fields = [
            'ci',
            'num_pasaporte',
            'otro_documento',
            'categoria_lic_conduccion',
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
            'instagram',
            'subcategoria_servicio',
            'idioma',
            'habilidades',
            'estatura',
            'peso',
            'color_piel',
            'color_ojos',
            'tipo_pelo',
            'tendencia_racial',
            'cadera',
            'cintura',
            'hombro',
            'calzado',
            'precio_euro',
            'observaciones',
            'primera_img',
            'segunda_img',
            'tercera_img',
            'cuarta_img',
            'quinta_img',

        ]

        widgets = {
            'ci': forms.TextInput(attrs={'class': 'form-control'}),
            'num_pasaporte': forms.TextInput(attrs={'class': 'form-control'}),
            'otro_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria_lic_conduccion': forms.SelectMultiple(attrs={'class': 'form-control'}),
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
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'subcategoria_servicio': forms.Select(attrs={'class': 'form-control'}),
            'idioma': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'habilidades': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'estatura': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.TextInput(attrs={'class': 'form-control'}),
            'color_piel': forms.Select(attrs={'class': 'form-control'}),
            'color_ojos': forms.Select(attrs={'class': 'form-control'}),
            'tipo_pelo': forms.Select(attrs={'class': 'form-control'}),
            'tendencia_racial': forms.Select(attrs={'class': 'form-control'}),
            'cadera': forms.TextInput(attrs={'class': 'form-control'}),
            'cintura': forms.TextInput(attrs={'class': 'form-control'}),
            'hombro': forms.TextInput(attrs={'class': 'form-control'}),
            'calzado': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_euro': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'ci': 'Número de CI',
            'num_pasaporte': 'Número de pasaporte',
            'otro_documento': 'Otro documento',
            'categoria_lic_conduccion': 'Categoría de lic. conducción',
            'primer_nombre': 'Primer nombre',
            'segundo_nombre': 'Segundo nombre',
            'primer_apellido': 'Primer apellido',
            'segundo_apellido': 'Segundo apellido',
            'apodo': 'Alias',
            'sexo': 'Sexo',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'pais': 'País',
            'municipio': 'Municipio',
            'direccion': 'Dirección',
            'correo': 'Correo',
            'telefono': 'Teléfono',
            'telefono_movil': 'Teléfono móvil',
            'instagram': 'Instagram',
            'subcategoria_servicio': 'Subcategoría de servicio',
            'idioma': 'Idioma',
            'habilidades': 'Habilidades',
            'estatura': 'Estatura',
            'peso': 'Peso (Kg)',
            'color_piel': 'Color de la piel',
            'color_ojos': 'Color de los ojos',
            'tipo_pelo': 'Tipo de pelo',
            'tendencia_racial': 'Tendencia racial',
            'cadera': 'Caderas',
            'cintura': 'Cintura',
            'hombro': 'Hombros',
            'calzado': 'Calzado',
            'precio_euro': 'Precio en Euro',
            'observaciones': 'Observaciones',
        }

    primera_img = forms.ImageField(required=False, label='Pimera imagen')
    segunda_img = forms.ImageField(required=False, label='Segunda imagen')
    tercera_img = forms.ImageField(required=False, label='Tercera imagen')
    cuarta_img = forms.ImageField(required=False, label='Cuarta imagen')
    quinta_img = forms.ImageField(required=False, label='Quinta imagen')

    def __init__(self, *args, **kwargs):
        super(ActorForm, self).__init__(*args, **kwargs)
        categoria_servicio = CategoriaServicio.objects.get(id=3)
        categoria_servicio_id = categoria_servicio.id
        self.fields['subcategoria_servicio'].queryset = SubCategoria.objects.filter(categoria_servicio_id=categoria_servicio_id, activo=True).order_by('nombre')
        self.fields['correo'].required = False



    def clean(self):
        data = super().clean()
        if data['quinta_img'] and not data['cuarta_img'] and not data['tercera_img'] and not data['segunda_img'] and not data['primera_img']:
            self.add_error('cuarta_img', ('Debe insertar "Cuarta imagen" para luego insertar "Quinta imagen"'))
        elif data['quinta_img'] and data['cuarta_img'] and not data['tercera_img']:
            self.add_error('tercera', ('Debe insertar "Tercera imagen" para luego insertar "Cuarta imagen"'))
        elif data['primera_img'] and data['tercera_img'] and not data['segunda_img']:
            self.add_error('segunda_img', ('Debe insertar "Segunda imagen" para luego insertar "Tercera imagen"'))
        elif data['primera_img'] and data['segunda_img'] and data['cuarta_img'] and not data['tercera_img']:
            self.add_error('tercera_img', ('Debe insertar "Tercera imagen" para luego insertar "Cuarta imagen"'))
        elif data['primera_img'] and data['segunda_img'] and data['tercera_img'] and data['quinta_img'] and not data['cuarta_img']:
            self.add_error('tercera_img', ('Debe insertar "Cuarta imagen" para luego insertar "Quinta imagen"'))
        elif data['segunda_img'] and not data['primera_img']:
            self.add_error('primera_img', ('Debe insertar "Primera imagen" para luego insertar "Segunda imagen"'))
        elif data['tercera_img'] and not data['segunda_img']:
            self.add_error('segunda_img', ('Debe insertar "Segunda imagen" para luego insertar "Tercera imagen"'))
        elif data['cuarta_img'] and not data['tercera_img']:
            self.add_error('tercera_img', ('Debe insertar "Tercera imagen" para luego insertar "Cuarta imagen"'))
