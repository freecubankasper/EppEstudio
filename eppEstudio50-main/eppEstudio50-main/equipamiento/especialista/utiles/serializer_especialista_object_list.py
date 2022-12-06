# -*- coding: utf-8 -*-
import json
import datetime
import pytz


def listado_especialistas(especialistas):
    especialistas = [especialista_serializer(especialista) for especialista in especialistas]
    return json.dumps(especialistas)


def especialista_serializer(especialista):
    return {
        'EspecialistaId': especialista.id,
        'NúmeroCI': especialista.ci,
        'PrimerNombre': especialista.primer_nombre,
        'PrimerApellido': especialista.primer_apellido,
        'Apodo': especialista.apodo if especialista.apodo else "-",
        'Pais': especialista.pais.nombre,
        'Estado': especialista.activo,
        'FechaRegistro': str(especialista.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
    }
