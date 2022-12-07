# -*- coding: utf-8 -*-
from django.urls import path
from nomencladores.views import entidad, provincia, municipio, tipo_entidad, categoria, marca_comercial_registrada, \
    pais, parte_cuerpo, categoria_servicio, sub_categoria, categoria_lic_conduccion, idioma, tipo_suelo, \
    tipo_arquitectura, tipo_lugar, tipo_vehiculo, modelo_transporte, marca_transporte
from nomencladores.views import organismo


urlpatterns = [

    # ORGANISMOS
    path('organismos/', organismo.ListadoOrganismosView.as_view(), name='organismos'),
    path('organismos/registrar/', organismo.RegistrarOrganismoView.as_view(), name='registrar_organismo'),
    path('organismos/modificar/<int:pk>/', organismo.ModificarOrganismoView.as_view(), name='modificar_organismo'),
    path('organismos/habilitar/<int:pk>/', organismo.HabilitarOrganismoView.as_view(), name='habilitar_organismo'),
    path('organismos/deshabilitar/<int:pk>/', organismo.DeshabilitarOrganismoView.as_view(), name='deshabilitar_organismo'),


    # ENTIDADES
    path('entidades/', entidad.ListadoEntidadesView.as_view(), name='entidades'),
    path('entidades/registrar/', entidad.RegistrarEntidadView.as_view(), name='registrar_entidad'),
    path('entidades/modificar/<int:pk>/', entidad.ModificarEntidadView.as_view(), name='modificar_entidad'),
    path('entidades/habilitar/<int:pk>/', entidad.HabilitarEntidadView.as_view(), name='habilitar_entidad'),
    path('entidades/deshabilitar/<int:pk>/', entidad.DeshabilitarEntidadView.as_view(), name='deshabilitar_entidad'),
    path('entidades/detalles/<int:pk>/', entidad.DetallesEntidadView.as_view(), name='detalles_entidad'),
    path('entidades/certificado_entidad/<int:pk>/', entidad.CertificadoEntidadPDFView.as_view(), name='exportar_certificado_entidad'),

    # IDIOMAS
    path('idiomas/', idioma.ListadoIdiomasView.as_view(), name='idiomas'),
    path('idiomas/registrar/', idioma.RegistrarIdiomaView.as_view(), name='registrar_idioma'),
    path('idiomas/modificar/<int:pk>/', idioma.ModificarIdiomaView.as_view(), name='modificar_idioma'),
    path('idiomas/habilitar/<int:pk>/', idioma.HabilitarIdiomaView.as_view(), name='habilitar_idioma'),
    path('idiomas/deshabilitar/<int:pk>/', idioma.DeshabilitarIdiomaView.as_view(), name='deshabilitar_idioma'),

    # PROVINCIAS
    path('provincias/', provincia.ListadoProvinciasView.as_view(), name='provincias'),
    path('provincias/registrar/', provincia.RegistrarProvinciaView.as_view(), name='registrar_provincia'),
    path('provincias/modificar/<int:pk>/', provincia.ModificarProvinciaView.as_view(), name='modificar_provincia'),
    path('provincias/habilitar/<int:pk>/', provincia.HabilitarProvinciaView.as_view(), name='habilitar_provincia'),
    path('provincias/deshabilitar/<int:pk>/', provincia.DeshabilitarProvinciaView.as_view(), name='deshabilitar_provincia'),



    # MUNICIPIOS
    path('municipios/', municipio.ListadoMunicipiosView.as_view(), name='municipios'),
    path('municipios/registrar/', municipio.RegistrarMunicipioView.as_view(), name='registrar_municipio'),
    path('municipios/modificar/<int:pk>/', municipio.ModificarMunicipioView.as_view(), name='modificar_municipio'),
    path('municipios/habilitar/<int:pk>/', municipio.HabilitarMunicipioView.as_view(), name='habilitar_municipio'),
    path('municipios/deshabilitar/<int:pk>/', municipio.DeshabilitarMunicipioView.as_view(), name='deshabilitar_municipio'),


    # TIPOS DE ENTIDADES
    path('tipos_entidad/', tipo_entidad.ListadoTiposEntidadesView.as_view(), name='tipos_entidad'),
    path('tipos_entidad/registrar/', tipo_entidad.RegistrarTipoEntidadView.as_view(), name='registrar_tipo_entidad'),
    path('tipos_entidad/modificar/<int:pk>/', tipo_entidad.ModificarTipoEntidadView.as_view(), name='modificar_tipo_entidad'),
    path('tipos_entidad/habilitar/<int:pk>/', tipo_entidad.HabilitarTipoEntidadView.as_view(), name='habilitar_tipo_entidad'),
    path('tipos_entidad/deshabilitar/<int:pk>/', tipo_entidad.DeshabilitarTipoEntidadView.as_view(), name='deshabilitar_tipo_entidad'),

    # CATEGORÍAS
    path('categorias/', categoria.ListadoCategoriasView.as_view(), name='categorias'),
    path('categorias/registrar/', categoria.RegistrarCategoriaView.as_view(), name='registrar_categoria'),
    path('categorias/modificar/<int:pk>/', categoria.ModificarCategoriaView.as_view(), name='modificar_categoria'),
    path('categorias/habilitar/<int:pk>/', categoria.HabilitarCategoriaView.as_view(), name='habilitar_categoria'),
    path('categorias/deshabilitar/<int:pk>/', categoria.DeshabilitarCategoriaView.as_view(), name='deshabilitar_categoria'),

    # CATEGORÍASLICENCIACONDUCCIÖN
    path('categorias_lic_conduccion/', categoria_lic_conduccion.ListadoCategoriasLicenciasConduccionView.as_view(), name='categorias_lic_conduccion'),
    path('categorias_lic_conduccion/registrar/', categoria_lic_conduccion.RegistrarCategoriaLicenciaConduccionView.as_view(), name='registrar_categoria_lic_conduccion'),
    path('categorias_lic_conduccion/modificar/<int:pk>/', categoria_lic_conduccion.ModificarCategoriaLicenciaConduccionView.as_view(), name='modificar_categoria_lic_conduccion'),
    path('categorias_lic_conduccion/habilitar/<int:pk>/', categoria_lic_conduccion.HabilitarCategoriaLicenciaConduccionView.as_view(), name='habilitar_categoria_lic_conduccion'),
    path('categorias_lic_conduccion/deshabilitar/<int:pk>/', categoria_lic_conduccion.DeshabilitarCategoriaLicenciaConduccionView.as_view(), name='deshabilitar_categoria_lic_conduccion'),

    # CATEGORÍAS DE SERVICIO
    path('categorias_servicio/', categoria_servicio.ListadoCategoriasServicioView.as_view(), name='categorias_servicio'),
    path('categorias_servicio/registrar/', categoria_servicio.RegistrarCategoriaServicioView.as_view(), name='registrar_categoria_servicio'),
    path('categorias_servicio/modificar/<int:pk>/', categoria_servicio.ModificarCategoriaServicioView.as_view(), name='modificar_categoria_servicio'),
    path('categorias_servicio/habilitar/<int:pk>/', categoria_servicio.HabilitarCategoriaServicioView.as_view(), name='habilitar_categoria_servicio'),
    path('categorias_servicio/deshabilitar/<int:pk>/', categoria_servicio.DeshabilitarCategoriaServicioView.as_view(), name='deshabilitar_categoria_servicio'),

    # SUBCATEGORÍAS
    path('subcategoria/', sub_categoria.ListadoSubsCategoriaView.as_view(), name='subs_categoria'),
    path('subcategoria/registrar/', sub_categoria.RegistrarSubCategoriaView.as_view(), name='registrar_sub_categoria'),
    path('subcategoria/modificar/<int:pk>/', sub_categoria.ModificarSubCategoriaView.as_view(), name='modificar_sub_categoria'),
    path('subcategoria/habilitar/<int:pk>/', sub_categoria.HabilitarSubCategoriaView.as_view(), name='habilitar_sub_categoria'),
    path('subcategoria/deshabilitar/<int:pk>/', sub_categoria.DeshabilitarSubCategoriaView.as_view(), name='deshabilitar_sub_categoria'),

    # TIPOS DE SUELOS
    path('tipos_suelo/', tipo_suelo.ListadoTiposSuelosView.as_view(), name='tipos_suelo'),
    path('tipos_suelo/registrar/', tipo_suelo.RegistrarTipoSueloView.as_view(), name='registrar_tipo_suelo'),
    path('tipos_suelo/modificar/<int:pk>/', tipo_suelo.ModificarTipoSueloView.as_view(), name='modificar_tipo_suelo'),
    path('tipos_suelo/habilitar/<int:pk>/', tipo_suelo.HabilitarTipoSueloView.as_view(), name='habilitar_tipo_suelo'),
    path('tipos_suelo/deshabilitar/<int:pk>/', tipo_suelo.DeshabilitarTipoSueloView.as_view(), name='deshabilitar_tipo_suelo'),

    # TIPOS DE ARQUITECTURAS
    path('tipos_arquitectura/', tipo_arquitectura.ListadoTiposArquitecturasView.as_view(), name='tipos_arquitectura'),
    path('tipos_arquitectura/registrar/', tipo_arquitectura.RegistrarTipoArquitecturaView.as_view(), name='registrar_tipo_arquitectura'),
    path('tipos_arquitectura/modificar/<int:pk>/', tipo_arquitectura.ModificarTipoArquitecturaView.as_view(), name='modificar_tipo_arquitectura'),
    path('tipos_arquitectura/habilitar/<int:pk>/', tipo_arquitectura.HabilitarTipoArquitecturaView.as_view(), name='habilitar_tipo_arquitectura'),
    path('tipos_arquitectura/deshabilitar/<int:pk>/', tipo_arquitectura.DeshabilitarTipoArquitecturaView.as_view(), name='deshabilitar_tipo_arquitectura'),

    # TIPOS DE LUGARES
    path('tipos_lugar/', tipo_lugar.ListadoTiposLugaresView.as_view(), name='tipos_lugar'),
    path('tipos_lugar/registrar/', tipo_lugar.RegistrarTipoLugarView.as_view(), name='registrar_tipo_lugar'),
    path('tipos_lugar/modificar/<int:pk>/', tipo_lugar.ModificarTipoLugarView.as_view(), name='modificar_tipo_lugar'),
    path('tipos_lugar/habilitar/<int:pk>/', tipo_lugar.HabilitarTipoLugarView.as_view(), name='habilitar_tipo_lugar'),
    path('tipos_lugar/deshabilitar/<int:pk>/', tipo_lugar.DeshabilitarTipoLugarView.as_view(), name='deshabilitar_tipo_lugar'),

    # TIPOS DE VEHÍCULOS
    path('tipos_vehículo/', tipo_vehiculo.ListadoTiposVehiculosView.as_view(), name='tipos_vehiculo'),
    path('tipos_vehículo/registrar/', tipo_vehiculo.RegistrarTipoVehiculoView.as_view(), name='registrar_tipo_vehiculo'),
    path('tipos_vehículo/modificar/<int:pk>/', tipo_vehiculo.ModificarTipoVehiculoView.as_view(), name='modificar_tipo_vehiculo'),
    path('tipos_vehículo/habilitar/<int:pk>/', tipo_vehiculo.HabilitarTipoVehiculoView.as_view(), name='habilitar_tipo_vehiculo'),
    path('tipos_vehículo/deshabilitar/<int:pk>/', tipo_vehiculo.DeshabilitarTipoVehiculoView.as_view(), name='deshabilitar_tipo_vehiculo'),

    # MARCAS COMERCIALES REGISTRADAS
    path('marcas_comercial_registrada/', marca_comercial_registrada.ListadoMarcasComercialesRegistradasView.as_view(), name='marcas_comercial_registrada'),
    path('marcas_comercial_registrada/registrar/', marca_comercial_registrada.RegistrarMarcaComercialRegistradaView.as_view(), name='registrar_marca_comercial_registrada'),
    path('marcas_comercial_registrada/modificar/<int:pk>/', marca_comercial_registrada.ModificarMarcaComercialRegistradaView.as_view(), name='modificar_marca_comercial_registrada'),
    path('marcas_comercial_registrada/habilitar/<int:pk>/', marca_comercial_registrada.HabilitarMarcaComercialRegistradaView.as_view(), name='habilitar_marca_comercial_registrada'),
    path('marcas_comercial_registrada/deshabilitar/<int:pk>/', marca_comercial_registrada.DeshabilitarMarcaComercialRegistradaView.as_view(), name='deshabilitar_marca_comercial_registrada'),

    # MARCASTRANSPORTES
    path('marcas_transporte/', marca_transporte.ListadoMarcasTransaporteView.as_view(), name='marcas_transporte'),
    path('marcas_transporte/registrar/', marca_transporte.RegistrarMarcaTransaporteView.as_view(), name='registrar_marca_transporte'),
    path('marcas_transporte/modificar/<int:pk>/', marca_transporte.ModificarMarcaTransaporteView.as_view(), name='modificar_marca_transporte'),
    path('marcas_transporte/habilitar/<int:pk>/', marca_transporte.HabilitarMarcaTransaporteView.as_view(), name='habilitar_marca_transporte'),
    path('marcas_transporte/deshabilitar/<int:pk>/', marca_transporte.DeshabilitarMarcaTransaporteView.as_view(), name='deshabilitar_marca_transporte'),

    # MODELOSTRANSPORTES
    path('modelos_transporte/', modelo_transporte.ListadoModelosView.as_view(), name='modelos'),
    path('modelos_transporte/registrar/', modelo_transporte.RegistrarModeloView.as_view(), name='registrar_modelo'),
    path('modelos_transporte/modificar/<int:pk>/', modelo_transporte.ModificarModeloView.as_view(), name='modificar_modelo'),
    path('modelos_transporte/habilitar/<int:pk>/', modelo_transporte.HabilitarModeloView.as_view(), name='habilitar_modelo'),
    path('modelos_transporte/deshabilitar/<int:pk>/', modelo_transporte.DeshabilitarModeloView.as_view(), name='deshabilitar_modelo'),

    # PAISES
    path('paises/', pais.ListadoPaisesView.as_view(), name='paises'),
    path('paises/registrar/', pais.RegistrarPaisView.as_view(), name='registrar_pais'),
    path('paises/modificar/<int:pk>/', pais.ModificarPaisView.as_view(), name='modificar_pais'),
    path('paises/habilitar/<int:pk>/', pais.HabilitarPaisView.as_view(), name='habilitar_pais'),
    path('paises/deshabilitar/<int:pk>/', pais.DeshabilitarPaisView.as_view(), name='deshabilitar_pais'),

    # PARTES DEL CUERPO
    path('partes_cuerpo/', parte_cuerpo.ListadoPartesCuerpoView.as_view(), name='partes_cuerpo'),
    path('partes_cuerpo/registrar/', parte_cuerpo.RegistrarParteCuerpoView.as_view(), name='registrar_parte_cuerpo'),
    path('partes_cuerpo/modificar/<int:pk>/', parte_cuerpo.ModificarParteCuerpoView.as_view(), name='modificar_parte_cuerpo'),
    path('partes_cuerpo/habilitar/<int:pk>/', parte_cuerpo.HabilitarParteCuerpoView.as_view(), name='habilitar_parte_cuerpo'),
    path('partes_cuerpo/deshabilitar/<int:pk>/', parte_cuerpo.DeshabilitarParteCuerpoView.as_view(), name='deshabilitar_parte_cuerpo'),
]
