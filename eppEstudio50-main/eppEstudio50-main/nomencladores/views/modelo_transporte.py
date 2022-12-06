from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_modelo_transporte import ModeloForm
from nomencladores.models.modelo_transporte import Modelo


class ListadoModelosView(PermissionRequiredMixin, ListView):
    model = Modelo
    template_name = 'modelo_transporte/listado_modelos.html'
    paginate_by = 10
    permission = 'nomencladores.view_modelo'

    def get_queryset(self):
        modelos = Modelo.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            modelos = modelos.filter(nombre__icontains=q)

        return modelos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de modelos'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Modelos', 'href': reverse_lazy('modelos')}
        ]
        return context


class RegistrarModeloView(PermissionRequiredMixin, CreateView):
    model = Modelo
    template_name = "modelo_transporte/modelo_form.html"
    form_class = ModeloForm
    success_url = reverse_lazy('modelos')
    permission = 'nomencladores.add_modelo'

    def get_context_data(self, **kwargs):
        context = super(RegistrarModeloView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar modelo'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'modelo'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Modelo', 'href': reverse_lazy('modelos')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_modelo')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Modelo agregado con éxito.")
        return super(RegistrarModeloView, self).form_valid(form)


class ModificarModeloView(PermissionRequiredMixin, UpdateView):
    model = Modelo
    template_name = "modelo_transporte/modelo_form.html"
    form_class = ModeloForm
    success_url = reverse_lazy('modelos')
    permission = 'nomencladores.change_modelo'

    def get_context_data(self, **kwargs):
        context = super(ModificarModeloView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar modelo'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "modelo"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Modelo', 'href': reverse_lazy('modelos')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_modelo', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Modelo modificado con éxito.")
        return super(ModificarModeloView, self).form_valid(form)


class HabilitarModeloView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_modelo'

    def get(self, request, *args, **kwargs):
        modelo = Modelo.objects.get(id=self.kwargs['pk'])
        modelo.activo = True
        modelo.save()
        messages.add_message(request, messages.SUCCESS, "Modelo habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarModeloView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_modelo'

    def get(self, request, *args, **kwargs):
        modelo = Modelo.objects.get(id=self.kwargs['pk'])
        modelo.activo = False
        modelo.save()
        messages.add_message(request, messages.SUCCESS, "Modelo deshabilitado con éxito.")
        return JsonResponse({})


