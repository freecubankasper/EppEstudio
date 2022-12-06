# -*- coding: utf-8 -*-
import json
import datetime
import pytz

from epp.settings import MEDIA_URL


def listado_documentos(documentos):
    documentos = [documento_serializer(documento) for documento in documentos]
    return json.dumps(documentos)


def documento_serializer(documento):
    return {
        'DocumentoId': documento.id,
        'Nombre': documento.nombre,
        'Estado': documento.activo,
        'FechaRegistro': str(documento.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
        'FechaActualizacion': str(documento.fecha_actualizacion.strftime("%Y-%m-%d %H:%M:%S")),
    }
