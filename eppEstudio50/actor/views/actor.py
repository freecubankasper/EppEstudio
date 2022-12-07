import datetime
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from actor.forms.form_actor import ActorForm
from actor.models.actor import Actor
from core.utiles.permission_required import PermissionRequiredMixin
from nomencladores.models import Municipio
from nomencladores.models.categoria_lic_conduccion import CategoriaLicenciaConduccion
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.idioma import Idioma
from nomencladores.models.pais import Pais
from nomencladores.models.sub_categoria import SubCategoria


class ListadoActoresView(PermissionRequiredMixin, ListView):
    model = Actor
    template_name = 'actor/listado_actor.html'
    paginate_by = 10
    permission = 'actor.view_actor'

    def get_queryset(self):
        actores = Actor.objects.all().order_by('id')

        ci = self.request.GET.get('ci')
        if ci is not None and ci != "":
            actores = actores.filter(ci__contains=ci)

        numero_pasaporte = self.request.GET.get('numero_pasaporte')
        if numero_pasaporte is not None and numero_pasaporte != "":
            actores = actores.filter(num_pasaporte__contains=numero_pasaporte)

        primer_nombre = self.request.GET.get('primer_nombre')
        if primer_nombre is not None and primer_nombre != "":
            actores = actores.filter(primer_nombre__icontains=primer_nombre)

        segundo_nombre = self.request.GET.get('segundo_nombre')
        if segundo_nombre is not None and segundo_nombre != "":
            actores = actores.filter(segundo_nombre__icontains=segundo_nombre)

        primer_apellido = self.request.GET.get('primer_apellido')
        if primer_apellido is not None and primer_apellido != "":
            actores = actores.filter(primer_apellido__icontains=primer_apellido)

        segundo_apellido = self.request.GET.get('segundo_apellido')
        if segundo_apellido is not None and segundo_apellido != "":
            actores = actores.filter(segundo_apellido__icontains=segundo_apellido)

        apodo = self.request.GET.get('apodo')
        if apodo is not None and apodo != "":
            actores = actores.filter(apodo__icontains=apodo)

        sexo = self.request.GET.get('sexo')
        if sexo is not None and sexo != "":
            actores = actores.filter(sexo__contains=sexo)

        fecha_nacimiento = self.request.GET.get('fecha_nacimiento')
        if fecha_nacimiento is not None and fecha_nacimiento != "":
            actores = actores.filter(fecha_nacimiento=fecha_nacimiento)

        categoria_conduccion = self.request.GET.get('categoria_conduccion')
        if categoria_conduccion is not None and categoria_conduccion != "":
            actores = actores.filter(categoria_lic_conduccion=categoria_conduccion)

        pais = self.request.GET.get('pais')
        if pais is not None and pais != "":
            actores = actores.filter(pais_id=pais)

        municipio = self.request.GET.get('municipio')
        if municipio is not None and municipio != "":
            actores = actores.filter(municipio__id=municipio)

        subcategoria_servicio = self.request.GET.get('subcategoria_servicio')
        if subcategoria_servicio is not None and subcategoria_servicio != "":
            actores = actores.filter(subcategoria_servicio_id=subcategoria_servicio)

        idioma = self.request.GET.get('idioma')
        if idioma is not None and idioma != "":
            actores = actores.filter(idioma=idioma)

        color_piel = self.request.GET.get('color_piel')
        if color_piel is not None and color_piel != "":
            actores = actores.filter(color_piel__contains=color_piel)

        color_ojos = self.request.GET.get('color_ojos')
        if color_ojos is not None and color_ojos != "":
            actores = actores.filter(color_ojos__contains=color_ojos)

        tipo_pelo = self.request.GET.get('tipo_pelo')
        if tipo_pelo is not None and tipo_pelo != "":
            actores = actores.filter(tipo_pelo__contains=tipo_pelo)

        tendencia_racial = self.request.GET.get('tendencia_racial')
        if tendencia_racial is not None and tendencia_racial != "":
            actores = actores.filter(tendencia_racial__contains=tendencia_racial)

        return actores

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de actores'
        context['activar_actores'] = True
        context['path'] = [
            {'name': 'Actores', 'href': reverse_lazy('actores')}
        ]

        # Filtros
        categoria_servicio = CategoriaServicio.objects.get(id=3)
        categoria_servicio_id = categoria_servicio.id
        context['subcategorias_servicio'] = SubCategoria.objects.filter(categoria_servicio_id=categoria_servicio_id, activo=True).order_by('nombre')
        context['paises'] = Pais.objects.filter(activo=True).order_by('nombre')
        context['municipios'] = Municipio.objects.filter(activo=True).order_by('nombre')
        context['idiomas'] = Idioma.objects.filter(activo=True).order_by('nombre')
        context['categorias_conduccion'] = CategoriaLicenciaConduccion.objects.filter(activo=True).order_by('nombre')


        return context


class RegistrarActorView(PermissionRequiredMixin, CreateView):
    model = Actor
    template_name = "actor/form_actor.html"
    form_class = ActorForm
    success_url = reverse_lazy('actores')
    permission = 'actor.add_actor'

    def get_context_data(self, **kwargs):
        context = super(RegistrarActorView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar actor'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'actor'
        context['icono_form'] = 'plus'
        context['activar_actores'] = True
        context['path'] = [
            {'name': 'Actores'},
            {'name': 'Actor', 'href': reverse_lazy('actores')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_actor')}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Actor agregado con éxito.")
        return super(RegistrarActorView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Actor no agregado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarActorView(PermissionRequiredMixin, UpdateView):
    model = Actor
    template_name = "actor/form_actor.html"
    form_class = ActorForm
    success_url = reverse_lazy('actores')
    permission = 'actor.change_actor'

    def get_context_data(self, **kwargs):
        context = super(ModificarActorView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar actor'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "actor"
        context['icono_form'] = 'edit'
        context['activar_actores'] = True
        context['path'] = [
            {'name': 'Actores'},
            {'name': 'Actor', 'href': reverse_lazy('actores')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_actor', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Actor modificado con éxito.")
        return super(ModificarActorView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Actor no modificado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarActorView(PermissionRequiredMixin, View):
    permission = 'actor.delete_actor'

    def get(self, request, *args, **kwargs):
        actor = Actor.objects.get(id=self.kwargs['pk'])
        actor.delete()
        messages.add_message(request, messages.SUCCESS, "Actor eliminado con éxito.")
        return JsonResponse({})


class HabilitarActorView(PermissionRequiredMixin, View):
    permission = 'actor.enable_actor'

    def get(self, request, *args, **kwargs):
        actor = Actor.objects.get(id=self.kwargs['pk'])
        actor.activo = True
        actor.save()
        messages.add_message(request, messages.SUCCESS, "Actor habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarActorView(PermissionRequiredMixin, View):
    permission = 'actor.disable_actor'

    def get(self, request, *args, **kwargs):
        actor = Actor.objects.get(id=self.kwargs['pk'])
        actor.activo = False
        actor.save()
        messages.add_message(request, messages.SUCCESS, "Actor deshabilitado con éxito.")
        return JsonResponse({})


class EliminarActoresSeleccionadosView(PermissionRequiredMixin, TemplateView):
    permission = 'actor.delete_actores_seleccionados'

    def get(self, request, *args, **kwargs):

        try:
            ids = request.GET.get('ids').split(',')
            Actor.objects.filter(id__in=ids).delete()

            mensaje = "Actores eliminados con éxito." if ids.__len__() > 1 else "Actor eliminado con éxito."
            messages.add_message(request, messages.SUCCESS, mensaje)

        except Exception as e:
            print(e.args)
            messages.add_message(request, messages.ERROR, "Ocurrió un error durante la operación.")

        return JsonResponse({})


class DetallesActorView(PermissionRequiredMixin, DetailView):
        template_name = 'actor/detalles_actor.html'
        model = Actor
        permission = 'actor.view_actor'

        def get_context_data(self, **kwargs):
            context = super(DetallesActorView, self).get_context_data(**kwargs)
            context['titulo'] = 'Detalles del actor'
            context['titulo_tabla'] = 'Detalles'
            context['activar_actores'] = True
            context['path'] = [
                {'name': 'Actores'},
                {'name': 'Actor', 'href': reverse_lazy('actores')},
                {'name': 'Detalles', 'href': reverse_lazy('detalles_actor', kwargs={'pk': self.kwargs['pk']})},
            ]
            return context


