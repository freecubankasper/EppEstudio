'use strict';

var KTDatatableDataLocalDemo = function () {
    var local_data = $('#local_data'),
        locaciones = local_data.data('locaciones'),
        modificar_locacion = local_data.data('modificar_locacion'),
        deshabilitar_locacion = local_data.data('deshabilitar_locacion'),
        habilitar_locacion = local_data.data('habilitar_locacion'),
        eliminar_locacion = local_data.data('eliminar_locacion'),
        detalles_locacion = local_data.data('detalles_locacion'),
        registrar_evento = local_data.data('registrar_evento'),
        listado_evento = local_data.data('listado_evento');

    var demo = function () {

        var dataJSON = locaciones;

        var datatable = $('.kt-datatable').KTDatatable({
            data: {
                type: 'local',
                source: dataJSON
            },

            sortable: false,

            pagination: false,

            columns: [
                {
                    field: 'LocacionId',
                    title: '#',
                    sortable: false,
                    width: 15,
                    selector: {class: 'kt-checkbox--solid'},
                    textAlign: 'center'
                },
                {
                    field: 'Nombre',
                    title: 'Nombre',
                },
                {
                    field: 'SubcategoriaServicio',
                    title: 'Subcategoría de servicio',
                },
                {
                    field: 'Municipio',
                    title: 'Municipio',
                    width: 70
                },
                {
                    field: 'Estado',
                    title: 'Estado',
                    width: 80,
                    template: function (row) {
                        if (row.Estado) {
                            return '<span style="width: 145px;">' +
                                '<span class="kt-badge  kt-badge--success kt-badge--inline kt-badge--pill">Habilitada</span>' +
                                '</span>';
                        } else {
                            return '<span style="width: 145px;">' +
                                '<span class="kt-badge  kt-badge--danger kt-badge--inline kt-badge--pill">Deshabilitada</span>' +
                                '</span>';
                        }
                    }
                },
                {
                    field: 'FechaRegistro',
                    title: 'Fecha de registro'
                },
                {
                    field: 'FechaActualizacion',
                    title: 'Fecha de actualización'
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
                        if (detalles_locacion === "True") {
                            opciones += '<a href="detalles/' + row.LocacionId + '" class="dropdown-item"><i class="la la-search"></i> Detalles</a>';
                        }
                        if (modificar_locacion === "True") {
                            opciones += '<a href="modificar/' + row.LocacionId + '" class="dropdown-item"><i class="la la-edit"></i> Modificar</a>';
                        }
                        if (registrar_evento === "True") {
                            opciones += '<a href="' + row.LocacionId + '/registrar" class="dropdown-item"><i class="la la-plus"></i> Registrar Evento</a>';
                        }
                        if (listado_evento === "True") {
                            opciones += '<a href="' + row.LocacionId + '/eventos" class="dropdown-item"><i class="la la-list"></i> Listado de Eventos</a>';
                        }

                        if (row.Estado) {
                            if (deshabilitar_locacion === "True") {
                                opciones += '<a href="javascript:;" class="dropdown-item"' +
                                    ' onclick="mostrar_confirmacion_deshabilitar(' + row.LocacionId + ')"' +
                                    ' data-texto="la locación seleccionada"' +
                                    ' data-href="deshabilitar/' + row.LocacionId + '"' +
                                    ' id="btn_deshabilitar_' + row.LocacionId + '">' +
                                    ' <i class="la la-remove"></i> Deshabilitar' +
                                    '</a>';
                            }
                        } else {
                            if (habilitar_locacion === "True") {
                                opciones += '<a href="javascript:;" class="dropdown-item"' +
                                    ' onclick="mostrar_confirmacion_habilitar(' + row.LocacionId + ')"' +
                                    ' data-texto="la locación seleccionada"' +
                                    ' data-href="habilitar/' + row.LocacionId + '"' +
                                    ' id="btn_habilitar_' + row.LocacionId + '">' +
                                    ' <i class="la la-check"></i> Habilitar' +
                                    '</a>';
                            }
                        }
                        if (eliminar_locacion === "True") {
                            opciones += '<a href="javascript:;" class="dropdown-item"' +
                                ' onclick="mostrar_confirmacion_eliminar(' + row.LocacionId + ')"' +
                                ' data-texto="la locación seleccionada"' +
                                ' data-href="eliminar/' + row.LocacionId + '"' +
                                ' id="btn_eliminar_' + row.LocacionId + '">' +
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