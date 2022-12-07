# -*- coding: utf-8 -*-
import datetime
import os
import random
import string

from django.contrib.staticfiles import finders
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView
from django.views.generic.base import View

from core.utiles.permission_required import PermissionRequiredMixin
from epp import settings
from equipo_proteccion_personal.utiles.pdfs import to_base64
from nomencladores.forms.form_entidad import EntidadForm
from nomencladores.models import Organismo, Municipio
from nomencladores.models.entidad import Entidad, TipoEntidad
from nomencladores.models.pais import Pais


class ListadoEntidadesView(PermissionRequiredMixin, ListView):
    model = Entidad
    template_name = 'entidad/listado_entidades.html'
    paginate_by = 10
    permission = 'nomencladores.view_entidad'

    def get_queryset(self):
        entidades = Entidad.objects.all().order_by('nombre')

        nombre = self.request.GET.get('nombre')
        if nombre is not None and nombre != "":
            entidades = entidades.filter(nombre__icontains=nombre)

        pais = self.request.GET.get('pais')
        if pais is not None and pais != "":
            entidades = entidades.filter(pais_id=pais)

        municipio = self.request.GET.get('municipio')
        if municipio is not None and municipio != "":
            entidades = entidades.filter(municipio__id=municipio)

        num_contrato = self.request.GET.get('num_contrato')
        if num_contrato is not None and num_contrato != "":
            entidades = entidades.filter(num_contrato__icontains=num_contrato)

        tipo_entidad_nacional = self.request.GET.get('tipo_entidad_nacional')
        if tipo_entidad_nacional is not None and tipo_entidad_nacional != "":
            entidades = entidades.filter(tipo_entidad_nacional_id=tipo_entidad_nacional)

        tipo_entidad_extranjera = self.request.GET.get('tipo_entidad_extranjera')
        if tipo_entidad_extranjera is not None and tipo_entidad_extranjera != "":
            entidades = entidades.filter(tipo_entidad_extranjera_id=tipo_entidad_extranjera)

        return entidades

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de entidades'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Entidades', 'href': reverse_lazy('entidades')}
        ]

        # Filtros
        tipo_entidad_nacional = 'Nacional'
        tipo_entidad_extranjera = 'Extranjera'
        context['paises'] = Pais.objects.filter(activo=True).order_by('nombre')
        context['municipios'] = Municipio.objects.filter(activo=True).order_by('nombre')
        context['tipos_entidad_nacional'] = TipoEntidad.objects.filter(tipo__icontains=tipo_entidad_nacional, activo=True).order_by('nombre')
        context['tipos_entidad_extranjera'] = TipoEntidad.objects.filter(tipo__icontains=tipo_entidad_extranjera, activo=True).order_by('nombre')
        #

        return context


class RegistrarEntidadView(PermissionRequiredMixin, CreateView):
    model = Entidad
    template_name = "entidad/entidad_form.html"
    form_class = EntidadForm
    success_url = reverse_lazy('entidades')
    permission = 'nomencladores.add_entidad'

    def get_context_data(self, **kwargs):
        context = super(RegistrarEntidadView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar entidad'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'entidad'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Entidad', 'href': reverse_lazy('entidades')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_entidad')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Entidad agregada con éxito.")
        return super(RegistrarEntidadView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Entidad no agregada con éxito, revisar campos")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarEntidadView(PermissionRequiredMixin, UpdateView):
    model = Entidad
    template_name = "entidad/entidad_form.html"
    form_class = EntidadForm
    success_url = reverse_lazy('entidades')
    permission = 'nomencladores.change_entidad'

    def get_context_data(self, **kwargs):
        context = super(ModificarEntidadView, self).get_context_data(**kwargs)
        entidad = self.model.objects.get(id=self.kwargs['pk'])
        context['form'] = self.form_class(instance=entidad)
        context['titulo'] = 'Modificar entidad'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "entidad"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Entidad', 'href': reverse_lazy('entidades')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_entidad', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Entidad modificada con éxito.")
        return super(ModificarEntidadView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Entidad no modificada con éxito, revisar campos")
        return render(self.request, self.template_name, self.get_context_data())


class HabilitarEntidadView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_entidad'

    def get(self, request, *args, **kwargs):
        entidad = Entidad.objects.get(id=self.kwargs['pk'])
        entidad.activo = True
        entidad.save()
        messages.add_message(request, messages.SUCCESS, "Entidad habilitada con éxito.")
        return JsonResponse({})


class DeshabilitarEntidadView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_entidad'

    def get(self, request, *args, **kwargs):
        entidad = Entidad.objects.get(id=self.kwargs['pk'])
        entidad.activo = False
        entidad.save()
        messages.add_message(request, messages.SUCCESS, "Entidad deshabilitada con éxito.")
        return JsonResponse({})


class DetallesEntidadView(DetailView):
        template_name = 'entidad/detalles_entidad.html'
        model = Entidad
        permission = 'nomencladores.view_entidad'

        def get_context_data(self, **kwargs):
            context = super(DetallesEntidadView, self).get_context_data(**kwargs)
            context['titulo'] = 'Detalles de la entidad'
            context['titulo_tabla'] = 'Detalles'
            context['activar_nomencladores'] = True
            context['path'] = [
                {'name': 'Nomencladores'},
                {'name': 'Entidad', 'href': reverse_lazy('entidades')},
                {'name': 'Detalles', 'href': reverse_lazy('detalles_entidad', kwargs={'pk': self.kwargs['pk']})},
            ]
            return context


class CertificadoEntidadPDFView(View):

    def get(self, request, *args, **kwargs):
        template_path = 'entidad/pdfs/certificado_entidad_pdf.html'
        entidad = get_object_or_404(Entidad, pk=self.kwargs.get('pk'))
        if not request.user.has_perm('nomencladores.export_certificado_entidad'):
            raise PermissionDenied
        title = f'CERTIFICADO DE REGISTRO DE LA ENTIDAD'
        subtitle = f'Centro de Registro y Aprobación de los Equipos de Protección Personal'
        fecha_actual = datetime.date.today()
        dia = current_date_format(fecha_actual)
        data = {
            'title': title,
            'subtitle': subtitle,
            'entidad': entidad,
            'fecha_actual': fecha_actual,
            'dia': dia,
            'header': to_base64(os.path.join(settings.BASE_DIR, 'static', 'img', 'logos', 'logo_factura.png')),
            'PROD': settings.PRODUCTION,
        }
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{title}.pdf"'
        template = get_template(template_path)
        html = template.render(data)

        # create a pdf

        return response


def current_date_format(date):
    days = ("Domingo", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Lunes")
    day = days[date.month - 1]
    messsage = "{}".format(day)

    return messsage


def generate_dirt(length):
    source = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(source, k=length))


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    sUrl = settings.STATIC_URL  # Typically /static/
    sRoot = settings.STATICFILES_DIRS  # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL  # Typically /media/
    mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path
