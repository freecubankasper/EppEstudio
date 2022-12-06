# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from nomencladores.models import Provincia, Municipio, Entidad
from nomencladores.models.organismo import Organismo
from nomencladores.models.pais import Pais


class User(AbstractUser):

    date_joined = None

    first_name = models.CharField(max_length=100, blank=False, null=False)

    last_name = models.CharField(max_length=200, blank=False, null=False)

    email = models.EmailField(blank=False, null=False, unique=True)

    is_staff = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)

    nombre = models.CharField(max_length=100, blank=False, null=False)

    apellidos = models.CharField(max_length=255, blank=False, null=False)

    telefono = models.CharField(max_length=250, blank=True, null=True)

    img_usuario = models.ImageField(upload_to='img_usuarios/', blank=True, null=True)

    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, blank=True, null=True)

    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, blank=True, null=True)

    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, blank=True, null=True)

    entidad = models.CharField(max_length=250, blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    fecha_actualizacion_password = models.DateTimeField(blank=True, null=True)

    fecha_deshabilitacion = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.first_name

    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)
    def proyectosbool(self):
        from proyecto.models import Proyecto
        return Proyecto.objects.filter(usuario_id=self.id).count()

    class Meta:
        app_label = 'usuario'
        db_table = 'auth_user'
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        ordering = ['id']
        permissions = (
            ('enable_usuario', 'Can enable usuario'),
            ('disable_usuario', 'Can disable usuario'),
            ('change_contraseña_usuario_actual', 'Can change contraseña usuario actual'),
            ('change_contraseña', 'Can change contraseña'),
            ('delete_usuarios_seleccionados', 'Can delete usuarios seleccionados'),
            ('enable_group', 'Can enable group'),
            ('disnable_group', 'Can disnable group'),
            ('view_menu_administracion', 'Can view menu administracion'),
            ('view_inicio', 'Can view inicio'),
            ('view_graficos', 'Can view graficos'),
            ('view_grafico_cantidades', 'Can view grafico cantidades'),
            ('view_grafico_gravedad', 'Can view grafico gravedad'),
        )
