from django.urls import path

from actor.views import actor

urlpatterns = [

    # ACTORES
    path('actores/', actor.ListadoActoresView.as_view(), name='actores'),
    path('actores/registrar/', actor.RegistrarActorView.as_view(), name='registrar_actor'),
    path('actores/modificar/<int:pk>/', actor.ModificarActorView.as_view(), name='modificar_actor'),
    path('actores/eliminar/<int:pk>/', actor.EliminarActorView.as_view(), name='eliminar_actor'),
    path('actores/habilitar/<int:pk>/', actor.HabilitarActorView.as_view(), name='habilitar_actor'),
    path('actores/deshabilitar/<int:pk>/', actor.DeshabilitarActorView.as_view(), name='deshabilitar_actor'),
    path('actores/eliminar_seleccionados/', actor.EliminarActoresSeleccionadosView.as_view(), name='eliminar_actores_seleccionados'),
    path('actores/detalles/<int:pk>/', actor.DetallesActorView.as_view(), name='detalles_actor'),

]
