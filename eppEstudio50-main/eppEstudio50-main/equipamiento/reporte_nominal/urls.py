from django.urls import path

from reporte_nominal.views import reporte_equipo_proteccion_personal_registrado, reporte_entidad, reportes, \
    reporte_equipo_proteccion_personal_aprobado, reporte_equipo_proteccion_personal_vencido, reporte_factura

urlpatterns = [
    #REPORTES NOMINAL
    path('reportes/', reportes.ReportesView.as_view(), name='reportes'),
    path('reportes-entidad/', reporte_entidad.ReportesEntidadView.as_view(), name='reportes_entidad'),
    path('reportes-equipo-proteccion-personal-registrado/', reporte_equipo_proteccion_personal_registrado.ReportesEquipoProteccionPersonalRegistradoView.as_view(), name='reportes_equipo_proteccion_personal_registrado'),
    path('reportes-equipo-proteccion-personal-aprobado/', reporte_equipo_proteccion_personal_aprobado.ReportesEquipoProteccionPersonalAprobadoView.as_view(), name='reportes_equipo_proteccion_personal_aprobado'),
    path('reportes-equipo-proteccion-personal-vencido/', reporte_equipo_proteccion_personal_vencido.ReportesEquipoProteccionPersonalVencidoView.as_view(), name='reportes_equipo_proteccion_personal_vencido'),
    path('reportes-factura/', reporte_factura.ReportesFacturaView.as_view(), name='reportes_factura'),
]
