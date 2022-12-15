# -*- coding: utf-8 -*-
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from core.utiles.tests import send_email_contact
from equipo_proteccion_personal.models.documento import Documento


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        documentos = Documento.objects.filter(activo=True).order_by('nombre')
        return {'documentos': documentos}


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        documentos = Documento.objects.filter(activo=True).order_by('nombre')
        return {'documentos': documentos}


class ContactEmailView(View):
    messages = ''

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        budget = request.POST.get('budget')
        messaged = request.POST.get('message')
        send_email_contact(first_name, last_name, email, phone, budget, messaged)
        messages.add_message(request, messages.SUCCESS, "Usuario registrado con éxito.")
        return HttpResponseRedirect(reverse_lazy('contact'), {messages: 'messages'})


class CatalogView(TemplateView):
    template_name = 'catalog.html'

    def get_context_data(self, **kwargs):
        documentos = Documento.objects.filter(activo=True).order_by('nombre')
        return {'documentos': documentos}
