from django.urls import path

from equipo_proteccion_personal.views import equipo_proteccion_personal, factura, numero_prefactura, documento

urlpatterns = [

    #EQUIPOSDEPROTECCIONPERSONAL
    path('equipos-proteccion-personal/', equipo_proteccion_personal.ListadoEquipoProteccionPersonalView.as_view(), name='equipos_proteccion_personal'),
    path('equipos-proteccion-personal/registrar/', equipo_proteccion_personal.RegistrarEquipoProteccionPersonalView.as_view(), name='registrar_equipo_proteccion_personal'),
    path('equipos-proteccion-personal/modificar/<int:pk>/', equipo_proteccion_personal.ModificarEquipoProteccionPersonalView.as_view(), name='modificar_equipo_proteccion_personal'),
    path('equipos-proteccion-personal/eliminar/<int:pk>/', equipo_proteccion_personal.EliminarEquipoProteccionPersonalView.as_view(), name='eliminar_equipo_proteccion_personal'),
    path('equipos-proteccion-personal/eliminar_seleccionados/', equipo_proteccion_personal.EliminarEquiposProteccionPersonalSeleccionadosView.as_view(), name='eliminar_equipos_proteccion_personal_seleccionados'),
    path('equipos-proteccion-personal/habilitar/<int:pk>/', equipo_proteccion_personal.HabilitarEquipoProteccionPersonalView.as_view(), name='habilitar_equipo_proteccion_personal'),
    path('equipos-proteccion-personal/deshabilitar/<int:pk>/', equipo_proteccion_personal.DeshabilitarEquipoProteccionPersonalView.as_view(), name='deshabilitar_equipo_proteccion_personal'),
    path('equipos-proteccion-personal/detalles/<int:pk>/', equipo_proteccion_personal.DetallesEquipoPoteccionPersonalView.as_view(), name='detalles_equipo_proteccion_personal'),
    path('equipos-proteccion-personal/renovar/<int:pk>/', equipo_proteccion_personal.RenovarEquipoProteccionPersonalView.as_view(), name='renovar_equipo_proteccion_personal'),
    path('equipos-proteccion-personal/factura/', equipo_proteccion_personal.FacturaPDFView.as_view(), name='exportar_factura'),
    path('equipos-proteccion-personal/prefactura/', equipo_proteccion_personal.PreFacturaPDFView.as_view(), name='exportar_prefactura'),
    path('equipos-proteccion-personal/certificado_epp/<int:pk>/', equipo_proteccion_personal.CertificadoEppPDFView.as_view(), name='exportar_certificado_epp'),

    # FACTURAS
    path('facturas/', factura.ListadoFacturasView.as_view(), name='facturas'),
    path('facturas/eliminar/<int:pk>/', factura.EliminarFacturaView.as_view(), name='eliminar_factura'),
    path('facturas/habilitar/<int:pk>/', factura.HabilitarFacturaView.as_view(), name='habilitar_factura'),
    path('facturas/deshabilitar/<int:pk>/', factura.DeshabilitarFacturaView.as_view(), name='deshabilitar_factura'),
    path('facturas/detalles/<int:pk>/', factura.DetallesFacturaView.as_view(), name='detalles_factura'),
    path('facturas/pagar-factura/', factura.PagarFactura.as_view(), name='pagar_factura'),

    # NUMEROSPREFACTURA
    path('numeros-prefactura/', numero_prefactura.ListadoNumerosPrefacturaView.as_view(), name='numeros_prefactura'),
    path('numeros-prefactura/registrar/', numero_prefactura.RegistrarNumeroPrefacturaView.as_view(), name='registrar_numero_prefactura'),
    path('numeros-prefactura/modificar/<int:pk>/', numero_prefactura.ModificarNumeroPrefacturaView.as_view(), name='modificar_numero_prefactura'),
    path('numeros-prefactura/eliminar/<int:pk>/', numero_prefactura.EliminarNumeroPrefacturaView.as_view(), name='eliminar_numero_prefactura'),
    path('numeros-prefactura/habilitar/<int:pk>/', numero_prefactura.HabilitarNumeroPrefacturaView.as_view(), name='habilitar_numero_prefactura'),
    path('numeros-prefactura/deshabilitar/<int:pk>/', numero_prefactura.DeshabilitarNumeroPrefacturaView.as_view(), name='deshabilitar_numero_prefactura'),

    # DOCUMENTOS
    path('documentos/', documento.ListadoDocumentosView.as_view(), name='documentos'),
    path('documentos/registrar/', documento.RegistrarDocumentoView.as_view(), name='registrar_documento'),
    path('documentos/modificar/<int:pk>/', documento.ModificarDocumentoView.as_view(), name='modificar_documento'),
    path('documentos/eliminar/<int:pk>/', documento.EliminarDocumentoView.as_view(), name='eliminar_documento'),
    path('documentos/habilitar/<int:pk>/', documento.HabilitarDocumentoView.as_view(), name='habilitar_documento'),
    path('documentos/deshabilitar/<int:pk>/', documento.DeshabilitarDocumentoView.as_view(), name='deshabilitar_documento'),
    path('documentos/descargar/<int:pk>/', documento.DescargarDocumentoView.as_view(), name='descargar_documento'),
]
