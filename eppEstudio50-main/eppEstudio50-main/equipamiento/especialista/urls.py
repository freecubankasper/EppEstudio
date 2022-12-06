from django.urls import path

from especialista.views import especialista

urlpatterns = [

    # ESPECIALISTAS
    path('especialistas/', especialista.ListadoEspecialistasView.as_view(), name='especialistas'),
    path('especialistas/registrar/', especialista.RegistrarEspecialistaView.as_view(), name='registrar_especialista'),
    path('especialistas/modificar/<int:pk>/', especialista.ModificarEspecialistaView.as_view(), name='modificar_especialista'),
    path('especialistas/eliminar/<int:pk>/', especialista.EliminarEspecialistaView.as_view(), name='eliminar_especialista'),
    path('especialistas/habilitar/<int:pk>/', especialista.HabilitarEspecialistaView.as_view(), name='habilitar_especialista'),
    path('especialistas/deshabilitar/<int:pk>/', especialista.DeshabilitarEspecialistaView.as_view(), name='deshabilitar_especialista'),
    path('especialistas/eliminar_seleccionados/', especialista.EliminarEspecialistasSeleccionadosView.as_view(), name='eliminar_especialistas_seleccionados'),
    path('especialistas/detalles/<int:pk>/', especialista.DetallesEspecialistaView.as_view(), name='detalles_especialista'),

]
