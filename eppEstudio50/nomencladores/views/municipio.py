from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_municipio import MunicipioForm
from nomencladores.models.municipio import Municipio


class ListadoMunicipiosView(PermissionRequiredMixin, ListView):
    model = Municipio
    template_name = 'municipio/listado_municipios.html'
    paginate_by = 10
    permission = 'nomencladores.view_municipio'

    def get_queryset(self):
        municipios = Municipio.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            municipios = municipios.filter(nombre__icontains=q)

        return municipios

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de municipios'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Municipios', 'href': reverse_lazy('municipios')}
        ]
        return context


class RegistrarMunicipioView(PermissionRequiredMixin, CreateView):
    model = Municipio
    template_name = "municipio/municipio_form.html"
    form_class = MunicipioForm
    success_url = reverse_lazy('municipios')
    permission = 'nomencladores.add_municipio'

    def get_context_data(self, **kwargs):
        context = super(RegistrarMunicipioView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar municipio'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'municipio'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Municipio', 'href': reverse_lazy('municipios')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_municipio')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Municipio agregado con éxito.")
        return super(RegistrarMunicipioView, self).form_valid(form)


class ModificarMunicipioView(PermissionRequiredMixin, UpdateView):
    model = Municipio
    template_name = "municipio/municipio_form.html"
    form_class = MunicipioForm
    success_url = reverse_lazy('municipios')
    permission = 'nomencladores.change_municipio'

    def get_context_data(self, **kwargs):
        context = super(ModificarMunicipioView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar municipio'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "municipio"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Municipio', 'href': reverse_lazy('municipios')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_municipio', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Municipio modificado con éxito.")
        return super(ModificarMunicipioView, self).form_valid(form)


class HabilitarMunicipioView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_municipio'

    def get(self, request, *args, **kwargs):
        municipio = Municipio.objects.get(id=self.kwargs['pk'])
        municipio.activo = True
        municipio.save()
        messages.add_message(request, messages.SUCCESS, "Municipio habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarMunicipioView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_municipio'

    def get(self, request, *args, **kwargs):
        municipio = Municipio.objects.get(id=self.kwargs['pk'])
        municipio.activo = False
        municipio.save()
        messages.add_message(request, messages.SUCCESS, "Municipio deshabilitado con éxito.")
        return JsonResponse({})


