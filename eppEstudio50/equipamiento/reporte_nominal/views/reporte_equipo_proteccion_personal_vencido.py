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


class ReportesEquipoProteccionPersonalVencidoView(PermissionRequiredMixin, View):
    permission = 'equipo_proteccion_personal.view_reporte_equipo_proteccion_personal_vencido'

    def get(self, request, *args, **kwargs):
        fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
        error = False

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f"attachment; filename=Reporte_nominal_(Equipos de Protección Personal Vencidos)({fecha_actual}).xlsx"

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
        worksheet_data.write("I1", "Entidad", formato)
        worksheet_data.write("J1", "Entidad Importadora", formato)
        worksheet_data.write("K1", "País", formato)
        worksheet_data.write("L1", "Provincia", formato)
        worksheet_data.write("M1", "Municipio", formato)
        worksheet_data.write("N1", "Organismo", formato)
        worksheet_data.write("O1", "Muestra de eqquipo", formato)
        worksheet_data.write("P1", "Certificado por otra entidad", formato)
        worksheet_data.write("Q1", "Factura", formato)
        worksheet_data.write("R1", "Tipo de pago", formato)
        worksheet_data.write("S1", "Usuario que gestionó el equipo", formato)
        worksheet_data.write("T1", "Fecha de emisión", formato)
        worksheet_data.write("U1", "Fecha de renovación", formato)
        worksheet_data.write("V1", "Estado de pago", formato)
        worksheet_data.write("W1", "Fecha de pago", formato)
        worksheet_data.write("X1", "Estado de vencimiento", formato)
        worksheet_data.write("Y1", "Fecha de vencimiento del certificado", formato)
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
        worksheet_data.set_column("I:I", 38)
        worksheet_data.set_column("J:J", 35)
        worksheet_data.set_column("K:K", 32)
        worksheet_data.set_column("L:L", 32)
        worksheet_data.set_column("M:M", 32)
        worksheet_data.set_column("N:N", 32)
        worksheet_data.set_column("O:O", 30)
        worksheet_data.set_column("P:P", 35)
        worksheet_data.set_column("Q:Q", 25)
        worksheet_data.set_column("R:R", 28)
        worksheet_data.set_column("S:S", 40)
        worksheet_data.set_column("T:T", 30)
        worksheet_data.set_column("U:U", 30)
        worksheet_data.set_column("V:V", 30)
        worksheet_data.set_column("W:W", 30)
        worksheet_data.set_column("X:X", 30)
        worksheet_data.set_column("Y:Y", 40)



    @staticmethod
    def contenido(self, worksheet_data, book):
        format_general = book.add_format({'border': 1})
        user = self.request.user
        rol = user.groups.first().name
        equipos = []

        if rol in ['Admin', 'Especialista']:
            equipos = EquipoProteccionPersonal.objects.filter(activo=False).exclude(factura__isnull=True)

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
            worksheet_data.write(index + 1, 9, equipo.entidad_importadora.nombre if equipo.entidad_importadora else '-', format_general)
            worksheet_data.write(index + 1, 10, equipo.numero_prefactura.entidad.pais.nombre, format_general)
            worksheet_data.write(index + 1, 11, equipo.numero_prefactura.entidad.municipio.provincia.nombre if equipo.numero_prefactura.entidad.municipio else '-', format_general)
            worksheet_data.write(index + 1, 12, equipo.numero_prefactura.entidad.municipio.nombre if equipo.numero_prefactura.entidad.municipio else '-', format_general)
            worksheet_data.write(index + 1, 13, equipo.numero_prefactura.entidad.organismo.nombre if equipo.numero_prefactura.entidad.organismo else '-', format_general)
            worksheet_data.write(index + 1, 14, "Si" if equipo.muestras_equipo else "No", format_general)
            worksheet_data.write(index + 1, 15, "Si" if equipo.equipo_ya_certificado else "No", format_general)
            worksheet_data.write(index + 1, 16, equipo.factura.numero_prefactura.numero_prefactura, format_general)
            worksheet_data.write(index + 1, 17, equipo.factura.tipo_pago, format_general)
            worksheet_data.write(index + 1, 18, equipo.usuario.username, format_general)
            worksheet_data.write(index + 1, 19, str(equipo.fecha_registro.strftime("%Y -%m -%d")), format_general)
            worksheet_data.write(index + 1, 20, str(equipo.fecha_renovacion.strftime("%Y -%m -%d") if equipo.fecha_renovacion else '-'), format_general)
            worksheet_data.write(index + 1, 21, "Pagado" if equipo.factura.estado_pago else "No pagado", format_general)
            worksheet_data.write(index + 1, 22, str(equipo.factura.fecha_pago.strftime("%Y -%m -%d") if equipo.factura.fecha_pago else '-'), format_general)
            worksheet_data.write(index + 1, 23, "Vigente" if equipo.activo else "Vencido", format_general)
            worksheet_data.write(index + 1, 24, str(equipo.fecha_vencimiento_certificado.strftime("%Y -%m -%d")), format_general)
