from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from core.utiles.permission_required import PermissionRequiredMixin
from django.views import View
from django.contrib import messages
from equipo_proteccion_personal.models.factura import Factura
from equipo_proteccion_personal.models.numero_prefactura import NumeroPrefactura
from nomencladores.models import Entidad
import datetime


class ListadoFacturasView(PermissionRequiredMixin, ListView):
    model = Factura
    template_name = 'factura/listado_factura.html'
    paginate_by = 10
    permission = 'equipo_proteccion_personal.view_factura'

    def get_queryset(self):
        today = datetime.datetime.now()
        facturas = Factura.objects.all().order_by('-id')
        factura_habilitadas = Factura.objects.filter(activo=True)
        cantidad_eliminadas = 0
        for factura in factura_habilitadas:
            if factura.fecha_limite_pago <= today.date():
                cantidad_eliminadas += 1
                factura.delete()
        if cantidad_eliminadas == 1:
            messages.add_message(self.request, messages.ERROR,
                                 f"Se eliminó {cantidad_eliminadas} factura y sus equipos correspondientes por execeder la fecha límite de pago.")
        elif cantidad_eliminadas > 1:
            messages.add_message(self.request, messages.ERROR,
                                 f"Se eliminaron {cantidad_eliminadas} facturas y sus equipos correspondientes por execeder la fecha límite de pago.")

        estado_pago = self.request.GET.get('estado_pago')
        if estado_pago == "Pagado":
            estado_pago = True
        elif estado_pago == "No pagado":
            estado_pago = False
        if estado_pago is not None and estado_pago != "":
            facturas = facturas.filter(estado_pago=estado_pago)

        entidad = self.request.GET.get('entidad')
        if entidad is not None and entidad != "":
            facturas = facturas.filter(numero_prefactura__entidad_id=entidad)

        fecha_pago = self.request.GET.get('fecha_pago')
        if fecha_pago is not None and fecha_pago != "":
            facturas = facturas.filter(fecha_pago=fecha_pago)

        numero_prefactura = self.request.GET.get('numero_prefactura')
        if numero_prefactura is not None and numero_prefactura != "":
            facturas = facturas.filter(numero_prefactura_id=numero_prefactura)

        return facturas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de facturas'
        context['activar_equipos_proteccion_personal'] = True
        context['path'] = [
            {'name': 'Equipos de prtección personal'},
            {'name': 'Factura', 'href': reverse_lazy('facturas')}
        ]

        # Filtros
        context['entidades'] = Entidad.objects.filter(activo=True).order_by('nombre')
        context['numeros_prefactura'] = NumeroPrefactura.objects.filter(activo=True).order_by('numero_prefactura')
        #

        return context


class EliminarFacturaView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.delete_factura'

    def get(self, request, *args, **kwargs):
        factura = Factura.objects.get(id=self.kwargs['pk'])
        factura.delete()
        messages.add_message(request, messages.SUCCESS, "Factura eliminada con éxito.")
        return JsonResponse({})


class HabilitarFacturaView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.enable_factura'

    def get(self, request, *args, **kwargs):
        factura = Factura.objects.get(id=self.kwargs['pk'])
        factura.activo = True
        factura.save()
        messages.add_message(request, messages.SUCCESS, "Factura habilitada con éxito.")
        return JsonResponse({})


class DeshabilitarFacturaView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.disable_factura'

    def get(self, request, *args, **kwargs):
        factura = Factura.objects.get(id=self.kwargs['pk'])
        factura.activo = False
        factura.save()
        messages.add_message(request, messages.SUCCESS, "Factura deshabilitada con éxito.")
        return JsonResponse({})


class DetallesFacturaView(PermissionRequiredMixin, DetailView):
    template_name = 'factura/detalles_factura.html'
    model = Factura
    permission = 'equipo_proteccion_personal.view_factura'

    def get_context_data(self, **kwargs):
        context = super(DetallesFacturaView, self).get_context_data(**kwargs)
        context['titulo'] = 'Detalles de la factura'
        context['titulo_tabla'] = 'Detalles'
        context['activar_equipos_proteccion_personal'] = True
        context['path'] = [
            {'name': 'Equipos de prtección personal'},
            {'name': 'Factura', 'href': reverse_lazy('facturas')},
            {'name': 'Detalles', 'href': reverse_lazy('detalles_factura', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context


class PagarFactura(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.pagar_factura'

    def get(self, request, *args, **kwargs):
        numero_prefactura = request.GET.get('numero_prefactura')
        fecha_pago = request.GET.get('fecha_pago')
        factura = Factura.objects.filter(numero_prefactura_id=numero_prefactura)
        if not factura.exists():
            messages.add_message(self.request, messages.ERROR, "No existe ninguna factura con ese número de prefactura.")
            return HttpResponseRedirect(reverse_lazy('facturas'))
        factura = Factura.objects.filter(numero_prefactura_id=numero_prefactura, estado_pago=True)
        if factura.exists():
            messages.add_message(self.request, messages.ERROR, "La factura ya ha sido pagada.")
            return HttpResponseRedirect(reverse_lazy('facturas'))
        else:
            factura.estado_pago = True
            Factura.objects.filter(numero_prefactura_id=numero_prefactura).update(estado_pago=factura.estado_pago, fecha_pago=fecha_pago)
            messages.add_message(self.request, messages.SUCCESS, "Factura pagada con éxito.")
            return HttpResponseRedirect(reverse_lazy('facturas'))
