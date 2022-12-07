# -*- coding: utf-8 -*-
import datetime
from xlsxwriter import Workbook
from django.urls import reverse
from django.http import HttpResponse
from core.utiles.permission_required import PermissionRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic.base import View
from equipo_proteccion_personal.models.equipo_proteccion_personal import EquipoProteccionPersonal


class ReportesEquipoProteccionPersonalAprobadoView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.view_reporte_equipo_proteccion_personal_aprobado'

    def get(self, request, *args, **kwargs):
        fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
        error = False

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f"attachment; filename=Reporte_nominal_(Registro Nacional de Aprobaciones)({fecha_actual}).xlsx"

        book = Workbook(response, {'in_memory': True})
        worksheet_data = book.add_worksheet('Reporte Nominal')

        try:
            self.primera_fila(worksheet_data, book)
            self.contenido(self, worksheet_data, book)
            book.close()

        except Exception as e:
            error = True
            messages.add_message(request, messages.ERROR, 'Error creando excel.')
            print(f'Error creando excel: {e.args}')

        if not error:
            return response
        else:
            return redirect(reverse('reportes'))

    @staticmethod
    def primera_fila(worksheet_data, book):
        formato = book.add_format({'bold': True, 'border': 1})

        # Datos relacionados con el EPP
        worksheet_data.write("A1", "Número de Registro", formato)
        worksheet_data.write("B1", "Tipo de Aprobación", formato)
        worksheet_data.write("C1", "Parte del cuerpo que protege", formato)
        worksheet_data.write("D1", "Nombre del Equipo", formato)
        worksheet_data.write("E1", "Categoría", formato)
        worksheet_data.write("F1", "Marca comercial registrada", formato)
        worksheet_data.write("G1", "No. de referencia", formato)
        worksheet_data.write("H1", "Modelo", formato)
        worksheet_data.write("I1", "Nombre de la entidad", formato)
        worksheet_data.write("J1", "Fecha de emisión", formato)

        # Datos del proyecto
        # worksheet_data.write("U1", "", formato)

        # Ancho de las celdas:
        worksheet_data.set_column("A:A", 20)
        worksheet_data.set_column("B:B", 25)
        worksheet_data.set_column("C:C", 40)
        worksheet_data.set_column("D:D", 30)
        worksheet_data.set_column("E:E", 15)
        worksheet_data.set_column("F:F", 40)
        worksheet_data.set_column("G:G", 32)
        worksheet_data.set_column("H:H", 35)
        worksheet_data.set_column("I:I", 40)
        worksheet_data.set_column("J:J", 30)




    @staticmethod
    def contenido(self, worksheet_data, book):
        format_general = book.add_format({'border': 1})
        user = self.request.user
        rol = user.groups.first().name
        equipos = []

        if rol in ['Admin', 'Especialista']:
            equipos = EquipoProteccionPersonal.objects.filter(factura__estado_pago=True, activo=True)

        for index, equipo in enumerate(equipos):
            worksheet_data.write(index + 1, 0, f"R-{equipo.id}" if equipo.renovado else f"    {equipo.id}", format_general)
            worksheet_data.write(index + 1, 1, equipo.tipo_aprobacion.nombre, format_general)
            worksheet_data.write(index + 1, 2, ",".join(list(equipo.parte_cuerpo.values_list("nombre", flat=True))), format_general)
            worksheet_data.write(index + 1, 3, equipo.nombre, format_general)
            worksheet_data.write(index + 1, 4, equipo.categoria.nombre, format_general)
            worksheet_data.write(index + 1, 5, equipo.marca_comercial_registrada.nombre, format_general)
            worksheet_data.write(index + 1, 6, equipo.numero_referencia if equipo.numero_referencia else '-', format_general)
            worksheet_data.write(index + 1, 7, equipo.modelo if equipo.modelo else '-', format_general)
            worksheet_data.write(index + 1, 8, equipo.numero_prefactura.entidad.nombre, format_general)
            worksheet_data.write(index + 1, 9, str(equipo.fecha_registro.strftime("%Y -%m -%d")), format_general)
