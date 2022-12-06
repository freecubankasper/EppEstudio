from django.urls import path

from equipamiento.views import equipamiento

urlpatterns = [

    # EQUIPAMIENTOS
    path('equipamientos/', equipamiento.ListadoEquipamientosView.as_view(), name='equipamientos'),
    path('equipamientos/registrar/', equipamiento.RegistrarEquipamientoView.as_view(), name='registrar_equipamiento'),
    path('equipamientos/modificar/<int:pk>/', equipamiento.ModificarEquipamientoView.as_view(), name='modificar_equipamiento'),
    path('equipamientos/eliminar/<int:pk>/', equipamiento.EliminarEquipamientoView.as_view(), name='eliminar_equipamiento'),
    path('equipamientos/habilitar/<int:pk>/', equipamiento.HabilitarEquipamientoView.as_view(), name='habilitar_equipamiento'),
    path('equipamientos/deshabilitar/<int:pk>/', equipamiento.DeshabilitarEquipamientoView.as_view(), name='deshabilitar_equipamiento'),
    path('equipamientos/eliminar_seleccionados/', equipamiento.EliminarEquipamientosSeleccionadosView.as_view(), name='eliminar_equipamientos_seleccionados'),
    path('equipamientos/detalles/<int:pk>/', equipamiento.DetallesEquipamientoView.as_view(), name='detalles_equipamiento'),

]
