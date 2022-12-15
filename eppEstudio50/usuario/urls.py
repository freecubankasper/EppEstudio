# -*- coding: utf-8 -*-
from django.urls import path
from usuario.views import groups, usuarios

urlpatterns = [

    # USUARIOS

    path('usuarios/', usuarios.ListadoUsuariosView.as_view(), name='usuarios'),
    path('usuarios/registrar/', usuarios.RegistrarUsuarioView.as_view(), name='registrar_usuario'),
    path('usuarios/registrar_front/', usuarios.CrearUsuarioFrontView.as_view(), name='registrar_usuario_front'),
    path('usuarios/modificar/<int:pk>/', usuarios.ModificarUsuarioView.as_view(), name='modificar_usuario'),
    path('usuarios/modificar_contrasena/<int:pk>/', usuarios.ModificarContrasenaView.as_view(), name='modificar_contrasena'),
    path('usuarios/modificar_contrasena_usuario_actual/<int:pk>/', usuarios.ModificarContrasenaUsuarioActualView.as_view(), name='modificar_contrasena_usuario_actual'),
    path('usuarios/habilitar/<int:pk>/', usuarios.HabilitarUsuarioView.as_view(), name='habilitar_usuario'),
    path('usuarios/deshabilitar/<int:pk>/', usuarios.DeshabilitarUsuarioView.as_view(), name='deshabilitar'),
    path('usuarios/eliminar/<int:pk>/', usuarios.EliminarUsuarioView.as_view(), name='eliminar_usuario'),
    path('usuarios/eliminar_usuarios_seleccionados/', usuarios.EliminarUsuariosSeleccionadosView.as_view(), name='eliminar_usuarios_seleccionados'),
    path('usuarios/detalles/<int:pk>/', usuarios.DetallesUsuarioView.as_view(), name='detalles_usuario'),
    path('usuarios/provincia_municipio/', usuarios.MunicipioAjaxView.as_view(), name='usuario_provincia_municipio'),
    path('usuarios/municipio_entidad/', usuarios.EntidadAjaxView.as_view(), name='usuario_municipio_entidad'),

    # GRUPOS
    path('grupos/', groups.ListadoGroupsView.as_view(), name='grupos'),
    path('grupos/registrar/', groups.RegistrarGroupsView.as_view(), name='registrar_grupo'),
    path('grupos/modificar/<int:pk>/', groups.ModificarGroupsView.as_view(), name='modificar_grupo'),
    # path('grupos/habilitar/<int:pk>/', groups.HabilitarGroupsView.as_view(), name='habilitar_grupo'),
    # path('grupos/deshabilitar/<int:pk>/', groups.DeshabilitarGroupsView.as_view(), name='deshabilitar_grupo'),
]
