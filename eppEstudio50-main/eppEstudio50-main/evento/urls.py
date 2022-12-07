from django.urls import path

from evento.views import evento_proyecto, evento_equipamiento, evento_actor, evento_locacion, evento_transporte, \
    evento_abastecimiento, evento_especialista

urlpatterns = [

    # EVENTOSPROYECTOS
    path('proyectos/listado-proyecto/<int:proyecto_id>/llamados/<int:llamado_id>/registrar/', evento_proyecto.RegistrarEventoProyectoView.as_view(), name='registrar_evento_proyecto'),
    path('calendario/<int:proyecto_id>/eventos/<int:llamado_id>/registrar/',evento_proyecto.RegistrarEventoProyectoCalendarioView.as_view(), name='registrar_evento_proyecto_calendario'),
    path('calendario/<int:proyecto_id>/eventos/<int:llamado_id>/registrarequipamiento/',evento_proyecto.RegistrarEventoEquipamientoCalendarioView.as_view(), name='registrar_evento_equipamiento_calendario'),
    path('calendario/<int:proyecto_id>/eventos/<int:llamado_id>/registrareventollamado/',evento_proyecto.RegistrarEventoLlamadoCalendarioView.as_view(), name='registrar_evento_llamado_calendario'),
    path('calendario/<int:proyecto_id>/eventos/<int:llamado_id>/registrartransporte/',evento_proyecto.RegistrarEventoTransporteCalendarioView.as_view(), name='registrar_evento_transporte_calendario'),
    path('calendario/<int:proyecto_id>/eventos/<int:llamado_id>/registrartalent/',evento_proyecto.RegistrarEventoTalentCalendarioView.as_view(), name='registrar_evento_talent_calendario'),
    path('proyectos/listado-proyecto/<int:proyecto_id>/llamados/<int:llamado_id>/eventos/', evento_proyecto.ListadoEventosProyectoView.as_view(), name='eventos_proyecto'),
    path('proyectos/listado-proyecto/<int:proyecto_id>/llamados/<int:llamado_id>/eventos/modificar/<int:pk>/', evento_proyecto.ModificarEventoProyectoView.as_view(), name='modificar_evento_proyecto'),
    path('proyectos/listado-proyecto/<int:proyecto_id>/llamados/<int:llamado_id>/eventos/eliminar/<int:pk>/', evento_proyecto.EliminarEventoProyectoView.as_view(), name='eliminar_evento_proyecto'),
    path('proyectos/listado-proyecto/<int:proyecto_id>/llamados/<int:llamado_id>/eventos/habilitar/<int:pk>/', evento_proyecto.HabilitarEventoProyectoView.as_view(), name='habilitar_evento_proyecto'),
    path('proyectos/listado-proyecto/<int:proyecto_id>/llamados/<int:llamado_id>/eventos/deshabilitar/<int:pk>/', evento_proyecto.DeshabilitarEventoProyectoView.as_view(), name='deshabilitar_evento_proyecto'),
    path('proyectos/listado-proyecto/<int:proyecto_id>/llamados/<int:llamado_id>/eventos/detalles/<int:pk>/', evento_proyecto.DetallesEventoProyectoView.as_view(), name='detalles_evento_proyecto'),
    path('proyectos/listado-proyecto/<int:proyecto_id>/llamados/<int:llamado_id>/eventos/exportar_eventos/', evento_proyecto.EventosProyectoPDFView.as_view(), name='exportar_eventos_proyecto'),

    # EVENTOSEQUIPAMIENTOS
    path('equipamientos/<int:equipamiento_id>/registrar/', evento_equipamiento.RegistrarEventoEquipamientoView.as_view(), name='registrar_evento_equipamiento'),
    path('registrarevento/<int:llamado_id>', evento_equipamiento.RegistrarEventoEquipamientoLlamadoView.as_view(), name='registrar_evento_equipamiento_llamado'),
    path('registrareventotalet/<int:llamado_id>', evento_actor.RegistrarEventoTalentoLlamadoView.as_view(), name='registrar_evento_talento_llamado'),
    path('equipamientos/<int:equipamiento_id>/eventos/', evento_equipamiento.ListadoEventosEquipamientoView.as_view(), name='eventos_equipamiento'),
    path('equipamientos/<int:equipamiento_id>/eventos/modificar/<int:pk>/', evento_equipamiento.ModificarEventoEquipamientoView.as_view(), name='modificar_evento_equipamiento'),
    path('equipamientos/<int:equipamiento_id>/eventos/eliminar/<int:pk>/', evento_equipamiento.EliminarEventoEquipamientoView.as_view(), name='eliminar_evento_equipamiento'),
    path('equipamientos/<int:equipamiento_id>/eventos/habilitar/<int:pk>/', evento_equipamiento.HabilitarEventoEquipamientoView.as_view(), name='habilitar_evento_equipamiento'),
    path('equipamientos/<int:equipamiento_id>/eventos/deshabilitar/<int:pk>/', evento_equipamiento.DeshabilitarEventoEquipamientoView.as_view(), name='deshabilitar_evento_equipamiento'),
    path('equipamientos/<int:equipamiento_id>/eventos/detalles/<int:pk>/', evento_equipamiento.DetallesEventoEquipamientoView.as_view(), name='detalles_evento_equipamiento'),
    path('equipamientos/<int:equipamiento_id>/eventos/exportar_eventos/', evento_equipamiento.EventosEquipamientoPDFView.as_view(), name='exportar_eventos_equipamiento'),

    # EVENTOSACTORES
    path('actores/<int:actor_id>/registrar/', evento_actor.RegistrarEventoActorView.as_view(), name='registrar_evento_actor'),
    path('actores/<int:actor_id>/eventos/', evento_actor.ListadoEventosActorView.as_view(), name='eventos_actor'),
    path('actores/<int:actor_id>/eventos/modificar/<int:pk>/', evento_actor.ModificarEventoActorView.as_view(), name='modificar_evento_actor'),
    path('actores/<int:actor_id>/eventos/eliminar/<int:pk>/', evento_actor.EliminarEventoActorView.as_view(), name='eliminar_evento_actor'),
    path('actores/<int:actor_id>/eventos/habilitar/<int:pk>/', evento_actor.HabilitarEventoActorView.as_view(), name='habilitar_evento_actor'),
    path('actores/<int:actor_id>/eventos/deshabilitar/<int:pk>/', evento_actor.DeshabilitarEventoActorView.as_view(), name='deshabilitar_evento_actor'),
    path('actores/<int:actor_id>/eventos/detalles/<int:pk>/', evento_actor.DetallesEventoActorView.as_view(), name='detalles_evento_actor'),
    path('actores/<int:actor_id>/eventos/exportar_eventos/', evento_actor.EventosActorPDFView.as_view(), name='exportar_eventos_actor'),

    # EVENTOSLOCACIONES
    path('locaciones/<int:locacion_id>/registrar/', evento_locacion.RegistrarEventoLocacionView.as_view(), name='registrar_evento_locacion'),
    path('locaciones/<int:locacion_id>/eventos/', evento_locacion.ListadoEventosLocacionView.as_view(), name='eventos_locacion'),
    path('locaciones/<int:locacion_id>/eventos/modificar/<int:pk>/', evento_locacion.ModificarEventoLocacionView.as_view(), name='modificar_evento_locacion'),
    path('locaciones/<int:locacion_id>/eventos/eliminar/<int:pk>/', evento_locacion.EliminarEventoLocacionView.as_view(), name='eliminar_evento_locacion'),
    path('locaciones/<int:locacion_id>/eventos/habilitar/<int:pk>/', evento_locacion.HabilitarEventoLocacionView.as_view(), name='habilitar_evento_locacion'),
    path('locaciones/<int:locacion_id>/eventos/deshabilitar/<int:pk>/', evento_locacion.DeshabilitarEventoLocacionView.as_view(), name='deshabilitar_evento_locacion'),
    path('locaciones/<int:locacion_id>/eventos/detalles/<int:pk>/', evento_locacion.DetallesEventoLocacionView.as_view(), name='detalles_evento_locacion'),
    path('locaciones/<int:locacion_id>/eventos/exportar_eventos/', evento_locacion.EventosLocacionPDFView.as_view(), name='exportar_eventos_locacion'),

    # EVENTOSTRANSPORTES
    path('transportes/<int:transporte_id>/registrar/', evento_transporte.RegistrarEventoTransporteView.as_view(), name='registrar_evento_transporte'),
    path('transportes/<int:transporte_id>/eventos/', evento_transporte.ListadoEventosTransporteView.as_view(), name='eventos_transporte'),
    path('transportes/<int:transporte_id>/eventos/modificar/<int:pk>/', evento_transporte.ModificarEventoTransporteView.as_view(), name='modificar_evento_transporte'),
    path('transportes/<int:transporte_id>/eventos/eliminar/<int:pk>/', evento_transporte.EliminarEventoTransporteView.as_view(), name='eliminar_evento_transporte'),
    path('transportes/<int:transporte_id>/eventos/habilitar/<int:pk>/', evento_transporte.HabilitarEventoTransporteView.as_view(), name='habilitar_evento_transporte'),
    path('transportes/<int:transporte_id>/eventos/deshabilitar/<int:pk>/', evento_transporte.DeshabilitarEventoTransporteView.as_view(), name='deshabilitar_evento_transporte'),
    path('transportes/<int:transporte_id>/eventos/detalles/<int:pk>/', evento_transporte.DetallesEventoTransporteView.as_view(), name='detalles_evento_transporte'),
    path('transportes/<int:transporte_id>/eventos/exportar_eventos/', evento_transporte.EventosTransportePDFView.as_view(), name='exportar_eventos_transporte'),

    # EVENTOSABASTECIMIENTOS
    path('abastecimientos/<int:abastecimiento_id>/registrar/', evento_abastecimiento.RegistrarEventoAbastecimientoView.as_view(), name='registrar_evento_abastecimiento'),
    path('abastecimientos/<int:abastecimiento_id>/eventos/', evento_abastecimiento.ListadoEventosAbastecimientoView.as_view(), name='eventos_abastecimiento'),
    path('abastecimientos/<int:abastecimiento_id>/eventos/modificar/<int:pk>/', evento_abastecimiento.ModificarEventoAbastecimientoView.as_view(), name='modificar_evento_abastecimiento'),
    path('abastecimientos/<int:abastecimiento_id>/eventos/eliminar/<int:pk>/', evento_abastecimiento.EliminarEventoAbastecimientoView.as_view(), name='eliminar_evento_abastecimiento'),
    path('abastecimientos/<int:abastecimiento_id>/eventos/habilitar/<int:pk>/', evento_abastecimiento.HabilitarEventoAbastecimientoView.as_view(), name='habilitar_evento_abastecimiento'),
    path('abastecimientos/<int:abastecimiento_id>/eventos/deshabilitar/<int:pk>/', evento_abastecimiento.DeshabilitarEventoAbastecimientoView.as_view(), name='deshabilitar_evento_abastecimiento'),
    path('abastecimientos/<int:abastecimiento_id>/eventos/detalles/<int:pk>/', evento_abastecimiento.DetallesEventoAbastecimientoView.as_view(), name='detalles_evento_abastecimiento'),
    path('abastecimientos/<int:abastecimiento_id>/eventos/exportar_eventos/', evento_abastecimiento.EventosAbastecimientoPDFView.as_view(), name='exportar_eventos_abastecimiento'),

    # EVENTOSESPECIALISTAS
    path('especialistas/<int:especialista_id>/registrar/', evento_especialista.RegistrarEventoEspecialistaView.as_view(), name='registrar_evento_especialista'),
    path('especialistas/<int:especialista_id>/eventos/', evento_especialista.ListadoEventosEspecialistaView.as_view(), name='eventos_especialista'),
    path('especialistas/<int:especialista_id>/eventos/modificar/<int:pk>/', evento_especialista.ModificarEventoEspecialistaView.as_view(), name='modificar_evento_especialista'),
    path('especialistas/<int:especialista_id>/eventos/eliminar/<int:pk>/', evento_especialista.EliminarEventoEspecialistaView.as_view(), name='eliminar_evento_especialista'),
    path('especialistas/<int:especialista_id>/eventos/habilitar/<int:pk>/', evento_especialista.HabilitarEventoEspecialistaView.as_view(), name='habilitar_evento_especialista'),
    path('especialistas/<int:especialista_id>/eventos/deshabilitar/<int:pk>/', evento_especialista.DeshabilitarEventoEspecialistaView.as_view(), name='deshabilitar_evento_especialista'),
    path('especialistas/<int:especialista_id>/eventos/detalles/<int:pk>/', evento_especialista.DetallesEventoEspecialistaView.as_view(), name='detalles_evento_especialista'),
    path('especialistas/<int:especialista_id>/eventos/exportar_eventos/', evento_especialista.EventosEspecialistaPDFView.as_view(), name='exportar_eventos_especialista'),

]
