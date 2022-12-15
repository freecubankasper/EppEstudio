# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import Group

from nomencladores.models import Municipio, Provincia, Entidad
from nomencladores.models.organismo import Organismo
from usuario.models import User
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm


class RegistrarUsuarioForm(UserCreationForm):

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'groups',
            'telefono',
            'img_usuario',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'groups': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'min': 0}),
        }

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'username': 'Usuario',
            'email': 'Correo',
            'password1': 'Contraseña',
            'password2': 'Contraseña (Confirmación)',
            'telefono': 'Teléfono',
            'groups': 'Rol',
            'img_usuario': 'Imagen',
        }

    img_usuario = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super(RegistrarUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['groups'].queryset = Group.objects.all()
        self.fields['municipio'].queryset = Municipio.objects.filter(activo=True).order_by('nombre')
        self.fields['provincia'].queryset = Provincia.objects.filter(activo=True).order_by('nombre')
        self.fields['entidad'].queryset = Entidad.objects.filter(activo=True).order_by('nombre')


class ModificarUsuarioForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'telefono',
            'groups',
            'img_usuario',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control tooltips'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control tooltips'}),
            'username': forms.TextInput(attrs={'class': 'form-control tooltips'}),
            'email': forms.EmailInput(attrs={'class': 'form-control tooltips'}),
            'groups': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'min': 0}),
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'username': 'Usuario',
            'email': 'Correo',
            'telefono': 'Teléfono',
            'groups': 'Rol',
        }

    img_usuario = forms.ImageField(required=False, label='Imagen')

    def __init__(self, *args, **kwargs):
        super(ModificarUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['groups'].queryset = Group.objects.all()
        self.fields['municipio'].queryset = Municipio.objects.filter(activo=True).order_by('nombre')
        self.fields['provincia'].queryset = Provincia.objects.filter(activo=True).order_by('nombre')


class ModificarContrasenaUsuarioActualForm(forms.Form):

    password1 = forms.CharField(
        required=True,
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput(),
    )

    password2 = forms.CharField(
        required=True,
        label="Contraseña (Confirmación)",
        strip=False,
        widget=forms.PasswordInput()
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.user = None
        super(ModificarContrasenaUsuarioActualForm, self).__init__(*args, **kwargs)

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Los dos campos de contraseña no coinciden.")
        return self.cleaned_data

    def clean_password2(self):
        password2 = self.cleaned_data.get("password2")
        password_validation.validate_password(password2)
        return password2
