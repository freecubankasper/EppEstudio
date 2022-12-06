
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView, DeleteView
from core.utiles.permission_required import PermissionRequiredMixin
from llamado.forms.form_llamado_proyecto import LlamadoProyectoForm
from llamado.models.llamado_proyecto import LlamadoProyecto


class ListadoLlamadosProyectoView(PermissionRequiredMixin, ListView):
    model = LlamadoProyecto
    template_name = 'llamado_proyecto/listado_llamado_proyecto.html'
    permission = 'llamado.view_llamadoproyecto'

    def get_queryset(self):
        proyecto_id = self.kwargs['proyecto_id']
        llamados = LlamadoProyecto.objects.filter(proyecto_id=proyecto_id).order_by('id')
        q = self.request.GET.get('q')
        if q is not None and q != "":
            llamados = llamados.filter(titulo__icontains=q)

        return llamados

    def get_context_data(self, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Llamados'
        context['proyecto_id'] = proyecto_id
        context['activar_llamados'] = True
        context['path'] = [
            {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')},
            {'name': 'Llamados', 'href': reverse_lazy('llamados_proyecto', kwargs={'proyecto_id': self.kwargs['proyecto_id']})}
        ]

        return context


class RegistrarLlamadoProyectoView(PermissionRequiredMixin, CreateView):
    model = LlamadoProyecto
    template_name = "llamado_proyecto/llamado_proyecto_form.html"
    form_class = LlamadoProyectoForm
    permission = 'llamado.add_llamadoproyecto'

    def get_success_url(self):
        return reverse_lazy('llamados_proyecto', kwargs={'proyecto_id': self.kwargs['proyecto_id']})

    def get_context_data(self, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        context = super(RegistrarLlamadoProyectoView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar llamado'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'llamado'
        context['proyecto_id'] = proyecto_id
        context['icono_form'] = 'plus'
        context['activar_llamados'] = True
        context['path'] = [
            {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')},
            {'name': 'Llamados', 'href': reverse_lazy('llamados_proyecto', kwargs={'proyecto_id': self.kwargs['proyecto_id']})},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_llamado_proyecto', kwargs={'proyecto_id': proyecto_id})}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        llamado = form.save(commit=False)
        proyecto_id = self.kwargs['proyecto_id']
        llamado.proyecto_id = proyecto_id
        llamado.save()
        messages.add_message(self.request, messages.SUCCESS, "Llamado agregado con éxito.")
        return super(RegistrarLlamadoProyectoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Llamado no agregado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarLlamadoProyectoView(PermissionRequiredMixin, UpdateView):
    model = LlamadoProyecto
    template_name = "llamado_proyecto/llamado_proyecto_form.html"
    form_class = LlamadoProyectoForm
    permission = 'llamado.change_llamadoproyecto'

    def get_success_url(self):
        return reverse_lazy('llamados_proyecto', kwargs={'proyecto_id': self.kwargs['proyecto_id']})

    def get_context_data(self, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        pk = self.kwargs['pk']
        context = super(ModificarLlamadoProyectoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar llamado'
        context['titulo_tabla'] = "Modificar"
        context['proyecto_id'] = proyecto_id
        context['subtitulo_tabla'] = "llamado"
        context['icono_form'] = 'edit'
        context['activar_llamados'] = True
        context['path'] = [
            {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')},
            {'name': 'Llamados', 'href': reverse_lazy('llamados_proyecto', kwargs={'proyecto_id': self.kwargs['proyecto_id']})},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_llamado_proyecto', kwargs={'proyecto_id': proyecto_id, 'pk': pk})},
        ]
        return context

    def form_valid(self, form):
        llamado = form.save(commit=False)
        proyecto_id = self.kwargs['proyecto_id']
        llamado.proyecto_id = proyecto_id
        llamado.save()
        messages.add_message(self.request, messages.SUCCESS, "Llamado modificado con éxito.")
        return super(ModificarLlamadoProyectoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Llamado no modificado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarLlamadoProyectoView(PermissionRequiredMixin, DeleteView):
    permission = 'llamado.delete_llamadoproyecto'

    def get(self, request, *args, **kwargs):
        llamado = LlamadoProyecto.objects.get(id=self.kwargs['pk'])
        llamado.delete()
        messages.add_message(request, messages.SUCCESS, "Llamado eliminado con éxito.")
        return JsonResponse({})


class HabilitarLlamadoProyectoView(PermissionRequiredMixin, View):
    permission = 'llamado.enable_llamadoproyecto'

    def get(self, request, *args, **kwargs):
        llamado = LlamadoProyecto.objects.get(id=self.kwargs['pk'])
        llamado.activo = True
        llamado.save()
        messages.add_message(request, messages.SUCCESS, "Llamado habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarLlamadoProyectoView(PermissionRequiredMixin, View):
    permission = 'llamado.disable_llamadoproyecto'

    def get(self, request, *args, **kwargs):
        llamado = LlamadoProyecto.objects.get(id=self.kwargs['pk'])
        llamado.activo = False
        llamado.save()
        messages.add_message(request, messages.SUCCESS, "Llamado deshabilitado con éxito.")
        return JsonResponse({})


class EliminarLlamadosProyectoSeleccionadosView(PermissionRequiredMixin, TemplateView):
    permission = 'llamado.delete_llamadosproyecto_seleccionados'

    def get(self, request, *args, **kwargs):

        try:
            ids = request.GET.get('ids').split(',')
            LlamadoProyecto.objects.filter(id__in=ids).delete()

            mensaje = "Llamados eliminados con éxito." if ids.__len__() > 1 else "Llamado eliminado con éxito."
            messages.add_message(request, messages.SUCCESS, mensaje)

        except Exception as e:
            print(e.args)
            messages.add_message(request, messages.ERROR, "Ocurrió un error durante la operación.")

        return JsonResponse({})


class DetallesLlamadoProyectoView(PermissionRequiredMixin, DetailView):
        template_name = 'llamado_proyecto/detalles_llamado_proyecto.html'
        model = LlamadoProyecto
        permission = 'llamado.view_llamadoproyecto'

        def get_context_data(self, **kwargs):
            proyecto_id = self.kwargs['proyecto_id']
            context = super(DetallesLlamadoProyectoView, self).get_context_data(**kwargs)
            context['titulo'] = 'Detalles del llamado'
            context['proyecto_id'] = proyecto_id
            context['titulo_tabla'] = 'Detalles'
            context['activar_llamados'] = True
            context['path'] = [
                {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')},
                {'name': 'Llamados', 'href': reverse_lazy('llamados_proyecto', kwargs={'proyecto_id': self.kwargs['proyecto_id']})},
                {'name': 'Detalles', 'href': reverse_lazy('detalles_llamado_proyecto', kwargs={'proyecto_id': self.kwargs['proyecto_id'], 'pk': self.kwargs['pk']})},
            ]
            return context

