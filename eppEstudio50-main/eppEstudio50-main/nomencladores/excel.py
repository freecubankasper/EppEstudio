# -*- coding: utf-8 -*-
import os
import xlrd
from django.conf import settings
from nomencladores.models import Provincia, Municipio, Organismo
from nomencladores.models.categoria import Categoria
from nomencladores.models.pais import Pais
from nomencladores.models.sub_categoria import SubCategoria
from nomencladores.models.categoria_servicio import CategoriaServicio
from nomencladores.models.marca_comercial_registrada import MarcaComercialRegistrada
from equipamiento.models.equipamiento import Equipamiento
from nomencladores.models.categoria_lic_conduccion import CategoriaLicenciaConduccion
from nomencladores.models.idioma import Idioma


def load_excels():

    print('\n... CARGANDO EXCEL: Provincias.xlsx ...')
    path_excel = os.path.join(settings.BASE_DIR, 'nomencladores', 'excels', '01.Provincias.xlsx')
    excel = xlrd.open_workbook(path_excel)
    filas_excel_provincias = excel.sheet_by_index(0)._cell_values

    for index, fila in enumerate(filas_excel_provincias):
        if index > 0:
            try:
                Provincia.objects.get_or_create(
                    id=fila[0],
                    nombre=str(fila[1]).capitalize()
                )

            except Exception as ex:
                print(f"Error importando {fila[1]}. Excel Provincias.xlsx")
                print(ex.args)
                print('\n')

    print('\n... CARGANDO EXCEL: Municipios.xlsx ...')
    path_excel = os.path.join(settings.BASE_DIR, 'nomencladores', 'excels', '02.Municipios.xlsx')
    book = xlrd.open_workbook(path_excel)
    filas = book.sheet_by_index(0)._cell_values

    for index, fila in enumerate(filas):
        if index > 0:
            try:
                Municipio.objects.get_or_create(
                    id=fila[0],
                    nombre=str(fila[1]).capitalize(),
                    provincia_id=fila[2],
                    plan_turquino=fila[3]
                )

            except Exception as ex:
                print(f"Error importando {fila[1]}. Excel Municipios.xlsx")
                print(ex.args)
                print('\n')

    print('\n... CARGANDO EXCEL: Organismos.xlsx ...')
    path_excel = os.path.join(settings.BASE_DIR, 'nomencladores', 'excels', '03.Organismos.xlsx')
    book = xlrd.open_workbook(path_excel)
    filas = book.sheet_by_index(0)._cell_values

    for index, fila in enumerate(filas):
        if index > 0:
            try:
                Organismo.objects.get_or_create(
                    id=fila[0],
                    nombre=str(fila[1]).capitalize(),
                    siglas=fila[2],
                    hijode_id=fila[3]
                )

            except Exception as ex:
                print(f"Error importando {fila[1]}. Excel Organismos.xlsx")
                print(ex.args)
                print('\n')

    print('\n... CARGANDO EXCEL: Paises.xlsx ...')
    path_excel = os.path.join(settings.BASE_DIR, 'nomencladores', 'excels', '04.Paises.xlsx')
    excel = xlrd.open_workbook(path_excel)
    filas_excel_paises = excel.sheet_by_index(0)._cell_values

    for index, fila in enumerate(filas_excel_paises):
        if index > 0:
            try:
                Pais.objects.get_or_create(
                    id=fila[0],
                    nombre=str(fila[1]).capitalize(),
                    nacionalidad=fila[2],
                    siglas=fila[3]
                )

            except Exception as ex:
                print(f"Error importando {fila[1]}. Excel Paises.xlsx")
                print(ex.args)
                print('\n')

    print('\n... CARGANDO EXCEL: Categorias.xlsx ...')
    path_excel = os.path.join(settings.BASE_DIR, 'nomencladores', 'excels', '05.Categorias.xlsx')
    excel = xlrd.open_workbook(path_excel)
    filas_excel_paises = excel.sheet_by_index(0)._cell_values

    for index, fila in enumerate(filas_excel_paises):
        if index > 0:
            try:
                Categoria.objects.get_or_create(
                    id=fila[0],
                    nombre=str(fila[1]).capitalize(),
                    precio_cup=fila[2],
                    precio_mlc=fila[3]
                )

            except Exception as ex:
                print(f"Error importando {fila[1]}. Excel Categorias.xlsx")
                print(ex.args)
                print('\n')

    print('\n... CARGANDO EXCEL: categoriasservicios.xlsx ...')
    path_excel = os.path.join(settings.BASE_DIR, 'nomencladores', 'excels', 'categoriasservicios.xlsx')
    excel = xlrd.open_workbook(path_excel)
    filas_excel_paises = excel.sheet_by_index(0)._cell_values

    for index, fila in enumerate(filas_excel_paises):
        if index > 0:
            try:
                CategoriaServicio.objects.get_or_create(
                    id=fila[0],
                    nombre=str(fila[1]).capitalize(),
                )

            except Exception as ex:
                print(f"Error importando {fila[1]}. Excel categoriasservicios.xlsx")
                print(ex.args)
                print('\n')


    print('\n... CARGANDO EXCEL: tipo_talento.xlsx ...')
    path_excel = os.path.join(settings.BASE_DIR, 'nomencladores', 'excels', 'tipo_talento.xlsx')
    excel = xlrd.open_workbook(path_excel)
    filas_excel_paises = excel.sheet_by_index(0)._cell_values

    for index, fila in enumerate(filas_excel_paises):
        if index > 0:
            try:
                SubCategoria.objects.get_or_create(
                    id=fila[0],
                    nombre=str(fila[1]).capitalize(),
                    categoria_servicio_id=fila[2],
                )

            except Exception as ex:
                print(f"Error importando {fila[1]}. Excel tipo_talento.xlsx")
                print(ex.args)
                print('\n')

    print('\n... CARGANDO EXCEL: marca.xlsx ...')
    path_excel = os.path.join(settings.BASE_DIR, 'nomencladores', 'excels', 'marca.xlsx')
    excel = xlrd.open_workbook(path_excel)
    filas_excel_paises = excel.sheet_by_index(0)._cell_values

    for index, fila in enumerate(filas_excel_paises):
        if index > 0:
            try:
                MarcaComercialRegistrada.objects.get_or_create(
                    id=fila[0],
                    nombre=str(fila[1]).capitalize(),
                )

            except Exception as ex:
                print(f"Error importando {fila[1]}. Excel marca.xlsx")
                print(ex.args)
                print('\n')

    print('\n... CARGANDO EXCEL: ProductoImportok.xlsx ...')
    path_excel = os.path.join(settings.BASE_DIR, 'nomencladores', 'excels', 'ProductoImportok.xlsx')
    excel = xlrd.open_workbook(path_excel)
    filas_excel_paises = excel.sheet_by_index(0)._cell_values

    for index, fila in enumerate(filas_excel_paises):
        if index > 0:
            try:
                Equipamiento.objects.get_or_create(
                    id=fila[0],
                    nombre=str(fila[1]).capitalize(),
                    cantidad=fila[4],
                    descripcion=str(fila[5]).capitalize() + '' + str(fila[7]).capitalize(),
                    equipamiento_img=str(fila[6]).capitalize(),
                    marca_id=fila[3],
                    sub_categoria_id=int(fila[2]),

                )

            except Exception as ex:
                print(f"Error importando {fila[1]}. Excel ProductoImportok.xlsx")
                print(ex.args)
                print('\n')

    print('\n... CARGANDO EXCEL: Idiomas.xlsx ...')
    path_excel = os.path.join(settings.BASE_DIR, 'nomencladores', 'excels', '06.Idiomas.xlsx')
    excel = xlrd.open_workbook(path_excel)
    filas_excel_idiomas = excel.sheet_by_index(0)._cell_values

    for index, fila in enumerate(filas_excel_idiomas):
        if index > 0:
            try:
                Idioma.objects.get_or_create(
                    id=fila[0],
                    nombre=str(fila[1]).capitalize(),
                )

            except Exception as ex:
                print(f"Error importando {fila[1]}. Excel Idiomas.xlsx")
                print(ex.args)
                print('\n')

    print('\n... CARGANDO EXCEL: LicenciaConduccion.xlsx ...')
    path_excel = os.path.join(settings.BASE_DIR, 'nomencladores', 'excels', '07.LicenciaConduccion.xlsx')
    excel = xlrd.open_workbook(path_excel)
    filas_excel_licencias = excel.sheet_by_index(0)._cell_values

    for index, fila in enumerate(filas_excel_licencias):
        if index > 0:
            try:
                CategoriaLicenciaConduccion.objects.get_or_create(
                    id=fila[0],
                    nombre=str(fila[1]).capitalize(),
                )

            except Exception as ex:
                print(f"Error importando {fila[1]}. Excel LicenciaConduccion.xlsx")
                print(ex.args)
                print('\n')