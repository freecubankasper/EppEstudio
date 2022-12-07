# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.template.context_processors import request
from django.views.generic import TemplateView, ListView

from actor.models.actor import Actor
from core.utiles.filters import ActorFilter
from nomencladores.models.sub_categoria import SubCategoria


class TalentView(ListView):
    template_name = 'talent.html'
    model= Actor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['talentos'] = ActorFilter(self.request.GET, queryset=self.get_queryset())

        return context