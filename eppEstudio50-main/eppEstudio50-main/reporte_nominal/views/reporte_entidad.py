# -*- coding: utf-8 -*-
import datetime
from xlsxwriter import Workbook
from django.urls import reverse
from django.http import HttpResponse
from core.utiles.permission_required import PermissionRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic.base import View

from nomencladores.models import Entidad


class ReportesEntidadView(PermissionRequiredMixin, View):
    permission = 'nomencladores.view_reporte_entidad'

    def get(self, request, *args, **kwargs):
        fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
        error = False

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f"attachment; filename=Reporte_nominal_(Entidad)({fecha_actual}).xlsx"

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

        # Datos de la entidad
        worksheet_data.write("A1", "Número de Registro", formato)
        worksheet_data.write("B1", "Código REEUP", formato)
        worksheet_data.write("C1", "Nombre de la entidad", formato)
        worksheet_data.write("D1", "País", formato)
        worksheet_data.write("E1", "Oganismo, OSDE o Gobierno", formato)
        worksheet_data.write("F1", "Municipio", formato)
        worksheet_data.write("G1", "Teléfono", formato)
        worksheet_data.write("H1", "Número de Contrato", formato)
        worksheet_data.write("I1", "Dirección", formato)
        worksheet_data.write("J1", "Dirección web", formato)
        worksheet_data.write("K1", "Correo", formato)
        worksheet_data.write("L1", "No. Lic.Comercial Cámara de Comercio", formato)
        worksheet_data.write("M1", "No. Acta de Protocolización", formato)
        worksheet_data.write("N1", "Identificación Fiscal Única", formato)
        worksheet_data.write("O1", "No. Escritura Pública Notarial", formato)
        worksheet_data.write("P1", "Nombre del representante, gerente o director", formato)
        worksheet_data.write("Q1", "Cargo del representante, gerente o director", formato)
        worksheet_data.write("R1", "Tipo entidad", formato)
        worksheet_data.write("S1", "Almacén", formato)
        worksheet_data.write("T1", "Observaciones", formato)
        worksheet_data.write("U1", "Estado", formato)
        # Datos del proyecto
        # worksheet_data.write("U1", "", formato)

        # Ancho de las celdas:
        worksheet_data.set_column("A:A", 20)
        worksheet_data.set_column("B:B", 20)
        worksheet_data.set_column("C:C", 32)
        worksheet_data.set_column("D:D", 30)
        worksheet_data.set_column("E:E", 35)
        worksheet_data.set_column("F:F", 30)
        worksheet_data.set_column("G:G", 20)
        worksheet_data.set_column("H:H", 20)
        worksheet_data.set_column("I:I", 40)
        worksheet_data.set_column("J:J", 35)
        worksheet_data.set_column("K:K", 35)
        worksheet_data.set_column("L:L", 40)
        worksheet_data.set_column("M:M", 38)
        worksheet_data.set_column("N:N", 38)
        worksheet_data.set_column("O:O", 38)
        worksheet_data.set_column("P:P", 42)
        worksheet_data.set_column("Q:Q", 40)
        worksheet_data.set_column("R:R", 25)
        worksheet_data.set_column("S:S", 12)
        worksheet_data.set_column("T:T", 40)
        worksheet_data.set_column("U:U", 12)


    @staticmethod
    def contenido(self, worksheet_data, book):
        format_general = book.add_format({'border': 1})
        user = self.request.user
        rol = user.groups.first().name
        entidades = []

        if rol in ['Admin', 'Especialista']:
            entidades = Entidad.objects.filter(activo=True)

        for index, entidad in enumerate(entidades):
            worksheet_data.write(index + 1, 0, f"{entidad.id}", format_general)
            worksheet_data.write(index + 1, 1, entidad.cod_reeup if entidad.cod_reeup else '-', format_general)
            worksheet_data.write(index + 1, 2, entidad.nombre, format_general)
            worksheet_data.write(index + 1, 3, entidad.pais.nombre, format_general)
            worksheet_data.write(index + 1, 4, entidad.organismo.nombre if entidad.organismo else '-', format_general)
            worksheet_data.write(index + 1, 5, entidad.municipio.nombre if entidad.municipio else '-', format_general)
            worksheet_data.write(index + 1, 6, entidad.telefono, format_general)
            worksheet_data.write(index + 1, 7, entidad.num_contrato if entidad.num_contrato else '-', format_general)
            worksheet_data.write(index + 1, 8, entidad.direccion, format_general)
            worksheet_data.write(index + 1, 9, entidad.direccion_web if entidad.direccion_web else '-', format_general)
            worksheet_data.write(index + 1, 10, entidad.correo, format_general)
            worksheet_data.write(index + 1, 11, entidad.num_lic_comercial_camara_comercio if entidad.num_lic_comercial_camara_comercio else '-', format_general)
            worksheet_data.write(index + 1, 12, entidad.num_acta_protocolizacion if entidad.num_acta_protocolizacion else '-', format_general)
            worksheet_data.write(index + 1, 13, entidad.identificacion_fiscal if entidad.identificacion_fiscal else '-', format_general)
            worksheet_data.write(index + 1, 14, entidad.num_escritura_publica if entidad.num_escritura_publica else '-', format_general)
            worksheet_data.write(index + 1, 15, entidad.nombre_representante, format_general)
            worksheet_data.write(index + 1, 16, entidad.cargo_representante, format_general)
            worksheet_data.write(index + 1, 17, entidad.tipo_entidad_nacional.nombre if entidad.tipo_entidad_nacional else entidad.tipo_entidad_extranjera.nombre, format_general)
            worksheet_data.write(index + 1, 18, "Si " if entidad.almacen else "No", format_general)
            worksheet_data.write(index + 1, 19, entidad.observaciones, format_general)
            worksheet_data.write(index + 1, 20, "Si " if entidad.activo else "No", format_general)