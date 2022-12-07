import datetime
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView, DeleteView
from core.utiles.permission_required import PermissionRequiredMixin
from evento.forms.form_evento import EventoForm
from evento.models.evento import Evento


class ListadoEventosView(PermissionRequiredMixin, ListView):
    model = Evento
    template_name = 'evento/listado_evento.html'
    permission = 'evento.view_evento'

    def get_queryset(self):
        proyecto_id = self.kwargs['proyecto_id']
        eventos = Evento.objects.filter(proyecto_id=proyecto_id).order_by('id')

        return eventos

    def get_context_data(self, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eventos'
        context['proyecto_id'] = proyecto_id
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos', kwargs={'proyecto_id': self.kwargs['proyecto_id']})}
        ]

        return context


class RegistrarEventoView(PermissionRequiredMixin, CreateView):
    model = Evento
    template_name = "evento/form_evento.html"
    form_class = EventoForm
    permission = 'evento.add_evento'

    def get_success_url(self):
        return reverse_lazy('eventos', kwargs={'proyecto_id': self.kwargs['proyecto_id']})

    def get_context_data(self, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        context = super(RegistrarEventoView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar evento'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'evento'
        context['proyecto_id'] = proyecto_id
        context['icono_form'] = 'plus'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos', kwargs={'proyecto_id': self.kwargs['proyecto_id']})},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_evento', kwargs={'proyecto_id': proyecto_id})}
        ]
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print(form.errors)
    #     if form.is_valid():
    #         return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        evento = form.save(commit=False)
        proyecto_id = self.kwargs['proyecto_id']
        evento.proyecto_id = proyecto_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento agregado con éxito.")
        return super(RegistrarEventoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no agregado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class ModificarEventoView(PermissionRequiredMixin, UpdateView):
    model = Evento
    template_name = "evento/form_evento.html"
    form_class = EventoForm
    permission = 'evento.change_evento'

    def get_success_url(self):
        return reverse_lazy('eventos', kwargs={'proyecto_id': self.kwargs['proyecto_id']})

    def get_context_data(self, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        pk = self.kwargs['pk']
        context = super(ModificarEventoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar evento'
        context['titulo_tabla'] = "Modificar"
        context['proyecto_id'] = proyecto_id
        context['subtitulo_tabla'] = "evento"
        context['icono_form'] = 'edit'
        context['activar_eventos'] = True
        context['path'] = [
            {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')},
            {'name': 'Eventos', 'href': reverse_lazy('eventos', kwargs={'proyecto_id': self.kwargs['proyecto_id']})},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_evento', kwargs={'proyecto_id': proyecto_id, 'pk': pk})},
        ]
        return context

    def form_valid(self, form):
        evento = form.save(commit=False)
        proyecto_id = self.kwargs['proyecto_id']
        evento.proyecto_id = proyecto_id
        evento.save()
        messages.add_message(self.request, messages.SUCCESS, "Evento modificado con éxito.")
        return super(ModificarEventoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Evento no modificado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class EliminarEventoView(PermissionRequiredMixin, DeleteView):
    permission = 'evento.delete_evento'

    def get(self, request, *args, **kwargs):
        evento = Evento.objects.get(id=self.kwargs['pk'])
        evento.delete()
        messages.add_message(request, messages.SUCCESS, "Evento eliminado con éxito.")
        return JsonResponse({})


class HabilitarEventoView(PermissionRequiredMixin, View):
    permission = 'evento.enable_evento'

    def get(self, request, *args, **kwargs):
        evento = Evento.objects.get(id=self.kwargs['pk'])
        evento.activo = True
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarEventoView(PermissionRequiredMixin, View):
    permission = 'evento.disable_evento'

    def get(self, request, *args, **kwargs):
        evento = Evento.objects.get(id=self.kwargs['pk'])
        evento.activo = False
        evento.save()
        messages.add_message(request, messages.SUCCESS, "Evento deshabilitado con éxito.")
        return JsonResponse({})


class DetallesEventoView(PermissionRequiredMixin, DetailView):
        template_name = 'evento/detalles_evento.html'
        model = Evento
        permission = 'evento.view_evento'

        def get_context_data(self, **kwargs):
            proyecto_id = self.kwargs['proyecto_id']
            context = super(DetallesEventoView, self).get_context_data(**kwargs)
            context['titulo'] = 'Detalles del evento'
            context['proyecto_id'] = proyecto_id
            context['titulo_tabla'] = 'Detalles'
            context['activar_eventos'] = True
            context['path'] = [
                {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')},
                {'name': 'Eventos', 'href': reverse_lazy('eventos', kwargs={'proyecto_id': self.kwargs['proyecto_id']})},
                {'name': 'Detalles', 'href': reverse_lazy('detalles_evento', kwargs={'proyecto_id': self.kwargs['proyecto_id'], 'pk': self.kwargs['pk']})},
            ]
            return context

