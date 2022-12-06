from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_provincia import ProvinciaForm
from nomencladores.models.provincia import Provincia


class ListadoProvinciasView(PermissionRequiredMixin, ListView):
    model = Provincia
    template_name = 'provincia/listado_provincias.html'
    paginate_by = 10
    permission = 'nomencladores.view_provincia'

    def get_queryset(self):
        provincias = Provincia.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            provincias = provincias.filter(nombre__icontains=q)

        return provincias

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de provincias'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Provincias', 'href': reverse_lazy('provincias')}
        ]
        return context


class RegistrarProvinciaView(PermissionRequiredMixin, CreateView):
    model = Provincia
    template_name = "provincia/provincia_form.html"
    form_class = ProvinciaForm
    success_url = reverse_lazy('provincias')
    permission = 'nomencladores.add_provincia'

    def get_context_data(self, **kwargs):
        context = super(RegistrarProvinciaView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar provincia'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'provincia'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Provincia', 'href': reverse_lazy('provincias')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_provincia')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Provincia agregada con éxito.")
        return super(RegistrarProvinciaView, self).form_valid(form)


class ModificarProvinciaView(PermissionRequiredMixin, UpdateView):
    model = Provincia
    template_name = "provincia/provincia_form.html"
    form_class = ProvinciaForm
    success_url = reverse_lazy('provincias')
    permission = 'nomencladores.change_provincia'

    def get_context_data(self, **kwargs):
        context = super(ModificarProvinciaView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar provincia'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "provincia"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Provincia', 'href': reverse_lazy('provincias')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_provincia', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Provincia modificada con éxito.")
        return super(ModificarProvinciaView, self).form_valid(form)


class HabilitarProvinciaView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_provincia'

    def get(self, request, *args, **kwargs):
        provincia = Provincia.objects.get(id=self.kwargs['pk'])
        provincia.activo = True
        provincia.save()
        messages.add_message(request, messages.SUCCESS, "Provincia habilitada con éxito.")
        return JsonResponse({})


class DeshabilitarProvinciaView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_provincia'

    def get(self, request, *args, **kwargs):
        provincia = Provincia.objects.get(id=self.kwargs['pk'])
        provincia.activo = False
        provincia.save()
        messages.add_message(request, messages.SUCCESS, "Provincia deshabilitada con éxito.")
        return JsonResponse({})

