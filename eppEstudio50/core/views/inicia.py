# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from equipo_proteccion_personal.models.documento import Documento
from nomencladores.models.categoria import Categoria
from nomencladores.models.pais import Pais


class IniciaView(TemplateView):
    template_name = 'home-13.html'
    user = ''

    def get(self,request, **kwargs):
        context = super(IniciaView,self).get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['paises'] = Pais.objects.all()
        user = ''
        if self.request.user.is_authenticated:
            user = self.request.user.username
        return render(request, self.template_name, context)



