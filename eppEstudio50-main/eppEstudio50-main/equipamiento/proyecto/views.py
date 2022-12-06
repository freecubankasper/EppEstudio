import datetime
from django.core.checks import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.template.loader import get_template
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from core.utiles.permission_required import PermissionRequiredMixin
from equipo_proteccion_personal.utiles.pdfs import to_base64
from llamado.models.llamado_proyecto import LlamadoProyecto
from nomencladores.models.categoria import Categoria
from proyecto.forms.form_proyecto import ProyectoForm
from proyecto.models import Proyecto, HistorialEstadoProyecto
from django.contrib import messages
from django.shortcuts import render
from xhtml2pdf import pisa
import os
from epp import settings



class Gestionar_proyectoView(TemplateView):
    template_name = 'gestionar_proyecto.html'
    numeros_prefactura=Categoria.objects.all()

    def get(self, request, **kwargs):
        context = super(Gestionar_proyectoView).get_context_data(**kwargs)
        context['numeros_prefactura'] = Categoria.objects.all()
        return render(request, self.template_name, context)


class Crear_proyectoView(View):

    def get(self, request, *args, **kwargs):
        categoriahtml = request.GET.get('categoria')
        categoria= Categoria.objects.get(id=categoriahtml)
        usuario = self.request.user
        nombre = request.GET.get('proyecto_nombre')
        cliente = request.GET.get('proyecto_cliente')
        equipos_prefactura = Proyecto.objects.filter(nombre=nombre, activo=True)
        if equipos_prefactura.exists():
            messages.add_message(self.request, messages.ERROR,
                                 "Existe un proyecto con ese nombre.")
            return HttpResponseRedirect(reverse_lazy('listado_proyect'))
        fecha_inicio = request.GET.get('id_fecha_inicio')
        fecha_fin = request.GET.get('id_fecha_fin')
        proyecto = Proyecto.objects.create(nombre=nombre, cliente=cliente, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin,categoria=categoria, usuario=usuario)
        idusado = str(proyecto.id)
        # return HttpResponseRedirect(reverse_lazy('calendario/'+idusado+'/eventos/'))

        return HttpResponseRedirect(reverse_lazy('calendario', kwargs={'proyecto_id': idusado}))


class ModificarProyectoView(PermissionRequiredMixin, UpdateView):
    model = Proyecto
    template_name = "proyecto_form.html"
    form_class = ProyectoForm
    success_url = reverse_lazy('listado_proyect')
    permission = 'proyecto.change_proyecto'

    def get_context_data(self, **kwargs):
        context = super(ModificarProyectoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Modificar proyecto'
        context['titulo_tabla'] = "Modificar"
        context['subtitulo_tabla'] = "proyecto"
        context['icono_form'] = 'edit'
        context['activar_proyecto'] = True
        context['path'] = [
            {'name': 'Proyectos'},
            {'name': 'Proyecto', 'href': reverse_lazy('listado_proyect')},
            {'name': 'Modificar', 'href': reverse_lazy('modificar_proyecto', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context

    def form_valid(self, form):
        proyecto = form.save(commit=False)
        proyecto.usuario = self.request.user
        proyecto.save()
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Proyecto modificado con éxito.")
        return super(ModificarProyectoView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Proyecto no modificado con éxito.")
        return render(self.request, self.template_name, self.get_context_data())


class ListadoProyectosView(ListView):
    model = Proyecto
    template_name = 'gestionar_proyecto.html'
    paginate_by = 10
    permission = 'proyecto.view_proyecto'

    def get_queryset(self):
        proyectos = Proyecto.objects.all().order_by('-id')

        nombre = self.request.GET.get('nombre')
        if nombre is not None and nombre != "":
            proyectos = proyectos.filter(nombre__icontains=nombre)

        categoria = self.request.GET.get('categoria')
        if categoria is not None and categoria != "":
            proyectos = proyectos.filter(categoria_id=categoria)

        fecha_inicio = self.request.GET.get('fecha_inicio')
        if fecha_inicio is not None and fecha_inicio != "":
            proyectos = proyectos.filter(fecha_inicio=fecha_inicio)

        fecha_fin = self.request.GET.get('fecha_fin')
        if fecha_fin is not None and fecha_fin != "":
            proyectos = proyectos.filter(fecha_fin=fecha_fin)

        return proyectos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Proyectos'
        context['activar_proyecto'] = True
        context['path'] = [
            {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')}
        ]

        # Filtros
        context['categorias'] = Categoria.objects.filter(activo=True).order_by('nombre')

        return context


class HabilitarProyectoView(View):
    permission = 'proyecto.enable_proyecto'

    def get(self, request, *args, **kwargs):
        proyecto = Proyecto.objects.get(id=self.kwargs['pk'])
        proyecto.activo = True
        proyecto.save()
        messages.add_message(request, messages.SUCCESS, "Proyecto habilitado con éxito.")
        return JsonResponse({})


class DeshabilitarProyectoView(View):
    permission = 'proyecto.disable_proyecto'

    def get(self, request, *args, **kwargs):
        proyecto = Proyecto.objects.get(id=self.kwargs['pk'])
        proyecto.activo = False
        proyecto.save()
        messages.add_message(request, messages.SUCCESS, "Proyecto deshabilitado con éxito.")
        return JsonResponse({})


class EliminarProyectoView(View):
    permission = 'proyecto.delete_proyecto'

    def get(self, request, *args, **kwargs):
        proyecto = Proyecto.objects.get(id=self.kwargs['pk'])
        proyecto.delete()
        messages.add_message(request, messages.SUCCESS, "Proyecto eliminado con éxito.")
        return JsonResponse({})


class EliminarProyectosSeleccionadosView(TemplateView):
    permission = 'proyecto.delete_proyecto_seleccionados'

    def get(self, request, *args, **kwargs):

        try:
            ids = request.GET.get('ids').split(',')
            Proyecto.objects.filter(id__in=ids).delete()

            mensaje = "Proyectos eliminados con éxito." if ids.__len__() > 1 else "Proyecto con éxito."
            messages.add_message(request, messages.SUCCESS, mensaje)

        except:
            messages.add_message(request, messages.ERROR, "Ocurrió un error durante la operación.")

        return JsonResponse({})


class DetallesProyectoView(PermissionRequiredMixin, DetailView):
    template_name = 'detalles_proyecto.html'
    model = Proyecto
    permission = 'proyecto.view_proyecto'

    def get_context_data(self, **kwargs):
        context = super(DetallesProyectoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Detalles del proyecto'
        context['titulo_tabla'] = 'Detalles'
        context['activar_proyecto'] = True
        context['historial_estados'] = HistorialEstadoProyecto.objects.filter(proyecto_id=self.kwargs["pk"])
        context['path'] = [
            {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')},
            {'name': 'Detalles', 'href': reverse_lazy('detalles_proyecto', kwargs={'pk': self.kwargs['pk']})},
        ]
        return context


class ActualizarEstadoProyectoView(PermissionRequiredMixin, TemplateView):
    template_name = "actualizar_estado_proyecto.html"
    form_class = ProyectoForm
    permission = 'proyyecto.update_estado_proyecto'

    def get(self, request, *args, **kwargs):
        context = super(ActualizarEstadoProyectoView, self).get_context_data(**kwargs)
        context['titulo'] = 'Actualizar estado del proyecto'
        context['titulo_tabla'] = 'Actualizar estado del proyecto'
        context['icono_form'] = 'refresh'
        context['activar_proyecto'] = True
        context['path'] = [
            {'name': 'Proyectos', 'href': reverse_lazy('listado_proyect')},
            {'name': 'Actualizar estado de proyecto', 'href': reverse_lazy('actualizar_estado_proyecto', kwargs={'pk': self.kwargs['pk']})},
        ]
        proyecto = Proyecto.objects.get(id=self.kwargs['pk'])
        estados = []
        if proyecto.estado_proyecto == 'Creado':
            estados = ['SolicitudRevision']
        if proyecto.estado_proyecto == 'SolicitudRevision':
            estados = ['Aprobado', 'Denegado']
        elif proyecto.estado_proyecto == 'Aprobado' or proyecto.estado_proyecto == 'Denegado':
            estados = ['Finalizado']
        context['estados'] = estados
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        proyecto = Proyecto.objects.get(id=self.kwargs['pk'])
        estado = request.POST['estado']
        monto = request.POST['proyecto_monto']
        proyecto.estado_proyecto = estado
        proyecto.fecha_estado_proyecto = datetime.datetime.now()
        proyecto.precio_aprobacion = monto
        proyecto.save()
        HistorialEstadoProyecto.objects.create(proyecto=proyecto, estado_proyecto=estado)
        messages.add_message(request, messages.SUCCESS, "Estado del proyecto actualizado con éxito.")
        return redirect(reverse("listado_proyect"))
class ActualizarCalendarioEstadoProyectoView(TemplateView):
    def post(self, request, *args, **kwargs):
        if self.request.method=='POST':
            nombre = request.POST.get('id_observaciones')

            pk=self.kwargs['pk']
            proyecto = Proyecto.objects.filter(id=pk).first()
            proyecto.observaciones_aprobacion=nombre
            proyecto.estado_proyecto='SolicitudRevision'
            proyecto.save()


            HistorialEstadoProyecto.objects.create(proyecto=proyecto, estado_proyecto=proyecto.estado_proyecto)

            return HttpResponseRedirect(reverse_lazy('proyects'))

        raise PermissionDenied


class ProyectoPDFView(PermissionRequiredMixin, View):
    permission = 'evento.export_eventosproyecto'

    def get(self, request, *args, **kwargs):
        proyecto_id = self.kwargs['proyecto_id']
        proyecto = Proyecto.objects.filter(id=proyecto_id).first()
        llamados = LlamadoProyecto.objects.filter(proyecto_id=proyecto_id)
        eventos = Proyecto.objects.filter(id=proyecto_id).order_by('id')
        template_path = 'pdfs/eventos_proyecto_pdf.html'
        if not request.user.has_perm('evento.export_eventosproyecto'):
            raise PermissionDenied
        for evento in eventos:
            title = f'Proyecto {proyecto.nombre}'
            data = {
                'title': title,
                'proyecto': proyecto,
                'llamados': llamados,
                'header': to_base64(os.path.join(settings.BASE_DIR, 'static', 'assets', 'base', 'img', 'layout', 'logos', 'logo-5negrohabana.png')),
                'PROD': settings.PRODUCTION,

            }
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{title}.pdf"'
            template = get_template(template_path)
            html = template.render(data)

            # create a pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response)

            if pisa_status.err:
                return HttpResponse('Nosotros tuvimos algunos errores <pre>' + html + '</pre>')
            return response
