# -*- coding: utf-8 -*-
import json


def listado_usuarios(usuarios):
    usuarios = [usuario_serializer(usuario) for usuario in usuarios]
    return json.dumps(usuarios)


def usuario_serializer(usuario):
    return {
        'UsuarioId': usuario.id,
        'NombreUsuario': usuario.username,
        'NombreApellidos': usuario.fullname(),
        'Correo': usuario.email,
        'Telefono': usuario.telefono,
        'Estado': usuario.is_active,
    }


def listado_grupos(grupos):
    grupos = [grupo_serializer(grupo) for grupo in grupos]
    return json.dumps(grupos)


def grupo_serializer(grupo):
    return {
        'GroupsId': grupo.id,
        'Name': grupo.name,
    }
