from django.urls import path

from core.views.calendario import LlamadoView
from llamado.views import llamado_proyecto

urlpatterns = [

    # LLAMADOSPROYECTOS
    path('proyectos/listado-proyecto/<int:proyecto_id>/registrar/', llamado_proyecto.RegistrarLlamadoProyectoView.as_view(), name='registrar_llamado_proyecto'),
    path('llamado/<int:proyecto_id>/registrar/', LlamadoView.as_view(), name='registrar_llamado_proyecto_calendario'),
    path('proyectos/listado-proyecto/<int:proyecto_id>/llamados/', llamado_proyecto.ListadoLlamadosProyectoView.as_view(), name='llamados_proyecto'),
    path('proyectos/listado-proyecto/<int:proyecto_id>/llamados/modificar/<int:pk>/', llamado_proyecto.ModificarLlamadoProyectoView.as_view(), name='modificar_llamado_proyecto'),
    path('proyectos/listado-proyecto/<int:proyecto_id>/llamados/eliminar/<int:pk>/', llamado_proyecto.EliminarLlamadoProyectoView.as_view(), name='eliminar_llamado_proyecto'),
    path('proyectos/listado-proyecto/<int:proyecto_id>/llamados/eliminar_seleccionados/', llamado_proyecto.EliminarLlamadosProyectoSeleccionadosView.as_view(), name='eliminar_llamados_proyecto_seleccionados'),
    path('proyectos/listado-proyecto/<int:proyecto_id>/llamados/habilitar/<int:pk>/', llamado_proyecto.HabilitarLlamadoProyectoView.as_view(), name='habilitar_llamado_proyecto'),
    path('proyectos/listado-proyecto/<int:proyecto_id>/llamados/deshabilitar/<int:pk>/', llamado_proyecto.DeshabilitarLlamadoProyectoView.as_view(), name='deshabilitar_llamado_proyecto'),
    path('proyectos/listado-proyecto/<int:proyecto_id>/llamados/detalles/<int:pk>/', llamado_proyecto.DetallesLlamadoProyectoView.as_view(), name='detalles_llamado_proyecto'),

]
