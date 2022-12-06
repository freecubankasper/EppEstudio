from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_marca_transporte import MarcaTransporteForm
from nomencladores.models.marca_transporte import MarcaTransporte


class ListadoMarcasTransaporteView(PermissionRequiredMixin, ListView):
    model = MarcaTransporte
    template_name = 'marca_transporte/listado_marcas_transporte.html'
    paginate_by = 10
    permission = 'nomencladores.view_marcatransporte'

    def get_queryset(self):
        marcas = MarcaTransporte.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            marcas = marcas.filter(nombre__icontains=q)

        return marcas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de marcas'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Marcas', 'href': reverse_lazy('marcas_transporte')}
        ]
        return context


class RegistrarMarcaTransaporteView(PermissionRequiredMixin, CreateView):
    model = MarcaTransporte
    template_name = "marca_transporte/marca_transporte_form.html"
    form_class = MarcaTransporteForm
    success_url = reverse_lazy('marcas_transporte')
    permission = 'nomencladores.add_marcatransporte'

    def get_context_data(self, **kwargs):
        context = super(RegistrarMarcaTransaporteView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar marca'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'marca'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Marca', 'href': reverse_lazy('marcas_transporte')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_marca_transporte')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Marca agregada con éxito.")
        return super(RegistrarMarcaTransaporteView, self).form_valid(form)


class ModificarMarcaTransaporteView(PermissionRequiredMixin, UpdateView):
    model = MarcaTransporte
    template_name = "marca_transporte/marca_transporte_form.html"
    form_class = MarcaTransporteForm
    success_url = reverse_lazy('marcas_transporte')
    permission = 'nomencladores.change_marcatransporte'

    def get_context_data(self, **kwargs):
        context = super(ModificarMarcaTransaporteView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar marca'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "marca"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Marca', 'href': reverse_lazy('marcas_transporte')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_marca_transporte', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Marca modificada con éxito.")
        return super(ModificarMarcaTransaporteView, self).form_valid(form)


class HabilitarMarcaTransaporteView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_marcatransporte'

    def get(self, request, *args, **kwargs):
        marca = MarcaTransporte.objects.get(id=self.kwargs['pk'])
        marca.activo = True
        marca.save()
        messages.add_message(request, messages.SUCCESS, "Marca habilitada con éxito.")
        return JsonResponse({})


class DeshabilitarMarcaTransaporteView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_marcatransporte'

    def get(self, request, *args, **kwargs):
        marca = MarcaTransporte.objects.get(id=self.kwargs['pk'])
        marca.activo = False
        marca.save()
        messages.add_message(request, messages.SUCCESS, "Marca deshabilitada con éxito.")
        return JsonResponse({})


