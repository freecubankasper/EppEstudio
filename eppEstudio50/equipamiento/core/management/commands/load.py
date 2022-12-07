# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.contrib.auth.models import Permission, Group
from django.core.management import BaseCommand, call_command
from django.conf import settings
from nomencladores.excel import load_excels


class Command(BaseCommand):

    def handle(self, *args, **options):
        load_excels()

        print('... ACTUALIZANDO BD ...')
        # paths = [
        #     os.path.join(settings.BASE_DIR, 'nomencladores', 'fixtures'),
        # ]
        # for path in paths:
        #     fixtures = sorted(os.listdir(path))
            # for fixture in fixtures:
            #     print('\n... Cargando: %s ...' % fixture.split('.')[1])
            #     call_command('loaddata', fixture)
        print('\n... BD ACTUALIZADA ...')

        grupo_especialista, _ = Group.objects.get_or_create(name='Especialista')

        especialista_permissions = [
            'change_contraseña_usuario_actual',
            'change_contraseña',
            'view_user',
            'view_menu_administracion',
            'view_inicio',
            'view_equipoproteccionpersonal',
            'change_equipoproteccionpersonal',
            'delete_equipoproteccionpersonal',
            'add_equipoproteccionpersonal',
            'enable_equipo_proteccion_personal',
            'disable_equipo_proteccion_personal',
            'renew_equipo_proteccion_personal',
            'delete_equipo_proteccion_personal_seleccionados',
            'view_menu_equipo_proteccion_personal',
            'view_reporte_equipo_proteccion_personal_registrado',
            'view_listado_reportes',
            'view_menu_reporte_principal',
            'view_menu_reporte',
            'view_reporte_equipo_proteccion_personal_aprobado',
            'view_reporte_equipo_proteccion_personal_vencido',
            'export_factura',
            'export_prefactura',
            'export_certificado_epp',
            'view_documento',
            'change_documento',
            'add_documento',
            'delete_documento',
            'enable_documento',
            'disable_documento',
            'download_documento',
            'view_factura',
            'add_factura',
            'change_factura',
            'enable_factura',
            'disable_factura',
            'pagar_factura',
            'view_reporte_factura',
            'view_numeroprefactura',
            'add_numeroprefactura',
            'change_numeroprefactura',
            'enable_numero_prefactura',
            'disable_numero_prefactura',
            'view_categoria',
            'change_categoria',
            'add_categoria',
            'enable_categoria',
            'disable_categoria',
            'view_tipoentidad',
            'change_tipoentidad',
            'add_tipoentidad',
            'enable_tipo_entidad',
            'disable_tipo_entidad',
            'view_entidad',
            'add_entidad',
            'change_entidad',
            'enable_entidad',
            'disable_entidad',
            'view_menu_nomencladores',
            'view_reporte_entidad',
            'export_certificado_entidad',
            'view_marcacomercialregistrada',
            'add_marcacomercialregistrada',
            'change_marcacomercialregistrada',
            'enable_marca_comercial_registrada',
            'disable_marca_comercial_registrada',
            'view_provincia',
            'view_organismo',
            'view_municipio',
            'view_pais',
            'view_partecuerpo',
            'add_partecuerpo',
            'change_partecuerpo',
            'enable_parte_cuerpo',
            'disable_parte_cuerpo',
            'view_tipoaprobacion',
            'add_tipoaprobacion',
            'change_tipoaprobacion',
            'enable_tipo_aprobacion',
            'disable_tipo_aprobacion',
        ]

        all_permission = Permission.objects.all()

        especialista_permissions = all_permission.filter(codename__in=especialista_permissions)
        grupo_especialista.permissions.add(*especialista_permissions)


