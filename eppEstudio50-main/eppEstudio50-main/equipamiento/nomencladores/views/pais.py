from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.forms.form_pais import PaisForm
from nomencladores.models.pais import Pais


class ListadoPaisesView(PermissionRequiredMixin, ListView):
    model = Pais
    template_name = 'pais/listado_paises.html'
    paginate_by = 10
    permission = 'nomencladores.view_pais'

    def get_queryset(self):
        paises = Pais.objects.all().order_by('nombre')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            paises = paises.filter(nombre__icontains=q)

        return paises

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de países'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'Países', 'href': reverse_lazy('paises')}
        ]
        return context


class RegistrarPaisView(PermissionRequiredMixin, CreateView):
    model = Pais
    template_name = "pais/pais_form.html"
    form_class = PaisForm
    success_url = reverse_lazy('paises')
    permission = 'nomencladores.add_pais'

    def get_context_data(self, **kwargs):
        context = super(RegistrarPaisView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar país'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'país'
        context['icono_form'] = 'plus'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'País', 'href': reverse_lazy('paises')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_pais')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "País agregado con éxito.")
        return super(RegistrarPaisView, self).form_valid(form)


class ModificarPaisView(PermissionRequiredMixin, UpdateView):
    model = Pais
    template_name = "pais/pais_form.html"
    form_class = PaisForm
    success_url = reverse_lazy('paises')
    permission = 'nomencladores.change_pais'

    def get_context_data(self, **kwargs):
        context = super(ModificarPaisView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar país'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "país"
        context['icono_form'] = 'edit'
        context['activar_nomencladores'] = True
        context['path'] = [
            {'name': 'Nomencladores'},
            {'name': 'País', 'href': reverse_lazy('paises')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_pais', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "País modificado con éxito.")
        return super(ModificarPaisView, self).form_valid(form)


class HabilitarPaisView(PermissionRequiredMixin, View):
    permission = 'nomencladores.enable_pais'

    def get(self, request, *args, **kwargs):
        pais = Pais.objects.get(id=self.kwargs['pk'])
        pais.activo = True
        pais.save()
        messages.add_message(request, messages.SUCCESS, "País habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarPaisView(PermissionRequiredMixin, View):
    permission = 'nomencladores.disable_pais'

    def get(self, request, *args, **kwargs):
        pais = Pais.objects.get(id=self.kwargs['pk'])
        pais.activo = False
        pais.save()
        messages.add_message(request, messages.SUCCESS, "País deshabilitado con éxito.")
        return JsonResponse({})

