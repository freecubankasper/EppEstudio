from django.urls import path

from abastecimiento.views import abastecimiento

urlpatterns = [

    # EQUIPAMIENTOS
    path('abastecimientos/', abastecimiento.ListadoAbastecimientosView.as_view(), name='abastecimientos'),
    path('abastecimientos/registrar/', abastecimiento.RegistrarAbastecimientoView.as_view(), name='registrar_abastecimiento'),
    path('abastecimientos/modificar/<int:pk>/', abastecimiento.ModificarAbastecimientoView.as_view(), name='modificar_abastecimiento'),
    path('abastecimientos/eliminar/<int:pk>/', abastecimiento.EliminarAbastecimientoView.as_view(), name='eliminar_abastecimiento'),
    path('abastecimientos/habilitar/<int:pk>/', abastecimiento.HabilitarAbastecimientoView.as_view(), name='habilitar_abastecimiento'),
    path('abastecimientos/deshabilitar/<int:pk>/', abastecimiento.DeshabilitarAbastecimientoView.as_view(), name='deshabilitar_abastecimiento'),
    path('abastecimientos/eliminar_seleccionados/', abastecimiento.EliminarAbastecimientosSeleccionadosView.as_view(), name='eliminar_abastecimientos_seleccionados'),
    path('abastecimientos/detalles/<int:pk>/', abastecimiento.DetallesAbastecimientoView.as_view(), name='detalles_abastecimiento'),

]
