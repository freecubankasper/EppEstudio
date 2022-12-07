# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

register = template.Library()


def pagina_actual(pagina_anterior):
    if not pagina_anterior:
        return 1
    try:
        return int(pagina_anterior.split('page=')[1]) + 1
    except:
        return 2


def pagina_anterior(pag_anterior):
    if not pag_anterior:
        return None
    try:
        return int(pag_anterior.split('page=')[1])
    except:
        return 1


def pagina_siguiente(pag_siguiente):
    if not pag_siguiente:
        return 1
    try:
        return int(pag_siguiente.split('page=')[1])
    except:
        return 1


def ultima_pagina(total):
    return int(total / 10) + 1


register.filter('pagina_actual', pagina_actual)
register.filter('pagina_anterior', pagina_anterior)
register.filter('pagina_siguiente', pagina_siguiente)
register.filter('ultima_pagina', ultima_pagina)
