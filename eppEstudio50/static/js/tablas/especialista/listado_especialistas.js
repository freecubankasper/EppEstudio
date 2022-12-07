'use strict';

var KTDatatableDataLocalDemo = function () {
    var local_data = $('#local_data'),
        especialistas = local_data.data('especialistas'),
        modificar_especialista = local_data.data('modificar_especialista'),
        deshabilitar_especialista = local_data.data('deshabilitar_especialista'),
        habilitar_especialista = local_data.data('habilitar_especialista'),
        eliminar_especialista = local_data.data('eliminar_especialista'),
        detalles_especialista = local_data.data('detalles_especialista'),
        registrar_evento = local_data.data('registrar_evento'),
        listado_evento = local_data.data('listado_evento');

    var demo = function () {

        var dataJSON = especialistas;

        var datatable = $('.kt-datatable').KTDatatable({
            data: {
                type: 'local',
                source: dataJSON
            },

            sortable: false,

            pagination: false,

            columns: [
                {
                    field: 'EspecialistaId',
                    title: '#',
                    sortable: false,
                    width: 15,
                    selector: {class: 'kt-checkbox--solid'},
                    textAlign: 'center'
                },
                {
                    field: 'NúmeroCI',
                    title: 'Número CI',
                    width: 80
                },
                {
                    field: 'PrimerNombre',
                    title: 'Primer nombre',
                    width: 70
                },
                {
                    field: 'PrimerApellido',
                    title: 'Primer apellido',
                    width: 70
                },
                {
                    field: 'Apodo',
                    title: 'Apodo',
                    width: 70
                },
                {
                    field: 'Pais',
                    title: 'País',
                    width: 70
                },
                {
                    field: 'Estado',
                    title: 'Estado',
                    width: 80,
                    template: function (row) {
                        if (row.Estado) {
                            return '<span style="width: 145px;">' +
                                '<span class="kt-badge  kt-badge--success kt-badge--inline kt-badge--pill">Habilitado</span>' +
                                '</span>';
                        } else {
                            return '<span style="width: 145px;">' +
                                '<span class="kt-badge  kt-badge--danger kt-badge--inline kt-badge--pill">Deshabilitado</span>' +
                                '</span>';
                        }
                    }
                },
                {
                    field: 'FechaRegistro',
                    title: 'Fecha de registro'
                },
                {
                    field: 'Opciones',
                    title: 'Opciones',
                    width: 50,
                    template: function (row) {
                        var opciones = '<div class="dropdown">' +
                            '<a data-toggle="dropdown" class="btn btn-sm btn-clean btn-icon btn-icon-md">' +
                            '<i class="la la-cog"></i>' +
                            '</a>' +
                            '<div class="dropdown-menu dropdown-menu-right">';
                        if (detalles_especialista === "True") {
                            opciones += '<a href="detalles/' + row.EspecialistaId + '" class="dropdown-item"><i class="la la-search"></i> Detalles</a>';
                        }
                        if (modificar_especialista === "True") {
                            opciones += '<a href="modificar/' + row.EspecialistaId + '" class="dropdown-item"><i class="la la-edit"></i> Modificar</a>';
                        }
                        if (registrar_evento === "True") {
                            opciones += '<a href="' + row.EspecialistaId + '/registrar" class="dropdown-item"><i class="la la-plus"></i> Registrar Evento</a>';
                        }
                        if (listado_evento === "True") {
                            opciones += '<a href="' + row.EspecialistaId + '/eventos" class="dropdown-item"><i class="la la-list"></i> Listado de Eventos</a>';
                        }

                        if (row.Estado) {
                            if (deshabilitar_especialista === "True") {
                                opciones += '<a href="javascript:;" class="dropdown-item"' +
                                    ' onclick="mostrar_confirmacion_deshabilitar(' + row.EspecialistaId + ')"' +
                                    ' data-texto="el especialista seleccionado"' +
                                    ' data-href="deshabilitar/' + row.EspecialistaId + '"' +
                                    ' id="btn_deshabilitar_' + row.EspecialistaId + '">' +
                                    ' <i class="la la-remove"></i> Deshabilitar' +
                                    '</a>';
                            }
                        } else {
                            if (habilitar_especialista === "True") {
                                opciones += '<a href="javascript:;" class="dropdown-item"' +
                                    ' onclick="mostrar_confirmacion_habilitar(' + row.EspecialistaId + ')"' +
                                    ' data-texto="el especialista seleccionado"' +
                                    ' data-href="habilitar/' + row.EspecialistaId + '"' +
                                    ' id="btn_habilitar_' + row.EspecialistaId + '">' +
                                    ' <i class="la la-check"></i> Habilitar' +
                                    '</a>';
                            }
                        }
                        if (eliminar_especialista === "True") {
                            opciones += '<a href="javascript:;" class="dropdown-item"' +
                                ' onclick="mostrar_confirmacion_eliminar(' + row.EspecialistaId + ')"' +
                                ' data-texto="el especialista seleccionado"' +
                                ' data-href="eliminar/' + row.EspecialistaId + '"' +
                                ' id="btn_eliminar_' + row.EspecialistaId + '">' +
                                ' <i class="la la-trash"></i> Eliminar</a>' +
                                ' </div>' +
                                '</div>';
                        }
                        return opciones;
                    }
                }
            ]
        });
    };

    return {
        init: function () {
            demo();
        }
    };
}();

jQuery(document).ready(function () {
    KTDatatableDataLocalDemo.init();
});