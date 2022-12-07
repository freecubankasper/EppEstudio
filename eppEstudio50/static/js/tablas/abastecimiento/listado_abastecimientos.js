'use strict';

var KTDatatableDataLocalDemo = function () {
    var local_data = $('#local_data'),
        abastecimientos = local_data.data('abastecimientos'),
        modificar_abastecimiento = local_data.data('modificar_abastecimiento'),
        deshabilitar_abastecimiento = local_data.data('deshabilitar_abastecimiento'),
        habilitar_abastecimiento = local_data.data('habilitar_abastecimiento'),
        eliminar_abastecimiento = local_data.data('eliminar_abastecimiento'),
        detalles_abastecimiento = local_data.data('detalles_abastecimiento'),
        registrar_evento = local_data.data('registrar_evento'),
        listado_evento = local_data.data('listado_evento');

    var demo = function () {

        var dataJSON = abastecimientos;

        var datatable = $('.kt-datatable').KTDatatable({
            data: {
                type: 'local',
                source: dataJSON
            },

            sortable: false,

            pagination: false,

            columns: [
                {
                    field: 'AbastecimientoId',
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
                    field: 'NombreProducto',
                    title: 'Nombre del producto',
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
                        if (detalles_abastecimiento === "True") {
                            opciones += '<a href="detalles/' + row.AbastecimientoId + '" class="dropdown-item"><i class="la la-search"></i> Detalles</a>';
                        }
                        if (modificar_abastecimiento === "True") {
                            opciones += '<a href="modificar/' + row.AbastecimientoId + '" class="dropdown-item"><i class="la la-edit"></i> Modificar</a>';
                        }
                        if (registrar_evento === "True") {
                            opciones += '<a href="' + row.AbastecimientoId + '/registrar" class="dropdown-item"><i class="la la-plus"></i> Registrar Evento</a>';
                        }
                        if (listado_evento === "True") {
                            opciones += '<a href="' + row.AbastecimientoId + '/eventos" class="dropdown-item"><i class="la la-list"></i> Listado de Eventos</a>';
                        }

                        if (row.Estado) {
                            if (deshabilitar_abastecimiento === "True") {
                                opciones += '<a href="javascript:;" class="dropdown-item"' +
                                    ' onclick="mostrar_confirmacion_deshabilitar(' + row.AbastecimientoId + ')"' +
                                    ' data-texto="el abastecimiento seleccionado"' +
                                    ' data-href="deshabilitar/' + row.AbastecimientoId + '"' +
                                    ' id="btn_deshabilitar_' + row.AbastecimientoId + '">' +
                                    ' <i class="la la-remove"></i> Deshabilitar' +
                                    '</a>';
                            }
                        } else {
                            if (habilitar_abastecimiento === "True") {
                                opciones += '<a href="javascript:;" class="dropdown-item"' +
                                    ' onclick="mostrar_confirmacion_habilitar(' + row.AbastecimientoId + ')"' +
                                    ' data-texto="el abastecimiento seleccionado"' +
                                    ' data-href="habilitar/' + row.AbastecimientoId + '"' +
                                    ' id="btn_habilitar_' + row.AbastecimientoId + '">' +
                                    ' <i class="la la-check"></i> Habilitar' +
                                    '</a>';
                            }
                        }
                        if (eliminar_abastecimiento === "True") {
                            opciones += '<a href="javascript:;" class="dropdown-item"' +
                                ' onclick="mostrar_confirmacion_eliminar(' + row.AbastecimientoId + ')"' +
                                ' data-texto="el abastecimiento seleccionado"' +
                                ' data-href="eliminar/' + row.AbastecimientoId + '"' +
                                ' id="btn_eliminar_' + row.AbastecimientoId + '">' +
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