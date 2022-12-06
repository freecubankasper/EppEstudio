# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from core.utiles.permission_required import PermissionRequiredMixin
from usuario.forms.form_groups import GroupForm


class ListadoGroupsView(PermissionRequiredMixin, ListView):
    model = Group
    template_name = 'groups/listado_groups.html'
    paginate_by = 10
    permission = 'usuario.view_group'


    def get_queryset(self):
        groups = Group.objects.all().order_by('name')

        q = self.request.GET.get('q')
        if q is not None and q != "":
            groups = groups.filter(name__icontains=q)

        return groups

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de grupos'
        context['activar_administracion'] = True
        context['path'] = [
            {'name': 'Administración'},
            {'name': 'Grupos', 'href': reverse_lazy('grupos')}
        ]
        return context


class RegistrarGroupsView(PermissionRequiredMixin, CreateView):
    model = Group
    template_name = "groups/groups_form.html"
    form_class = GroupForm
    success_url = reverse_lazy('grupos')
    permission = 'usuario.add_group'


    def get_context_data(self, **kwargs):
        context = super(RegistrarGroupsView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['titulo'] = 'Registrar grupo'
        context['titulo_tabla'] = 'Registrar'
        context['subtitulo_tabla'] = 'grupo'
        context['icono_form'] = 'plus'
        context['activar_administracion'] = True
        context['path'] = [
            {'name': 'Administración'},
            {'name': 'Grupo', 'href': reverse_lazy('grupos')},
            {'name': 'Registrar', 'href': reverse_lazy('registrar_grupo')}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Grupo agregado con éxito.")
        return super(RegistrarGroupsView, self).form_valid(form)


class ModificarGroupsView(PermissionRequiredMixin, UpdateView):
    model = Group
    template_name = "groups/groups_form.html"
    form_class = GroupForm
    success_url = reverse_lazy('grupos')
    permission = 'usuario.change_group'


    def get_context_data(self, **kwargs):
        context = super(ModificarGroupsView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar grupo'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "grupo"
        context['icono_form'] = 'edit'
        context['activar_administracion'] = True
        context['path'] = [
            {'name': 'Administración'},
            {'name': 'Grupo', 'href': reverse_lazy('grupos')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_grupo', kwargs={'pk': self.kwargs['pk']})}
        ]
        return context

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Grupo modificado con éxito.")
        return super(ModificarGroupsView, self).form_valid(form)


# class HabilitarGroupsView(PermissionRequiredMixin, View):
#     permission = 'usuario.enable_group'
#
#     def get(self, request, *args, **kwargs):
#         grupo = Group.objects.get(id=self.kwargs['pk'])
#         grupo.is_active = True
#         grupo.save()
#         messages.add_message(request, messages.SUCCESS, "Grupo habilitado con éxito.")
#         return JsonResponse({})

#
# class DeshabilitarGroupsView(PermissionRequiredMixin, View):
#     permission = 'usuario.disable_group'
#
#     def get(self, request, *args, **kwargs):
#         grupo = Group.objects.get(id=self.kwargs['pk'])
#         grupo.is_active = False
#         grupo.save()
#         messages.add_message(request, messages.SUCCESS, "Grupo deshabilitado con éxito.")
#         return JsonResponse({})
