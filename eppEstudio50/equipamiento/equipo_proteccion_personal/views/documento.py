# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, ListView
from django.views.generic.base import View
from core.utiles.permission_required import PermissionRequiredMixin
from equipo_proteccion_personal.forms.form_documento import DocumentoForm

from equipo_proteccion_personal.models.documento import Documento


class ListadoDocumentosView(PermissionRequiredMixin, ListView):
    model = Documento
    template_name = 'documento/listado_documento.html'
    paginate_by = 10
    permission = 'equipo_proteccion_personal.view_documento'

    def get_queryset(self):
        documento = Documento.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            documento = documento.filter(nombre__icontains=q)

        return documento

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de documentos'
        context['activar_equipos_proteccion_personal'] = True
        context['path'] = [
            {'name': 'Equipos de prtección personal'},
            {'name': 'Documentos', 'href': reverse_lazy('documentos')}
        ]
        return context


class RegistrarDocumentoView(PermissionRequiredMixin, CreateView):
    model = Documento
    template_name = "documento/form_documento.html"
    form_class = DocumentoForm
    success_url = reverse_lazy('documentos')
    permission = 'equipo_proteccion_personal.add_documento'

    def get_context_data(self, **kwargs):
        context = super(RegistrarDocumentoView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar documento'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'documento'
        context['icono_form'] = 'plus'
        context['activar_equipos_proteccion_personal'] = True
        context['path'] = [
            {'name': 'Equipos de prtección personal'},
            {'name': 'Documento', 'href': reverse_lazy('documentos')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_documento')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Documento agregado con éxito.")
        return super(RegistrarDocumentoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Documento no agregado con éxito, revisar campos")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarDocumentoView(PermissionRequiredMixin, UpdateView):
    model = Documento
    template_name = "documento/form_documento.html"
    form_class = DocumentoForm
    success_url = reverse_lazy('documentos')
    permission = 'equipo_proteccion_personal.change_documento'

    def get_context_data(self, **kwargs):
        context = super(ModificarDocumentoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar documento'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "documento"
        context['icono_form'] = 'edit'
        context['activar_equipos_proteccion_personal'] = True
        context['path'] = [
            {'name': 'Equipos de prtección personal'},
            {'name': 'Documento', 'href': reverse_lazy('documentos')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_documento', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Documento modificado con éxito.")
        return super(ModificarDocumentoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Documento no modificado con éxito, revisar campos")
        return render(self.request, self.template_name, self.get_context_data())


class HabilitarDocumentoView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.enable_documento'

    def get(self, request, *args, **kwargs):
        documento = Documento.objects.get(id=self.kwargs['pk'])
        documento.activo = True
        documento.save()
        messages.add_message(request, messages.SUCCESS, "Documento habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarDocumentoView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.disable_documento'

    def get(self, request, *args, **kwargs):
        documento = Documento.objects.get(id=self.kwargs['pk'])
        documento.activo = False
        documento.save()
        messages.add_message(request, messages.SUCCESS, "Documento deshabilitado con éxito.")
        return JsonResponse({})


class EliminarDocumentoView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.delete_documento'

    def get(self, request, *args, **kwargs):
        documento = Documento.objects.get(id=self.kwargs['pk'])
        documento.delete()
        messages.add_message(request, messages.SUCCESS, "Documento eliminado con éxito.")
        return JsonResponse({})


class DescargarDocumentoView(View):
    permission = 'equipo_proteccion_personal.download_documento'

    def get(self, request, *args, **kwargs):
        documento = Documento.objects.get(id=self.kwargs['pk'])
        response = HttpResponse(documento.documento, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="%s"' % documento.documento
        return response
