from django.urls import path

from proyecto.views import Gestionar_proyectoView, Crear_proyectoView, ListadoProyectosView, DeshabilitarProyectoView, \
    HabilitarProyectoView, EliminarProyectoView, EliminarProyectosSeleccionadosView, DetallesProyectoView, \
    ActualizarEstadoProyectoView, ModificarProyectoView

urlpatterns = [

    #PROYECTOS
    path('proyectos/', Gestionar_proyectoView.as_view(), name='proyectos'),
    path('proyectos/registrar-proyecto/', Crear_proyectoView.as_view(), name='registrar_proyecto'),
    path('proyectos/listado-proyecto/', ListadoProyectosView.as_view(), name='listado_proyect'),
    path('proyectos/listado-proyecto/modificar/<int:pk>/', ModificarProyectoView.as_view(), name='modificar_proyecto'),
    path('proyectos/listado-proyecto/eliminar/<int:pk>/', EliminarProyectoView.as_view(), name='eliminar_proyecto'),
    path('proyectos/listado-proyecto/habilitar/<int:pk>/', HabilitarProyectoView.as_view(), name='habilitar_proyecto'),
    path('proyectos/listado-proyecto/deshabilitar/<int:pk>/', DeshabilitarProyectoView.as_view(), name='deshabilitar_proyecto'),
    path('proyectos/listado-proyecto/eliminar_seleccionados/', EliminarProyectosSeleccionadosView.as_view(), name='eliminar_proyectos_seleccionados'),
    path('proyectos/listado-proyecto/detalles/<int:pk>/', DetallesProyectoView.as_view(), name='detalles_proyecto'),
    path('proyectos/listado-proyecto/actualizar_estado_proyecto/<int:pk>/', ActualizarEstadoProyectoView.as_view(), name='actualizar_estado_proyecto'),

]

