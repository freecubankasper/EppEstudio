from django.urls import reverse_lazy
from django.views.generic import TemplateView

from core.utiles.permission_required import PermissionRequiredMixin


class ReportesView(PermissionRequiredMixin, TemplateView):
    template_name = 'reporte_nominal.html'
    permission = 'equipo_proteccion_personal.view_listado_reportes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de reportes'
        context['titulo'] = 'Listado de reportes'
        context['activar_menu_reportes'] = True
        context['path'] = [
            {'name': 'Listado de reportes', 'href': reverse_lazy('reportes')}
        ]

        return context