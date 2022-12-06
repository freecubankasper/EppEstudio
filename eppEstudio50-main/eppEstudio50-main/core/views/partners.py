# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from equipo_proteccion_personal.models.documento import Documento


class PartnersView(TemplateView):
    template_name = 'partners.html'

    def get_context_data(self, **kwargs):
        documentos = Documento.objects.filter(activo=True).order_by('nombre')
        return {'documentos': documentos}

