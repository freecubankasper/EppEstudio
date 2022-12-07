import datetime
import os
import random
import string
from django.contrib import messages
from django.contrib.staticfiles import finders
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse_lazy, reverse
from django.utils.baseconv import base64
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from core.utiles.permission_required import PermissionRequiredMixin
from epp import settings
from equipo_proteccion_personal.forms.form_equipo_proteccion_personal import EquipoProteccionPersonalForm
from equipo_proteccion_personal.models.equipo_proteccion_personal import EquipoProteccionPersonal, HistorialEPPRenovado
from equipo_proteccion_personal.models.factura import Factura
from equipo_proteccion_personal.models.numero_prefactura import NumeroPrefactura
from equipo_proteccion_personal.utiles.pdfs import to_base64
from nomencladores.models import Entidad
from nomencladores.models.categoria import Categoria


class ListadoEquipoProteccionPersonalView(PermissionRequiredMixin, ListView):
    model = EquipoProteccionPersonal
    template_name = 'equipo_proteccion_personal/listado_equipos_proteccion_personal.html'
    paginate_by = 10
    permission = 'equipo_proteccion_personal.view_equipoproteccionpersonal'

    def get_queryset(self):
        today = datetime.datetime.now()
        equipos = EquipoProteccionPersonal.objects.all().order_by('-id')
        equipos_habilitados = EquipoProteccionPersonal.objects.filter(activo=True)
        equipos_vencidos = 0
        for equipo in equipos_habilitados:
            if equipo.fecha_vencimiento_certificado <= today.date():
                equipo.activo = False
                equipo.save()
            if not equipo.activo:
                equipos_vencidos += 1
        if equipos_vencidos == 1:
            messages.add_message(self.request, messages.ERROR,
                                 f"Se ha vencido {equipos_vencidos} Equipo de Protección Personal.")
        if equipos_vencidos > 1:
            messages.add_message(self.request, messages.ERROR,
                                 f"Se han vencido {equipos_vencidos} Equipos de Protección Personal.")

        nombre = self.request.GET.get('nombre')
        if nombre is not None and nombre != "":
            equipos = equipos.filter(nombre__icontains=nombre)

        categoria = self.request.GET.get('categoria')
        if categoria is not None and categoria != "":
            equipos = equipos.filter(categoria_id=categoria)

        entidad = self.request.GET.get('entidad')
        if entidad is not None and entidad != "":
            equipos = equipos.filter(numero_prefactura__entidad_id=entidad)

        modelo = self.request.GET.get('modelo')
        if modelo is not None and modelo != "":
            equipos = equipos.filter(modelo_id=modelo)

        fecha_vencimiento_certificado = self.request.GET.get('fecha_vencimiento_certificado')
        if fecha_vencimiento_certificado is not None and fecha_vencimiento_certificado != "":
            equipos = equipos.filter(fecha_vencimiento_certificado=fecha_vencimiento_certificado)

        numero_prefactura = self.request.GET.get('numero_prefactura')
        if numero_prefactura is not None and numero_prefactura != "":
            equipos = equipos.filter(numero_prefactura_id=numero_prefactura)

        numero_referencia = self.request.GET.get('numero_referencia')
        if numero_referencia is not None and numero_referencia != "":
            equipos = equipos.filter(numero_referencia__exact=numero_referencia)

        estado_vencimiento = self.request.GET.get('estado_vencimiento')
        if estado_vencimiento == "Vigente":
            estado_vencimiento = True
        elif estado_vencimiento == "Vencido":
            estado_vencimiento = False
        if estado_vencimiento is not None and estado_vencimiento != "":
            equipos = equipos.filter(activo=estado_vencimiento)

        estado_pago = self.request.GET.get('estado_pago')
        if estado_pago == "Pagado":
            estado_pago = True
        elif estado_pago == "No pagado":
            estado_pago = False
        if estado_pago is not None and estado_pago != "":
            equipos = equipos.filter(factura__estado_pago=estado_pago)

        return equipos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de equipos de protección personal'
        context['activar_equipos_proteccion_personal'] = True
        context['path'] = [
            {'name': 'Equipo de protección personal', 'href': reverse_lazy('equipos_proteccion_personal')}
        ]

        # Filtros
        context['categorias'] = Categoria.objects.filter(activo=True).order_by('nombre')
        context['entidades'] = Entidad.objects.filter(activo=True).order_by('nombre')
        context['numeros_prefactura'] = NumeroPrefactura.objects.filter(activo=True).order_by('numero_prefactura')
        #

        return context


class RegistrarEquipoProteccionPersonalView(PermissionRequiredMixin, CreateView):
    model = EquipoProteccionPersonal
    template_name = "equipo_proteccion_personal/equipo_proteccion_personal_form.html"
    form_class = EquipoProteccionPersonalForm
    success_url = reverse_lazy('equipos_proteccion_personal')
    permission = 'equipo_proteccion_personal.add_equipoproteccionpersonal'

    def get_context_data(self, **kwargs):
        context = super(RegistrarEquipoProteccionPersonalView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar equipo de protección personal'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'equipo de protección personal'
        context['icono_form'] = 'plus'
        context['activar_equipos_proteccion_personal'] = True
        context['path'] = [
            {'name': 'Equipo de protección personal', 'href': reverse_lazy('equipos_proteccion_personal')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_equipo_proteccion_personal')}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        equipo = form.save(commit=False)
        equipo.usuario = self.request.user
        equipo.save()
        equipo_registrado = form.save(commit=False)
        equipos = EquipoProteccionPersonal.objects.filter(
            marca_comercial_registrada=equipo_registrado.marca_comercial_registrada, modelo=equipo_registrado.modelo,
            numero_referencia=equipo_registrado.numero_referencia)
        if equipos.count() >= 1:
            equipo_registrado.equipo_ya_certificado = True
            equipo_registrado.save()
        messages.add_message(self.request, messages.SUCCESS, "Equipo de protección personal agregado con éxito.")
        return super(RegistrarEquipoProteccionPersonalView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.add_message(self.request, messages.ERROR, "Equipo de protección personal no agregado con éxito, revisar campos")
        context = self.get_context_data()
        context['form'] = form
        return render(self.request, self.template_name, context)


class ModificarEquipoProteccionPersonalView(PermissionRequiredMixin, UpdateView):
    model = EquipoProteccionPersonal
    template_name = "equipo_proteccion_personal/equipo_proteccion_personal_form.html"
    form_class = EquipoProteccionPersonalForm
    success_url = reverse_lazy('equipos_proteccion_personal')
    permission = 'equipo_proteccion_personal.change_equipoproteccionpersonal'

    def get_context_data(self, **kwargs):
        context = super(ModificarEquipoProteccionPersonalView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar equipo de protección personal'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "equipo de protección personal"
        context['icono_form'] = 'edit'
        context['activar_equipos_proteccion_personal'] = True
        context['path'] = [
            {'name': 'Equipo de protección personal', 'href': reverse_lazy('equipos_proteccion_personal')},
            {'name': 'Modificar',
             'href': reverse_lazy('modificar_equipo_proteccion_personal', kwargs={'pk': self.kwargs['pk']})}
        ]
        return context

    def form_valid(self, form):
        usuario = self.request.user
        form.usuario = usuario
        form.save()
        equipo_registrado = form.save(commit=False)
        equipos = EquipoProteccionPersonal.objects.filter(
            marca_comercial_registrada=equipo_registrado.marca_comercial_registrada, modelo=equipo_registrado.modelo,
            numero_referencia=equipo_registrado.numero_referencia)
        if equipos.count() >= 1:
            equipo_registrado.equipo_ya_certificado = True
            equipo_registrado.save()
        messages.add_message(self.request, messages.SUCCESS, "Equipo de protección personal modificado con éxito.")
        return super(ModificarEquipoProteccionPersonalView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Equipo de protección personal no modificado con éxito, revisar campos")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarEquipoProteccionPersonalView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.delete_equipoproteccionpersonal'

    def get(self, request, *args, **kwargs):
        equipo = EquipoProteccionPersonal.objects.get(id=self.kwargs['pk'])
        equipo.delete()
        messages.add_message(request, messages.SUCCESS, "Equipo de protección personal eliminado con éxito.")
        return JsonResponse({})


class HabilitarEquipoProteccionPersonalView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.enable_equipo_proteccion_personal'

    def get(self, request, *args, **kwargs):
        equipo = EquipoProteccionPersonal.objects.get(id=self.kwargs['pk'])
        equipo.activo = True
        equipo.save()
        messages.add_message(request, messages.SUCCESS, "Equipo de protección personal validado con éxito.")
        return JsonResponse({})


class DeshabilitarEquipoProteccionPersonalView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.disable_equipo_proteccion_personal'

    def get(self, request, *args, **kwargs):
        equipo = EquipoProteccionPersonal.objects.get(id=self.kwargs['pk'])
        equipo.activo = False
        equipo.save()
        messages.add_message(request, messages.SUCCESS, "Equipo de protección personal vencido con éxito.")
        return JsonResponse({})


class EliminarEquiposProteccionPersonalSeleccionadosView(PermissionRequiredMixin, TemplateView):
    permission = 'equipo_proteccion_personal.delete_equipo_proteccion_personal_seleccionados'

    def get(self, request, *args, **kwargs):

        try:
            ids = request.GET.get('ids').split(',')
            EquipoProteccionPersonal.objects.filter(id__in=ids).delete()

            mensaje = "Equipos de protección personal eliminados con éxito." if ids.__len__() > 1 else "Equipo de protección personal eliminado con éxito."
            messages.add_message(request, messages.SUCCESS, mensaje)

        except:
            messages.add_message(request, messages.ERROR, "Ocurrió un error durante la operación.")

        return JsonResponse({})


class DetallesEquipoPoteccionPersonalView(PermissionRequiredMixin, DetailView):
    template_name = 'equipo_proteccion_personal/detalles_equipo_proteccion_personal.html'
    model = EquipoProteccionPersonal
    permission = 'equipo_proteccion_personal.view_equipoproteccionpersonal'

    def get_context_data(self, **kwargs):
        context = super(DetallesEquipoPoteccionPersonalView, self).get_context_data(**kwargs)
        context['titulo'] = 'Detalles del equipo de protección personal'
        context['titulo_tabla'] = 'Detalles'
        context['activar_equipos_proteccion_personal'] = True
        context['path'] = [
            {'name': 'Equipo de protección personal', 'href': reverse_lazy('equipos_proteccion_personal')},
            {'name': 'Detalles',
             'href': reverse_lazy('detalles_equipo_proteccion_personal', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context


class RenovarEquipoProteccionPersonalView(PermissionRequiredMixin, TemplateView):
    template_name = "equipo_proteccion_personal/renovar_equipo_proteccion_personal.html"
    form_class = EquipoProteccionPersonalForm
    permission = 'equipo_proteccion_personal.renew_equipo_proteccion_personal'

    def get(self, request, *args, **kwargs):
        context = super(RenovarEquipoProteccionPersonalView, self).get_context_data(**kwargs)
        context['titulo'] = 'Renovar equipo de protección personal'
        context['titulo_tabla'] = 'Renovación y cambio de número de prefactura del EPP'
        context['icono_form'] = 'check-square'
        context['activar_equipos_proteccion_personal'] = True
        context['path'] = [
            {'name': 'Equipo de protección personal', 'href': reverse_lazy('equipos_proteccion_personal')},
            {'name': 'Renovar', 'href': reverse_lazy('renovar_equipo_proteccion_personal', kwargs={'pk': self.kwargs['pk']})},
        ]

        context['numeros_prefactura'] = NumeroPrefactura.objects.filter(activo=True).order_by('numero_prefactura')
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        equipo = EquipoProteccionPersonal.objects.get(id=self.kwargs['pk'])
        fecha_actual = datetime.datetime.now()
        numero_prefactura = request.POST.get('numero_prefactura')
        equipo.numero_prefactura_id = numero_prefactura
        factura = Factura.objects.filter(numero_prefactura_id=numero_prefactura)
        if factura.exists():
            context = {
                'titulo': 'Renovar equipo de protección personal',
                'titulo_tabla': 'Renovación y cambio de número de prefactura del EPP',
                'icono_form': 'check-square',
                'numeros_prefactura': NumeroPrefactura.objects.filter(activo=True).order_by('numero_prefactura'),
                'activar_equipos_proteccion_personal': True,
                'path': [
                    {'name': 'Equipo de protección personal', 'href': reverse_lazy('equipos_proteccion_personal')},
                    {'name': 'Renovar', 'href': reverse_lazy('renovar_equipo_proteccion_personal', kwargs={'pk': self.kwargs['pk']})},
                ]

            }
            messages.add_message(self.request, messages.ERROR, "Ingrese otro número, ya existen equipos facturados con este número de prefactura")
            return render(self.request, self.template_name, context)
        elif not equipo.renovado:
            equipo.renovado = True
            equipo.activo = True
            equipo.factura_id = None
            equipo.save()
            HistorialEPPRenovado.objects.create(equipo=equipo, renovado=equipo.renovado)
            messages.add_message(self.request, messages.SUCCESS, "Equipo de protección personal renovado con éxito.")
            return redirect(reverse("equipos_proteccion_personal"))


class FacturaPDFView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.export_factura'

    def get(self, request, *args, **kwargs):
        numero_prefactura = request.GET.get('numero_prefactura')
        equipos_prefactura = EquipoProteccionPersonal.objects.filter(numero_prefactura_id=numero_prefactura, activo=True)
        if not equipos_prefactura.exists():
            messages.add_message(self.request, messages.ERROR,
                                 "No existe ningún equipo con ese número de prefactura.")
            return HttpResponseRedirect(reverse_lazy('equipos_proteccion_personal'))
        template_path = 'pdfs/factura_pdf.html'
        if not request.user.has_perm('equipo_proteccion_personal.export_factura'):
            raise PermissionDenied
        title = f'FACTURA'
        numero_prefactura_factura = NumeroPrefactura.objects.get(id=numero_prefactura)
        elaborado_nombre = request.GET.get('elaborado_nombre')
        elaborado_cargo = request.GET.get('elaborado_cargo')
        revisado_nombre = request.GET.get('revisado_nombre')
        revisado_cargo = request.GET.get('revisado_cargo')
        entregado_registrado_nombre = request.GET.get('entregado_registrado_nombre')
        entregado_registrado_cargo = request.GET.get('entregado_registrado_cargo')
        fecha_actual = datetime.datetime.today().strftime(("%d/%m/%y"))
        tipo_pago = request.GET.get('tipo_pago')
        total_cup = 0
        total_mlc = 0
        for equipo in equipos_prefactura:
            if tipo_pago == "CUP":
                if equipo.renovado:
                    total_cup += equipo.categoria.precio_renovado_cup
                elif not equipo.renovado and not equipo.equipo_ya_certificado:
                    total_cup += equipo.categoria.precio_cup
                elif equipo.equipo_ya_certificado:
                    total_cup += equipo.categoria.precio_equipo_ya_certificado_cup
            elif tipo_pago == "MLC":
                if equipo.renovado:
                    total_mlc += equipo.categoria.precio_renovado_mlc
                elif not equipo.renovado and not equipo.equipo_ya_certificado:
                    total_mlc += equipo.categoria.precio_mlc
                elif equipo.equipo_ya_certificado:
                    total_mlc += equipo.categoria.precio_equipo_ya_certificado_mlc
        data = {
            'title': title,
            'fecha_actual': fecha_actual,
            'numero_prefactura': numero_prefactura_factura,
            'equipos_prefactura': equipos_prefactura,
            'elaborado_nombre': elaborado_nombre,
            'elaborado_cargo': elaborado_cargo,
            'revisado_nombre': revisado_nombre,
            'revisado_cargo': revisado_cargo,
            'entregado_registrado_nombre': entregado_registrado_nombre,
            'entregado_registrado_cargo': entregado_registrado_cargo,
            'cantidad': equipos_prefactura.count(),
            'total_cup': total_cup,
            'total_mlc': total_mlc,
            'tipo_pago': tipo_pago,
            'componentes': {'direccion': 'Calle 23 e/ O y P, Vedado, Plaza de la Revolución.',
                            'codigo': '262.0.0026',
                            'numero_cuenta': '0407610011430112 BICSA, Ayestaràn y 20 de Mayo.',
                            'titular': 'MTSS.- Oficina Permiso de Trabajo', 'telefono': '78351641',
                            'email': 'valia.carbo@mtss.gob.cu, ariel.gonzalez@mtss.gob.cu, yudelsis.ametller@mtss.gob.cu, yanely.reyes@mtss.gob.cu'},
            'header': to_base64(os.path.join(settings.BASE_DIR, 'static', 'img', 'logos', 'logo_factura.png')),
            'PROD': settings.PRODUCTION,

        }
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{title}.pdf"'
        template = get_template(template_path)
        html = template.render(data)

        # create a pdf

        return response


class PreFacturaPDFView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.export_prefactura'

    def get(self, request, *args, **kwargs):
        numero_prefactura = request.GET.get('numero_prefactura')
        equipos_prefactura = EquipoProteccionPersonal.objects.filter(numero_prefactura_id=numero_prefactura,
                                                                     activo=True)
        if not equipos_prefactura.exists():
            messages.add_message(self.request, messages.ERROR,
                                 "No existe ningún equipo con ese número de prefactura.")
            return HttpResponseRedirect(reverse_lazy('equipos_proteccion_personal'))
        template_path = 'pdfs/prefactura_pdf.html'
        if not request.user.has_perm('equipo_proteccion_personal.export_prefactura'):
            raise PermissionDenied
        numero_prefactura_factura = NumeroPrefactura.objects.get(id=numero_prefactura)
        title = f'PREFACTURA'
        elaborado_nombre = request.GET.get('elaborado_nombre')
        elaborado_cargo = request.GET.get('elaborado_cargo')
        revisado_nombre = request.GET.get('revisado_nombre')
        revisado_cargo = request.GET.get('revisado_cargo')
        entregado_registrado_nombre = request.GET.get('entregado_registrado_nombre')
        entregado_registrado_cargo = request.GET.get('entregado_registrado_cargo')
        fecha_actual = datetime.datetime.today().strftime(("%d/%m/%y"))
        tipo_pago = request.GET.get('tipo_pago')
        total_cup = 0
        total_mlc = 0
        for equipo in equipos_prefactura:
            if tipo_pago == "CUP":
                if equipo.renovado:
                    total_cup += equipo.categoria.precio_renovado_cup
                elif not equipo.renovado and not equipo.equipo_ya_certificado:
                    total_cup += equipo.categoria.precio_cup
                elif equipo.equipo_ya_certificado:
                    total_cup += equipo.categoria.precio_equipo_ya_certificado_cup
            elif tipo_pago == "MLC":
                if equipo.renovado:
                    total_mlc += equipo.categoria.precio_renovado_mlc
                elif not equipo.renovado and not equipo.equipo_ya_certificado:
                    total_mlc += equipo.categoria.precio_mlc
                elif equipo.equipo_ya_certificado:
                    total_mlc += equipo.categoria.precio_equipo_ya_certificado_mlc
        data = {
            'title': title,
            'fecha_actual': fecha_actual,
            'numero_prefactura': numero_prefactura_factura,
            'equipos_prefactura': equipos_prefactura,
            'elaborado_nombre': elaborado_nombre,
            'elaborado_cargo': elaborado_cargo,
            'revisado_nombre': revisado_nombre,
            'revisado_cargo': revisado_cargo,
            'entregado_registrado_nombre': entregado_registrado_nombre,
            'entregado_registrado_cargo': entregado_registrado_cargo,
            'cantidad': equipos_prefactura.count(),
            'total_cup': total_cup,
            'total_mlc': total_mlc,
            'tipo_pago': tipo_pago,
            'componentes': {'direccion': 'Calle 23 e/ O y P, Vedado, Plaza de la Revolución.',
                            'codigo': '262.0.0026',
                            'numero_cuenta': '0407610011430112 BICSA, Ayestaràn y 20 de Mayo.',
                            'titular': 'MTSS.- Oficina Permiso de Trabajo', 'telefono': '78351641',
                            'email': 'valia.carbo@mtss.gob.cu, ariel.gonzalez@mtss.gob.cu, yudelsis.ametller@mtss.gob.cu, yanely.reyes@mtss.gob.cu'},
            'header': to_base64(os.path.join(settings.BASE_DIR, 'static', 'img', 'logos', 'logo_factura.png')),
            'PROD': settings.PRODUCTION,

        }
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{title}.pdf"'
        template = get_template(template_path)
        html = template.render(data)

        # create a pdf
        return response


class CertificadoEppPDFView(View):

    def get(self, request, *args, **kwargs):
        template_path = 'pdfs/certificado_epp_pdf.html'
        equipo = get_object_or_404(EquipoProteccionPersonal, pk=self.kwargs.get('pk'))
        if not request.user.has_perm('equipo_proteccion_personal.export_certificado_epp'):
            raise PermissionDenied
        title = f'REGISTRO Y DICTAMEN TÉCNICO'
        fecha_actual = datetime.datetime.now()
        mes = current_date_format(fecha_actual)
        data = {
            'title': title,
            'equipo': equipo,
            'fecha_actual': fecha_actual,
            'mes': mes,
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
    months = (
        "Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
        "Diciembre")
    month = months[date.month - 1]
    messsage = "{}".format(month)

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
