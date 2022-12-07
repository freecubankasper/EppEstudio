from django.urls import path

from locacion.views import locacion

urlpatterns = [

    # LOCACIONES
    path('locaciones/', locacion.ListadoLocacionesView.as_view(), name='locaciones'),
    path('locaciones/registrar/', locacion.RegistrarLocacionView.as_view(), name='registrar_locacion'),
    path('locaciones/modificar/<int:pk>/', locacion.ModificarLocacionView.as_view(), name='modificar_locacion'),
    path('locaciones/eliminar/<int:pk>/', locacion.EliminarLocacionView.as_view(), name='eliminar_locacion'),
    path('locaciones/habilitar/<int:pk>/', locacion.HabilitarLocacionView.as_view(), name='habilitar_locacion'),
    path('locaciones/deshabilitar/<int:pk>/', locacion.DeshabilitarLocacionView.as_view(), name='deshabilitar_locacion'),
    path('locaciones/eliminar_seleccionados/', locacion.EliminarLocacionesSeleccionadosView.as_view(), name='eliminar_locaciones_seleccionadas'),
    path('locaciones/detalles/<int:pk>/', locacion.DetallesLocacionView.as_view(), name='detalles_locacion'),

]
