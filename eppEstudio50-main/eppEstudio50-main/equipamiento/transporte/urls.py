from django.urls import path

from transporte.views import transporte

urlpatterns = [

    # TRANSPORTES
    path('transportes/', transporte.ListadoTransportesView.as_view(), name='transportes'),
    path('transportes/registrar/', transporte.RegistrarTransporteView.as_view(), name='registrar_transporte'),
    path('transportes/modificar/<int:pk>/', transporte.ModificarTransporteView.as_view(), name='modificar_transporte'),
    path('transportes/eliminar/<int:pk>/', transporte.EliminarTransporteView.as_view(), name='eliminar_transporte'),
    path('transportes/habilitar/<int:pk>/', transporte.HabilitarTransporteView.as_view(), name='habilitar_transporte'),
    path('transportes/deshabilitar/<int:pk>/', transporte.DeshabilitarTransporteView.as_view(), name='deshabilitar_transporte'),
    path('transportes/eliminar_seleccionados/', transporte.EliminarTransportesSeleccionadosView.as_view(), name='eliminar_transportes_seleccionados'),
    path('transportes/detalles/<int:pk>/', transporte.DetallesTransporteView.as_view(), name='detalles_transporte'),

]
