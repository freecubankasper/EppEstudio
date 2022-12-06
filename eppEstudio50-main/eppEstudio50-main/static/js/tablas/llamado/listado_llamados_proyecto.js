'use strict';

var KTDatatableDataLocalDemo = function () {
    var local_data = $('#local_data'),
        llamados_proyecto = local_data.data('llamados_proyecto'),
        modificar_llamado_proyecto = local_data.data('modificar_llamado_proyecto'),
        deshabilitar_llamado_proyecto = local_data.data('deshabilitar_llamado_proyecto'),
        habilitar_llamado_proyecto = local_data.data('habilitar_llamado_proyecto'),
        eliminar_llamado_proyecto = local_data.data('eliminar_llamado_proyecto'),
        registrar_evento = local_data.data('registrar_evento'),
        listado_evento = local_data.data('listado_evento'),
        detalles_llamado_proyecto = local_data.data('detalles_llamado_proyecto');


    var demo = function () {

        var dataJSON = llamados_proyecto;

        var datatable = $('.kt-datatable').KTDatatable({
            data: {
                type: 'local',
                source: dataJSON
            },

            sortable: false,

            pagination: false,

            columns: [
                {
                    field: 'LlamadoProyectoId',
                    title: '#',
                    sortable: false,
                    width: 15,
                    selector: {class: 'kt-checkbox--solid'},
                    textAlign: 'center'
                },
                {
                    field: 'Titulo',
                    title: 'Título'
                },
                {
                    field: 'Proyecto',
                    title: 'Proyecto',
                },
                {
                    field: 'CentroEmergencia',
                    title: 'Centro de Emergencia',
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

                        if (modificar_llamado_proyecto === "True") {
                            opciones += '<a href="modificar/' + row.LlamadoProyectoId + '" class="dropdown-item"><i class="la la-edit"></i> Editar</a>';
                        }
                        if (detalles_llamado_proyecto === "True") {
                            opciones += '<a href="detalles/' + row.LlamadoProyectoId + '" class="dropdown-item"><i class="la la-search"></i> Detalles</a>';
                        }
                        if (registrar_evento === "True") {
                            opciones += '<a href="' + row.LlamadoProyectoId + '/registrar" class="dropdown-item"><i class="la la-plus"></i> Registrar Evento</a>';
                        }
                        if (listado_evento === "True") {
                            opciones += '<a href="' + row.LlamadoProyectoId + '/eventos" class="dropdown-item"><i class="la la-list"></i> Listado de Eventos</a>';
                        }

                        if (row.Estado) {
                            if (deshabilitar_llamado_proyecto === "True") {
                                opciones += '<a href="javascript:;" class="dropdown-item"' +
                                    ' onclick="mostrar_confirmacion_deshabilitar(' + row.LlamadoProyectoId + ')"' +
                                    ' data-texto="el llamado seleccionado"' +
                                    ' data-href="deshabilitar/' + row.LlamadoProyectoId + '"' +
                                    ' id="btn_deshabilitar_' + row.LlamadoProyectoId + '">' +
                                    ' <i class="la la-remove"></i> Deshabilitar' +
                                    '</a>';
                            }
                        } else {
                            if (habilitar_llamado_proyecto === "True") {
                                opciones += '<a href="javascript:;" class="dropdown-item"' +
                                    ' onclick="mostrar_confirmacion_habilitar(' + row.LlamadoProyectoId + ')"' +
                                    ' data-texto="el llamado seleccionado"' +
                                    ' data-href="habilitar/' + row.LlamadoProyectoId + '"' +
                                    ' id="btn_habilitar_' + row.LlamadoProyectoId + '">' +
                                    ' <i class="la la-check"></i> Habilitar' +
                                    '</a>';
                            }
                        }

                        if (eliminar_llamado_proyecto === "True") {
                            opciones += '<a href="javascript:;" class="dropdown-item"' +
                                ' onclick="mostrar_confirmacion_eliminar(' + row.LlamadoProyectoId + ')"' +
                                ' data-texto="el llamado seleccionado"' +
                                ' data-href="eliminar/' + row.LlamadoProyectoId + '"' +
                                ' id="btn_eliminar_' + row.LlamadoProyectoId + '">' +
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