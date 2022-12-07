# -*- coding: utf-8 -*-
import datetime
from xlsxwriter import Workbook
from django.urls import reverse
from django.http import HttpResponse
from core.utiles.permission_required import PermissionRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic.base import View
from equipo_proteccion_personal.models.factura import Factura


class ReportesFacturaView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.view_reporte_factura'

    def get(self, request, *args, **kwargs):
        fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
        error = False

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f"attachment; filename=Reporte_nominal_(Factura)({fecha_actual}).xlsx"

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
        worksheet_data.write("B1", "Número de prefactura", formato)
        worksheet_data.write("C1", "Tipo de pago", formato)
        worksheet_data.write("D1", "Cantidad pagada", formato)
        worksheet_data.write("E1", "Cantidad de equipos", formato)
        worksheet_data.write("F1", "Estado de pago", formato)
        worksheet_data.write("G1", "Fecha de pago", formato)
        worksheet_data.write("H1", "Fecha límite de pago", formato)
        worksheet_data.write("I1", "Elaborado por (nombre)", formato)
        worksheet_data.write("J1", "Elaborado por (cargo)", formato)
        worksheet_data.write("K1", "Revisado por (nombre)", formato)
        worksheet_data.write("L1", "Revisado por (cargo)", formato)
        worksheet_data.write("M1", "Entregado y registrado por (nombre)", formato)
        worksheet_data.write("N1", "Entregado y registrado por (cargo)", formato)
        worksheet_data.write("O1", "Usuario que gestionó la factura", formato)
        worksheet_data.write("P1", "Fecha de registro", formato)
        worksheet_data.write("Q1", "Fecha de actualización", formato)
        worksheet_data.write("R1", "Estado", formato)

        # Datos del proyecto
        # worksheet_data.write("U1", "", formato)

        # Ancho de las celdas:
        worksheet_data.set_column("A:A", 20)
        worksheet_data.set_column("B:B", 25)
        worksheet_data.set_column("C:C", 25)
        worksheet_data.set_column("D:D", 25)
        worksheet_data.set_column("E:E", 28)
        worksheet_data.set_column("F:F", 25)
        worksheet_data.set_column("G:G", 25)
        worksheet_data.set_column("H:H", 35)
        worksheet_data.set_column("I:I", 35)
        worksheet_data.set_column("J:J", 35)
        worksheet_data.set_column("K:K", 35)
        worksheet_data.set_column("L:L", 35)
        worksheet_data.set_column("M:M", 40)
        worksheet_data.set_column("N:N", 40)
        worksheet_data.set_column("O:O", 40)
        worksheet_data.set_column("P:P", 30)
        worksheet_data.set_column("Q:Q", 30)
        worksheet_data.set_column("R:R", 12)




    @staticmethod
    def contenido(self, worksheet_data, book):
        format_general = book.add_format({'border': 1})
        user = self.request.user
        rol = user.groups.first().name
        facturas = []

        if rol in ['Admin', 'Especialista']:
            facturas = Factura.objects.filter(activo=True)

        for index, factura in enumerate(facturas):
            worksheet_data.write(index + 1, 0, f"{factura.id}", format_general)
            worksheet_data.write(index + 1, 1, factura.numero_prefactura.numero_prefactura, format_general)
            worksheet_data.write(index + 1, 2, factura.tipo_pago, format_general)
            worksheet_data.write(index + 1, 3, f"{factura.cantidad_cup}.00" if factura.tipo_pago == "CUP" else f"{factura.cantidad_mlc}.00", format_general)
            worksheet_data.write(index + 1, 4, factura.cantidad_equipos, format_general)
            worksheet_data.write(index + 1, 5, "Pagada" if factura.estado_pago else "No pagada", format_general)
            worksheet_data.write(index + 1, 6, str(factura.fecha_pago.strftime("%Y -%m -%d") if factura.fecha_pago else '-'), format_general)
            worksheet_data.write(index + 1, 7, str(factura.fecha_limite_pago.strftime("%Y -%m -%d") if not factura.estado_pago else 'Pagada'), format_general)
            worksheet_data.write(index + 1, 8, factura.elaborado_nombre, format_general)
            worksheet_data.write(index + 1, 9, factura.elaborado_cargo, format_general)
            worksheet_data.write(index + 1, 10, factura.revisado_nombre, format_general)
            worksheet_data.write(index + 1, 11, factura.revisado_cargo, format_general)
            worksheet_data.write(index + 1, 12, factura.entregado_registrado_nombre, format_general)
            worksheet_data.write(index + 1, 13, factura.entregado_registrado_cargo, format_general)
            worksheet_data.write(index + 1, 14, factura.usuario.username, format_general)
            worksheet_data.write(index + 1, 15, str(factura.fecha_registro.strftime("%Y -%m -%d")), format_general)
            worksheet_data.write(index + 1, 16, str(factura.fecha_actualizacion.strftime("%Y -%m -%d")), format_general)
            worksheet_data.write(index + 1, 17, "Si " if factura.activo else "No", format_general)

