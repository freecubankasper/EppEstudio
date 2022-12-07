'use strict';

var KTDatatableDataLocalDemo = function () {
    var local_data = $('#local_data'),
        equipamientos = local_data.data('equipamientos'),
        modificar_equipamiento = local_data.data('modificar_equipamiento'),
        deshabilitar_equipamiento = local_data.data('deshabilitar_equipamiento'),
        habilitar_equipamiento = local_data.data('habilitar_equipamiento'),
        eliminar_equipamiento = local_data.data('eliminar_equipamiento'),
        detalles_equipamiento = local_data.data('detalles_equipamiento'),
        registrar_evento = local_data.data('registrar_evento'),
        listado_evento = local_data.data('listado_evento');

    var demo = function () {

        var dataJSON = equipamientos;

        var datatable = $('.kt-datatable').KTDatatable({
            data: {
                type: 'local',
                source: dataJSON
            },

            sortable: false,

            pagination: false,

            columns: [
                {
                    field: 'EquipamientoId',
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
                    field: 'Marca',
                    title: 'Marca comercial',
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
                        if (detalles_equipamiento === "True") {
                            opciones += '<a href="detalles/' + row.EquipamientoId + '" class="dropdown-item"><i class="la la-search"></i> Detalles</a>';
                        }
                        if (modificar_equipamiento === "True") {
                            opciones += '<a href="modificar/' + row.EquipamientoId + '" class="dropdown-item"><i class="la la-edit"></i> Modificar</a>';
                        }
                        if (registrar_evento === "True") {
                            opciones += '<a href="' + row.EquipamientoId + '/registrar" class="dropdown-item"><i class="la la-plus"></i> Registrar Evento</a>';
                        }
                        if (listado_evento === "True") {
                            opciones += '<a href="' + row.EquipamientoId + '/eventos" class="dropdown-item"><i class="la la-list"></i> Listado de Eventos</a>';
                        }

                        if (row.Estado) {
                            if (deshabilitar_equipamiento === "True") {
                                opciones += '<a href="javascript:;" class="dropdown-item"' +
                                    ' onclick="mostrar_confirmacion_deshabilitar(' + row.EquipamientoId + ')"' +
                                    ' data-texto="el equipamiento seleccionado"' +
                                    ' data-href="deshabilitar/' + row.EquipamientoId + '"' +
                                    ' id="btn_deshabilitar_' + row.EquipamientoId + '">' +
                                    ' <i class="la la-remove"></i> Deshabilitar' +
                                    '</a>';
                            }
                        } else {
                            if (habilitar_equipamiento === "True") {
                                opciones += '<a href="javascript:;" class="dropdown-item"' +
                                    ' onclick="mostrar_confirmacion_habilitar(' + row.EquipamientoId + ')"' +
                                    ' data-texto="el equipamiento seleccionado"' +
                                    ' data-href="habilitar/' + row.EquipamientoId + '"' +
                                    ' id="btn_habilitar_' + row.EquipamientoId + '">' +
                                    ' <i class="la la-check"></i> Habilitar' +
                                    '</a>';
                            }
                        }
                        if (eliminar_equipamiento === "True") {
                            opciones += '<a href="javascript:;" class="dropdown-item"' +
                                ' onclick="mostrar_confirmacion_eliminar(' + row.EquipamientoId + ')"' +
                                ' data-texto="el equipamiento seleccionado"' +
                                ' data-href="eliminar/' + row.EquipamientoId + '"' +
                                ' id="btn_eliminar_' + row.EquipamientoId + '">' +
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