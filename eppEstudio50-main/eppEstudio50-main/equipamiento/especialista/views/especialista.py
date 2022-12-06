import datetime
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from core.utiles.permission_required import PermissionRequiredMixin
from especialista.forms.form_especialista import EspecialistaForm
from especialista.models.especialista import Especialista
from nomencladores.models import Municipio
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.idioma import Idioma
from nomencladores.models.pais import Pais
from nomencladores.models.sub_categoria import SubCategoria


class ListadoEspecialistasView(PermissionRequiredMixin, ListView):
    model = Especialista
    template_name = 'especialista/listado_especialista.html'
    paginate_by = 10
    permission = 'especialista.view_especialista'

    def get_queryset(self):
        especialistas = Especialista.objects.all().order_by('id')

        ci = self.request.GET.get('ci')
        if ci is not None and ci != "":
            especialistas = especialistas.filter(ci__contains=ci)

        numero_pasaporte = self.request.GET.get('numero_pasaporte')
        if numero_pasaporte is not None and numero_pasaporte != "":
            especialistas = especialistas.filter(num_pasaporte__contains=numero_pasaporte)

        primer_nombre = self.request.GET.get('primer_nombre')
        if primer_nombre is not None and primer_nombre != "":
            especialistas = especialistas.filter(primer_nombre__icontains=primer_nombre)

        segundo_nombre = self.request.GET.get('segundo_nombre')
        if segundo_nombre is not None and segundo_nombre != "":
            especialistas = especialistas.filter(segundo_nombre__icontains=segundo_nombre)

        primer_apellido = self.request.GET.get('primer_apellido')
        if primer_apellido is not None and primer_apellido != "":
            especialistas = especialistas.filter(primer_apellido__icontains=primer_apellido)

        segundo_apellido = self.request.GET.get('segundo_apellido')
        if segundo_apellido is not None and segundo_apellido != "":
            especialistas = especialistas.filter(segundo_apellido__icontains=segundo_apellido)

        apodo = self.request.GET.get('apodo')
        if apodo is not None and apodo != "":
            especialistas = especialistas.filter(apodo__icontains=apodo)

        sexo = self.request.GET.get('sexo')
        if sexo is not None and sexo != "":
            especialistas = especialistas.filter(sexo__contains=sexo)

        fecha_nacimiento = self.request.GET.get('fecha_nacimiento')
        if fecha_nacimiento is not None and fecha_nacimiento != "":
            especialistas = especialistas.filter(fecha_nacimiento=fecha_nacimiento)

        pais = self.request.GET.get('pais')
        if pais is not None and pais != "":
            especialistas = especialistas.filter(pais_id=pais)

        municipio = self.request.GET.get('municipio')
        if municipio is not None and municipio != "":
            especialistas = especialistas.filter(municipio__id=municipio)

        subcategoria_servicio = self.request.GET.get('subcategoria_servicio')
        if subcategoria_servicio is not None and subcategoria_servicio != "":
            especialistas = especialistas.filter(subcategoria_servicio_id=subcategoria_servicio)

        idioma = self.request.GET.get('idioma')
        if idioma is not None and idioma != "":
            especialistas = especialistas.filter(idioma=idioma)

        return especialistas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de especialistas'
        context['activar_especialistas'] = True
        context['path'] = [
            {'name': 'Especialistas', 'href': reverse_lazy('especialistas')}
        ]

        # Filtros
        categoria_servicio = CategoriaServicio.objects.get(id=2)
        categoria_servicio_id = categoria_servicio.id
        context['subcategorias_servicio'] = SubCategoria.objects.filter(categoria_servicio_id=categoria_servicio_id, activo=True).order_by('nombre')
        context['paises'] = Pais.objects.filter(activo=True).order_by('nombre')
        context['municipios'] = Municipio.objects.filter(activo=True).order_by('nombre')
        context['idiomas'] = Idioma.objects.filter(activo=True).order_by('nombre')

        return context


class RegistrarEspecialistaView(PermissionRequiredMixin, CreateView):
    model = Especialista
    template_name = "especialista/form_especialista.html"
    form_class = EspecialistaForm
    success_url = reverse_lazy('especialistas')
    permission = 'especialista.add_especialista'

    def get_context_data(self, **kwargs):
        context = super(RegistrarEspecialistaView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar especialista'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'especialista'
        context['icono_form'] = 'plus'
        context['activar_especialistas'] = True
        context['path'] = [
            {'name': 'Especialistas'},
            {'name': 'Especialista', 'href': reverse_lazy('especialistas')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_especialista')}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Especialista agregado con éxito.")
        return super(RegistrarEspecialistaView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Especialista no agregado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarEspecialistaView(PermissionRequiredMixin, UpdateView):
    model = Especialista
    template_name = "especialista/form_especialista.html"
    form_class = EspecialistaForm
    success_url = reverse_lazy('especialistas')
    permission = 'especialista.change_especialista'

    def get_context_data(self, **kwargs):
        context = super(ModificarEspecialistaView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar especialista'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "especialista"
        context['icono_form'] = 'edit'
        context['activar_especialistas'] = True
        context['path'] = [
            {'name': 'Especialistas'},
            {'name': 'Especialista', 'href': reverse_lazy('especialistas')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_especialista', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Especialista modificado con éxito.")
        return super(ModificarEspecialistaView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Especialista no modificado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarEspecialistaView(PermissionRequiredMixin, View):
    permission = 'especialista.delete_especialista'

    def get(self, request, *args, **kwargs):
        especialista = Especialista.objects.get(id=self.kwargs['pk'])
        especialista.delete()
        messages.add_message(request, messages.SUCCESS, "Especialista eliminado con éxito.")
        return JsonResponse({})


class HabilitarEspecialistaView(PermissionRequiredMixin, View):
    permission = 'especialista.enable_especialista'

    def get(self, request, *args, **kwargs):
        especialista = Especialista.objects.get(id=self.kwargs['pk'])
        especialista.activo = True
        especialista.save()
        messages.add_message(request, messages.SUCCESS, "Especialista habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarEspecialistaView(PermissionRequiredMixin, View):
    permission = 'especialista.disable_especialista'

    def get(self, request, *args, **kwargs):
        especialista = Especialista.objects.get(id=self.kwargs['pk'])
        especialista.activo = False
        especialista.save()
        messages.add_message(request, messages.SUCCESS, "Especialista deshabilitado con éxito.")
        return JsonResponse({})


class EliminarEspecialistasSeleccionadosView(PermissionRequiredMixin, TemplateView):
    permission = 'especialista.delete_especialistas_seleccionados'

    def get(self, request, *args, **kwargs):

        try:
            ids = request.GET.get('ids').split(',')
            Especialista.objects.filter(id__in=ids).delete()

            mensaje = "Especialistas eliminados con éxito." if ids.__len__() > 1 else "Especialista eliminado con éxito."
            messages.add_message(request, messages.SUCCESS, mensaje)

        except Exception as e:
            print(e.args)
            messages.add_message(request, messages.ERROR, "Ocurrió un error durante la operación.")

        return JsonResponse({})


class DetallesEspecialistaView(PermissionRequiredMixin, DetailView):
        template_name = 'especialista/detalles_especialista.html'
        model = Especialista
        permission = 'especialista.view_especialista'

        def get_context_data(self, **kwargs):
            context = super(DetallesEspecialistaView, self).get_context_data(**kwargs)
            context['titulo'] = 'Detalles del especialista'
            context['titulo_tabla'] = 'Detalles'
            context['activar_especialistas'] = True
            context['path'] = [
                {'name': 'Especialistas'},
                {'name': 'Especialista', 'href': reverse_lazy('especialistas')},
                {'name': 'Detalles', 'href': reverse_lazy('detalles_especialista', kwargs={'pk': self.kwargs['pk']})},
            ]
            return context


