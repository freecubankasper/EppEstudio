from django import forms
from equipo_proteccion_personal.models.equipo_proteccion_personal import EquipoProteccionPersonal
from equipo_proteccion_personal.models.factura import Factura
from equipo_proteccion_personal.models.numero_prefactura import NumeroPrefactura
from nomencladores.models import Entidad


class EquipoProteccionPersonalForm(forms.ModelForm):

    muestras_equipo = forms.ChoiceField(choices=(('', "Seleccione una opción..."), (True, "Sí"), (False, "No"),),
                                       widget=forms.Select(attrs={"class": "form-control"}), required=True,
                                       label='¿Muestras del equipo?')

    class Meta:
        model = EquipoProteccionPersonal

        fields = [
            'nombre',
            'categoria',
            'tipo_aprobacion',
            'entidad_importadora',
            'fecha_vencimiento_certificado',
            'marca_comercial_registrada',
            'modelo',
            'numero_referencia',
            'clientes_usuarios',
            'muestras_equipo',
            'numero_prefactura',
            'primera_img',
            'segunda_img',
            'tercera_img',
            'parte_cuerpo',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'tipo_aprobacion': forms.Select(attrs={'class': 'form-control'}),
            'entidad_importadora': forms.Select(attrs={'class': 'form-control'}),
            'fecha_vencimiento_certificado': forms.TextInput(attrs={'class': 'form-control date date-picker fecha_vencimiento_certificado', 'readonly': True}),
            'marca_comercial_registrada': forms.Select(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_referencia': forms.TextInput(attrs={'class': 'form-control'}),
            'clientes_usuarios': forms.TextInput(attrs={'class': 'form-control'}),
            'parte_cuerpo': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'numero_prefactura': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'nombre': 'Nombre',
            'categoria': 'Categoría del equipo',
            'tipo_aprobacion': 'Tipo de Aprobación',
            'entidad_importadora': 'Entidad importadora',
            'fecha_vencimiento_certificado': 'Fecha de vencimiento del certificado',
            'marca_comercial_registrada': 'Marca comercial registrada',
            'modelo': 'Modelo',
            'numero_referencia': 'No. de referencia',
            'clientes_usuarios': 'Clientes  o usuarios fundamentales del equipo',
            'parte_cuerpo': 'Parte del cuerpo que protege',
            'numero_prefactura': 'Número de prefactura',

        }

    primera_img = forms.ImageField(required=False, label='Pimera imagen')
    segunda_img = forms.ImageField(required=False, label='Segunda imagen')
    tercera_img = forms.ImageField(required=False, label='Tercera imagen')

    def __init__(self, *args, **kwargs):
        super(EquipoProteccionPersonalForm, self).__init__(*args, **kwargs)
        self.fields['entidad_importadora'].queryset = Entidad.objects.filter(entidad_importadora=True, activo=True).order_by('nombre')
        self.fields['numero_prefactura'].queryset = NumeroPrefactura.objects.filter(activo=True).order_by('numero_prefactura')

    def clean(self):
        data = super().clean()
        numero_prefactura = data.get('numero_prefactura')
        factura = Factura.objects.filter(numero_prefactura_id=numero_prefactura)
        if factura.exists():
            self.add_error('numero_prefactura', ('ingrese otro número, ya existen equipos facturados con este número de prefactura').capitalize())
        if data['segunda_img'] and data['tercera_img'] and not data['primera_img']:
            self.add_error('primera_img', ('Debe insertar "Primera imagen" para luego insertar "Segunda imagen"'))
        elif data['tercera_img'] and not data['segunda_img'] and not data['primera_img']:
            self.add_error('segunda_img', ('Debe insertar "Segunda imagen" para luego insertar "Tercera imagen"'))
        elif data['segunda_img'] and not data['primera_img']:
            self.add_error('primera_img', ('Debe insertar "Primera imagen" para luego insertar "Segunda imagen"'))
        elif data['primera_img'] and data['tercera_img'] and not data['segunda_img']:
            self.add_error('segunda_img', ('Debe insertar "Segunda imagen" para luego insertar "Tercera imagen"'))