# -*- coding: utf-8 -*-
import json
import datetime
import pytz


def listado_actores(actores):
    actores = [actor_serializer(actor) for actor in actores]
    return json.dumps(actores)


def actor_serializer(actor):
    return {
        'ActorId': actor.id,
        'NúmeroCI': actor.ci,
        'PrimerNombre': actor.primer_nombre,
        'PrimerApellido': actor.primer_apellido,
        'Apodo': actor.apodo if actor.apodo else "-",
        'Pais': actor.pais.nombre,
        'Estado': actor.activo,
        'FechaRegistro': str(actor.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")),
    }
