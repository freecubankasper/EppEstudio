# -*- coding: utf-8 -*-
import datetime
from django.contrib import messages
from django.contrib.auth.models import Group
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.base import View, TemplateView
from django.contrib.auth import login
from rest_framework.utils import json

from core.utiles.permission_required import PermissionRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    FormView,
    DetailView)

from nomencladores.models import Municipio, Entidad
from usuario.forms.form_usuario import (
    RegistrarUsuarioForm,
    ModificarUsuarioForm,
    ModificarContrasenaUsuarioActualForm
)
from usuario.models import User


class ListadoUsuariosView(PermissionRequiredMixin, ListView):
    model = User
    template_name = 'listado_usuarios.html'
    paginate_by = 20
    permission = 'usuario.view_user'

    def get_queryset(self):
        usuarios = User.objects.all().order_by('username')

        # paginate_by = self.request.GET.get('paginate_by')
        # if paginate_by is not None:
        #     self.paginate_by = paginate_by

        q = self.request.GET.get('q')
        if q is not None and q != "":
            try:
                usuarios = usuarios.filter(Q(username__icontains=q) |
                                           Q(first_name__icontains=q) |
                                           Q(last_name__icontains=q) |
                                           Q(email__icontains=q)
                                           )

            except Exception as e:
                messages.add_message(self.request, messages.ERROR, "Error durante la búsqueda.")
                print("Error buscando en la lista de usuarios: {}.".format(e.args))
                print("Usuario: {}. q: {}.".format(self.request.user, q))
                return usuarios
        return usuarios

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de usuarios'
        context['titulo_tabla'] = 'Usuarios'
        context['activar_administracion'] = True
        context['path'] = [
            {'name': 'Administración'},
            {'name': 'Usuarios', 'href': reverse_lazy('usuarios')}
        ]
        return context


class MunicipioAjaxView(View):

    def get(self, request, *args, **kwargs):
        id_provincia = request.GET['id_provincia']
        municipios = Municipio.objects.filter(provincia_id=id_provincia, activo=True)

        mun = [self.municipio_serializer(municipio) for municipio in municipios]
        return HttpResponse(json.dumps(mun), content_type='aplication/json')

    @classmethod
    def municipio_serializer(cls, municipio):
        return {'id': municipio.id, 'nombre': municipio.nombre}


class EntidadAjaxView(View):

    def get(self, request, *args, **kwargs):
        id_organismo = request.GET['id_organismo']
        id_municipio = request.GET['id_municipio']
        entidades = Entidad.objects.filter(organismo_id=id_organismo, municipio_id=id_municipio, activo=True)

        ent = [self.entidad_serializer(entidad) for entidad in entidades]
        return HttpResponse(json.dumps(ent), content_type='aplication/json')

    @classmethod
    def entidad_serializer(cls, entidad):
        return {'id': entidad.id, 'nombre': entidad.nombre}


class RegistrarUsuarioView(PermissionRequiredMixin, CreateView):
    model = User
    form_class = RegistrarUsuarioForm
    template_name = "usuario.html"
    success_url = reverse_lazy('usuarios')
    permission = 'usuario.add_user'

    def get_context_data(self, **kwargs):
        context = super(RegistrarUsuarioView, self).get_context_data(**kwargs)
        context['titulo'] = 'Registrar usuario'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'usuario'
        context['icono_form'] = 'plus'
        context['activar_administracion'] = True
        context['form_registrar'] = True
        context['form'] = self.form_class
        context['path'] = [
            {'name': 'Administración'},
            {'name': 'Usuario', 'href': reverse_lazy('usuarios')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_usuario')}
        ]
        return context

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST, request.FILES)

        ids_groups = request.POST.getlist('groups')
        if ids_groups.__len__() == 0:
            form.add_error('groups', 'Este campo es obligatorio.')
        if ids_groups and ids_groups.__len__() > 1:
            form.add_error('groups', 'No puede seleccionar más de un rol')

        if form.is_valid():
            user = form.save()
            for id_grupo in ids_groups:
                user.groups.add(Group.objects.get(id=id_grupo))
            messages.add_message(request, messages.SUCCESS, "Usuario registrado con éxito.")
            return HttpResponseRedirect(self.success_url)

        context = {
            'titulo': 'Registrar usuario',
            'titulo_tabla': "Registrar",
            'subtitulo_tabla': "usuario",
            'icono_form': 'plus',
            'activar_administracion': True,
            'form_registrar': True,
            'form': form,
            'path': [
                {'name': 'Administración'},
                {'name': 'Usuario', 'href': reverse_lazy('usuarios')},
                {'name': 'Registrar', 'href': reverse_lazy('registrar_usuario')}
            ]
        }
        return render(request, self.template_name, context)


class ModificarUsuarioView(PermissionRequiredMixin, UpdateView):
    model = User
    template_name = "usuario.html"
    form_class = ModificarUsuarioForm
    success_url = reverse_lazy('usuarios')
    permission = 'usuario.change_user'

    def get_context_data(self, **kwargs):
        context = super(ModificarUsuarioView, self).get_context_data(**kwargs)
        usuario = self.model.objects.get(id=self.kwargs['pk'])
        context['form'] = self.form_class(instance=usuario)
        context['titulo'] = 'Modificar usuario'
        context['titulo_tabla'] = 'Modificar'
        context['subtitulo_tabla'] = 'usuario'
        context['icono_form'] = 'edit'
        context['activar_administracion'] = True
        context['form_modificar'] = True
        context['path'] = [
            {'name': 'Administración'},
            {'name': 'Usuario', 'href': reverse_lazy('usuarios')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_usuario', kwargs={'pk': self.kwargs['pk']})}
        ]
        return context

    def post(self, request, *args, **kwargs):

        pk = self.kwargs['pk']
        usuario = self.model.objects.get(id=pk)
        form = self.form_class(request.POST, request.FILES, instance=usuario)
        ids_groups = request.POST.getlist('groups')
        if ids_groups.__len__() == 0:
            form.add_error('groups', 'Este campo es obligatorio.')
        if ids_groups and ids_groups.__len__() > 1:
            form.add_error('groups', 'No puede seleccionar más de un rol')

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Usuario modificado con éxito.")
            return HttpResponseRedirect(self.success_url)

        context = {
            'titulo': 'Modificar usuario',
            'titulo_tabla': "Modificar",
            'subtitulo_tabla': "usuario",
            'icono_form': 'edit',
            'activar_administracion': True,
            'form_modificar': True,
            'form': form,
            'path': [
                {'name': 'Administración'},
                {'name': 'Usuario', 'href': reverse_lazy('usuarios')},
                {'name': 'Modificar', 'href': reverse_lazy('modificar_usuario', kwargs={'pk': pk})}
            ]
        }
        return render(request, self.template_name, context)


class ModificarContrasenaUsuarioActualView(PermissionRequiredMixin, FormView):
    model = User
    template_name = "usuario.html"
    success_url = reverse_lazy('usuarios')
    form_class = ModificarContrasenaUsuarioActualForm
    permission = 'usuario.change_contraseña_usuario_actual'

    def get_context_data(self, **kwargs):
        get_object_or_404(User, id=self.kwargs['pk'])  # Validar que el usuario exista
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Modificar contraseña'
        context['titulo_tabla'] = 'Modificar contraseña'
        context['icono_form'] = 'edit'
        context['activar_administracion'] = True
        context['modificar_contrasena'] = True
        context['path'] = [
            {'name': 'Administración'},
            {'name': 'Usuarios', 'href': reverse_lazy('usuarios')},
            {'name': 'Modificar Contraseña', 'href': reverse_lazy('modificar_contrasena_usuario_actual', kwargs={'pk': self.kwargs['pk']})}
        ]
        return context

    def form_valid(self, form):
        user = self.request.user
        user.set_password(form.cleaned_data.get('password1'))
        user.fecha_actualizacion_password = datetime.datetime.now()
        user.save()

        login(self.request, user)

        messages.add_message(self.request, messages.SUCCESS, "Contraseña modificada con éxito.")
        return super().form_valid(form)


class ModificarContrasenaView(PermissionRequiredMixin, FormView):
    model = User
    template_name = "usuario.html"
    success_url = reverse_lazy('usuarios')
    form_class = ModificarContrasenaUsuarioActualForm
    permission = 'usuario.change_contraseña'

    def get_context_data(self, **kwargs):
        get_object_or_404(User, id=self.kwargs['pk'])  # Validar que el usuario exista
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modificar contraseña'
        context['titulo_tabla'] = 'Modificar contraseña'
        context['icono_form'] = 'edit'
        context['activar_administracion'] = True
        context['modificar_contrasena'] = True
        context['path'] = [
            {'name': 'Administración'},
            {'name': 'Usuarios', 'href': reverse_lazy('usuarios')},
            {'name': 'Modificar Contraseña', 'href': reverse_lazy('modificar_contrasena_usuario_actual', kwargs={'pk': self.kwargs['pk']})}
        ]
        return context

    def form_valid(self, form):
        user = get_object_or_404(User, id=self.kwargs['pk'])
        user.set_password(form.cleaned_data.get('password1'))
        user.fecha_actualizacion_password = datetime.datetime.now()
        user.save()

        # login(self.request, user)

        messages.add_message(self.request, messages.SUCCESS, "Contraseña modificada con éxito.")
        return super().form_valid(form)


class EliminarUsuarioView(PermissionRequiredMixin, View):
    permission = 'usuario.delete_user'

    def get(self, request, *args, **kwargs):
        usuario = User.objects.get(id=self.kwargs['pk'])
        usuario.delete()
        messages.add_message(request, messages.SUCCESS, "Usuario eliminado con éxito.")
        return JsonResponse({})


class HabilitarUsuarioView(PermissionRequiredMixin, View):
    permission = 'usuario.enable_usuario'

    def get(self, request, *args, **kwargs):
        usuario = User.objects.get(id=self.kwargs['pk'])
        usuario.is_active = True
        usuario.save()
        messages.add_message(request, messages.SUCCESS, "Usuario habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarUsuarioView(PermissionRequiredMixin, View):
    permission = 'usuario.disable_usuario'

    def get(self, request, *args, **kwargs):
        usuario = User.objects.get(id=self.kwargs['pk'])
        usuario.is_active = False
        usuario.fecha_deshabilitacion = datetime.datetime.now()
        usuario.save()
        messages.add_message(request, messages.SUCCESS, "Usuario deshabilitado con éxito.")
        return JsonResponse({})


class EliminarUsuariosSeleccionadosView(PermissionRequiredMixin, TemplateView):
    permission = 'usuario.delete_usuarios_seleccionados'

    def get(self, request, *args, **kwargs):

        try:
            ids = request.GET.get('ids').split(',')
            User.objects.filter(id__in=ids).delete()

            mensaje = "Usuarios eliminados con éxito." if ids.__len__() > 1 else "Usuario eliminado con éxito."
            messages.add_message(request, messages.SUCCESS, mensaje)

        except:
            messages.add_message(request, messages.ERROR, "Ocurrió un error durante la operación.")

        return JsonResponse({})


class DetallesUsuarioView(PermissionRequiredMixin, DetailView):
    template_name = 'detalles_usuario.html'
    model = User
    permission = 'usuario.view_user'

    def get_context_data(self, **kwargs):

        context = super(DetallesUsuarioView, self).get_context_data(**kwargs)
        context['titulo'] = 'Detalles de usuario'
        context['activar_administracion'] = True
        context['path'] = [
            {'name': 'Usuarios', 'href': reverse_lazy('usuarios')}
        ]
        return context
