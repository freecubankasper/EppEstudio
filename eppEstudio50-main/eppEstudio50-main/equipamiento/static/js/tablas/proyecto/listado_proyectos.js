'use strict';

var KTDatatableDataLocalDemo = function () {
    var local_data = $('#local_data'),
        proyectos = local_data.data('proyectos'),
        usuario_autenticado = local_data.data('usuario_autenticado'),
        modificar_proyecto = local_data.data('modificar_proyecto'),
        deshabilitar_proyecto = local_data.data('deshabilitar_proyecto'),
        habilitar_proyecto = local_data.data('habilitar_proyecto'),
        eliminar_proyecto = local_data.data('eliminar_proyecto'),
        registrar_llamado = local_data.data('registrar_llamado'),
        listado_llamado = local_data.data('listado_llamado'),
        actualizar_estado_proyecto = local_data.data('actualizar_estado_proyecto'),
        detalles_proyecto = local_data.data('detalles_proyecto');


    var demo = function () {

        var dataJSON = proyectos;

        var datatable = $('.kt-datatable').KTDatatable({
            data: {
                type: 'local',
                source: dataJSON
            },

            sortable: false,

            pagination: false,

            columns: [
                {
                    field: 'ProyectoId',
                    title: '#',
                    sortable: false,
                    width: 15,
                    selector: {class: 'kt-checkbox--solid'},
                    textAlign: 'center'
                },
                {
                    field: 'Nombre',
                    title: 'Nombre'
                },
                {
                    field: 'Categoria',
                    title: 'Categoría',
                    width: 70,
                },
                {
                    field: 'FechaInicio',
                    title: 'Fecha de Inicio',
                    width: 70,
                },
                {
                    field: 'FechaFin',
                    title: 'Fecha Final',
                    width: 70,
                },
                {
                    field: 'EstadoProyecto',
                    title: 'Estado del Proyecto',
                    width: 80,
                    template: function (row) {
						return '' +
						    '<span>' +
							    '<span class="kt-badge ' + get_color(row.EstadoProyecto) + ' kt-badge--inline kt-badge--pill" style="font-size: 90%;">' + row.EstadoProyecto + '</span>' +
						    '</span>';
                    }
                },
                {
                    field: 'Estado',
                    title: ' Estado de Habilitación',
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

                        if (usuario_autenticado === "True" && modificar_proyecto === "True") {
                            opciones += '<a href="modificar/' + row.ProyectoId + '" class="dropdown-item"><i class="la la-edit"></i> Editar</a>';
                        }
                        if (usuario_autenticado === "True" && detalles_proyecto === "True") {
                            opciones += '<a href="detalles/' + row.ProyectoId + '" class="dropdown-item"><i class="la la-search"></i> Detalles</a>';
                        }
                        if (usuario_autenticado === "True" && registrar_llamado === "True") {
                            opciones += '<a href="' + row.ProyectoId + '/registrar" class="dropdown-item"><i class="la la-plus"></i> Registrar Llamado</a>';
                        }
                        if (usuario_autenticado === "True" && listado_llamado === "True") {
                            opciones += '<a href="' + row.ProyectoId + '/llamados" class="dropdown-item"><i class="la la-list"></i> Listado de Llamados</a>';
                        }
                        if (usuario_autenticado === "True" && row.EstadoProyecto!=="Finalizado" && actualizar_estado_proyecto === "True"){
							            	opciones += '<a href="actualizar_estado_proyecto/' + row.ProyectoId + '" class="dropdown-item"><i class="la la-refresh"></i> Actualizar estado de proyecto</a>';

										}

                        if (row.Estado) {
                            if (usuario_autenticado === "True" && deshabilitar_proyecto === "True") {
                                opciones += '<a href="javascript:;" class="dropdown-item"' +
                                    ' onclick="mostrar_confirmacion_deshabilitar(' + row.ProyectoId + ')"' +
                                    ' data-texto="el proyecto seleccionado"' +
                                    ' data-href="deshabilitar/' + row.ProyectoId + '"' +
                                    ' id="btn_deshabilitar_' + row.ProyectoId + '">' +
                                    ' <i class="la la-remove"></i> Deshabilitar' +
                                    '</a>';
                            }
                        } else {
                            if (usuario_autenticado === "True" && habilitar_proyecto === "True") {
                                opciones += '<a href="javascript:;" class="dropdown-item"' +
                                    ' onclick="mostrar_confirmacion_habilitar(' + row.ProyectoId + ')"' +
                                    ' data-texto="el proyecto seleccionado"' +
                                    ' data-href="habilitar/' + row.ProyectoId + '"' +
                                    ' id="btn_habilitar_' + row.ProyectoId + '">' +
                                    ' <i class="la la-check"></i> Habilitar' +
                                    '</a>';
                            }
                        }

                        if (usuario_autenticado === "True" && eliminar_proyecto === "True") {
                            opciones += '<a href="javascript:;" class="dropdown-item"' +
                                ' onclick="mostrar_confirmacion_eliminar(' + row.ProyectoId + ')"' +
                                ' data-texto="el proyecto seleccionado"' +
                                ' data-href="eliminar/' + row.ProyectoId + '"' +
                                ' id="btn_eliminar_' + row.ProyectoId + '">' +
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

function get_color(value) {

	if (value === 'Creado'){
		return 'kt-badge--warning';
	} else if (value === 'Aprobado') {
		return 'kt-badge--success';
	} else if (value === 'Denegado'){
		return 'kt-badge--danger';
	} else if (value === 'Finalizado'){
		return 'kt-badge--primary';
	}
}

jQuery(document).ready(function () {
    KTDatatableDataLocalDemo.init();
});