# -*- coding: utf-8 -*-
import json
import datetime
import pytz


def listado_organismos(organismos):
    organismos = [organismo_serializer(organismo) for organismo in organismos]
    return json.dumps(organismos)


def organismo_serializer(organismo):
    return {
        'OrganismoId': organismo.id,
        'Organismo': organismo.nombre,
        'Siglas': organismo.siglas,
        'FechaRegistro': str(organismo.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(organismo.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': organismo.activo,
    }


def listado_entidades(entidades):
    if entidades:
        entidades = [entidad_serializer(entidad) for entidad in entidades]
        return json.dumps(entidades)
    else:
        return


def entidad_serializer(entidad):
    return {
        'EntidadId': entidad.id,
        'Entidad': entidad.nombre,
        'TipoEntidad': entidad.tipo_entidad_nacional.nombre if entidad.tipo_entidad_nacional else entidad.tipo_entidad_extranjera.nombre,
        'Pais': entidad.pais.nombre,
        'FechaRegistro': str(entidad.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': entidad.activo,
    }


def listado_idiomas(idiomas):
    idiomas = [idioma_serializer(idioma) for idioma in idiomas]
    return json.dumps(idiomas)


def idioma_serializer(idioma):
    return {
        'IdiomaId': idioma.id,
        'Nombre': idioma.nombre,
        'FechaRegistro': str(idioma.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(idioma.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': idioma.activo,
    }


def listado_municipios(municipios):
    municipios = [municipio_serializer(municipio) for municipio in municipios]
    return json.dumps(municipios)


def municipio_serializer(municipio):
    return {
        'MunicipioId': municipio.id,
        'Municipio': municipio.nombre,
        'Provincia': municipio.provincia.nombre,
        'FechaRegistro': str(municipio.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(municipio.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': municipio.activo,
    }


def listado_provincias(provincias):
    provincias = [provincia_serializer(provincia) for provincia in provincias]
    return json.dumps(provincias)


def provincia_serializer(provincia):
    return {
        'ProvinciaId': provincia.id,
        'Provincia': provincia.nombre,
        'FechaRegistro': str(provincia.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(provincia.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': provincia.activo,
    }


def listado_tipos_entidad(tipos_entidad):
    tipos_entidad = [tipo_entidad_serializer(tipo_entidad) for tipo_entidad in tipos_entidad]
    return json.dumps(tipos_entidad)


def tipo_entidad_serializer(tipo_entidad):
    return {
        'TipoEntidadId': tipo_entidad.id,
        'Nombre': tipo_entidad.nombre,
        'Tipo': tipo_entidad.tipo,
        'FechaRegistro': str(tipo_entidad.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(tipo_entidad.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': tipo_entidad.activo,
    }


def listado_categorias(categorias):
    categorias = [categoria_serializer(categoria) for categoria in categorias]
    return json.dumps(categorias)


def categoria_serializer(categoria):
    return {
        'CategoriaId': categoria.id,
        'Nombre': categoria.nombre,
        'FechaRegistro': str(categoria.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(categoria.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': categoria.activo,
    }


def listado_categorias_lic_conduccion(categorias_licencia):
    categorias_licencia = [categoria_lic_conduccion_serializer(categoria_licencia) for categoria_licencia in categorias_licencia]
    return json.dumps(categorias_licencia)


def categoria_lic_conduccion_serializer(categoria_licencia):
    return {
        'CategoriaLicenciaId': categoria_licencia.id,
        'Nombre': categoria_licencia.nombre,
        'FechaRegistro': str(categoria_licencia.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(categoria_licencia.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': categoria_licencia.activo,
    }


def listado_categorias_servicio(categorias_servicio):
    categorias_servicio = [categoria_servicio_serializer(categoria_servicio) for categoria_servicio in categorias_servicio]
    return json.dumps(categorias_servicio)


def categoria_servicio_serializer(categoria_servicio):
    return {
        'CategoriaServicioId': categoria_servicio.id,
        'Nombre': categoria_servicio.nombre,
        'FechaRegistro': str(categoria_servicio.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(categoria_servicio.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': categoria_servicio.activo,
    }


def listado_subs_categoria(subs_categoria):
    subs_categoria = [sub_categoria_serializer(sub_categoria) for sub_categoria in subs_categoria]
    return json.dumps(subs_categoria)


def sub_categoria_serializer(sub_categoria):
    return {
        'SubCategoriaId': sub_categoria.id,
        'Nombre': sub_categoria.nombre,
        'CategoriaServicio': sub_categoria.categoria_servicio.nombre,
        'FechaRegistro': str(sub_categoria.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(sub_categoria.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': sub_categoria.activo,
    }


def listado_tipos_suelo(tipos_suelo):
    tipos_suelo = [tipo_suelo_serializer(tipo_suelo) for tipo_suelo in tipos_suelo]
    return json.dumps(tipos_suelo)


def tipo_suelo_serializer(tipo_suelo):
    return {
        'TipoSueloId': tipo_suelo.id,
        'Nombre': tipo_suelo.nombre,
        'FechaRegistro': str(tipo_suelo.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(tipo_suelo.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': tipo_suelo.activo,
    }


def listado_tipos_arquitectura(tipos_arquitectura):
    tipos_arquitectura = [tipo_arquitectura_serializer(tipo_arquitectura) for tipo_arquitectura in tipos_arquitectura]
    return json.dumps(tipos_arquitectura)


def tipo_arquitectura_serializer(tipo_arquitectura):
    return {
        'TipoArquitecturaId': tipo_arquitectura.id,
        'Nombre': tipo_arquitectura.nombre,
        'FechaRegistro': str(tipo_arquitectura.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(tipo_arquitectura.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': tipo_arquitectura.activo,
    }


def listado_tipos_lugar(tipos_lugar):
    tipos_lugar = [tipo_lugar_serializer(tipo_lugar) for tipo_lugar in tipos_lugar]
    return json.dumps(tipos_lugar)


def tipo_lugar_serializer(tipo_lugar):
    return {
        'TipoLugarId': tipo_lugar.id,
        'Nombre': tipo_lugar.nombre,
        'FechaRegistro': str(tipo_lugar.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(tipo_lugar.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': tipo_lugar.activo,
    }


def listado_tipos_vehiculo(tipos_vehiculo):
    tipos_vehiculo = [tipo_vehiculo_serializer(tipo_vehiculo) for tipo_vehiculo in tipos_vehiculo]
    return json.dumps(tipos_vehiculo)


def tipo_vehiculo_serializer(tipo_vehiculo):
    return {
        'TipoVehiculoId': tipo_vehiculo.id,
        'Nombre': tipo_vehiculo.nombre,
        'FechaRegistro': str(tipo_vehiculo.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(tipo_vehiculo.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': tipo_vehiculo.activo,
    }


def listado_marcas_comercial_registrada(marcas_comercial_registrada):
    marcas_comercial_registrada = [marca_comercial_registrada_serializer(marca_comercial_registrada) for marca_comercial_registrada in marcas_comercial_registrada]
    return json.dumps(marcas_comercial_registrada)


def marca_comercial_registrada_serializer(marca_comercial_registrada):
    return {
        'MarcaComercialRegistradaId': marca_comercial_registrada.id,
        'Nombre': marca_comercial_registrada.nombre,
        'FechaRegistro': str(marca_comercial_registrada.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(marca_comercial_registrada.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': marca_comercial_registrada.activo,
    }


def listado_modelos_transporte(modelos):
    modelos = [modelo_transporte_serializer(modelo) for modelo in modelos]
    return json.dumps(modelos)


def modelo_transporte_serializer(modelo):
    return {
        'ModeloId': modelo.id,
        'Nombre': modelo.nombre,
        'FechaRegistro': str(modelo.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(modelo.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': modelo.activo,
    }


def listado_marcas_transporte(marcas):
    marcas = [marca_transporte_serializer(marca) for marca in marcas]
    return json.dumps(marcas)


def marca_transporte_serializer(marca):
    return {
        'MarcaId': marca.id,
        'Nombre': marca.nombre,
        'FechaRegistro': str(marca.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(marca.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': marca.activo,
    }


def listado_paises(paises):
    paises = [pais_serializer(pais) for pais in paises]
    return json.dumps(paises)


def pais_serializer(pais):
    return {
        'PaisId': pais.id,
        'Pais': pais.nombre,
        'Nacionalidad': pais.nacionalidad,
        'Siglas': pais.siglas,
        'FechaRegistro': str(pais.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(pais.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': pais.activo,
    }


def listado_partes_cuerpo(partes_cuerpo):
    partes_cuerpo = [parte_cuerpo_serializer(parte_cuerpo) for parte_cuerpo in partes_cuerpo]
    return json.dumps(partes_cuerpo)


def parte_cuerpo_serializer(parte_cuerpo):
    return {
        'ParteCuerpoId': parte_cuerpo.id,
        'Nombre': parte_cuerpo.nombre,
        'FechaRegistro': str(parte_cuerpo.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(parte_cuerpo.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
        'Estado': parte_cuerpo.activo,
    }