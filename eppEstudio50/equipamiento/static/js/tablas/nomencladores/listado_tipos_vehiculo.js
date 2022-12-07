'use strict';

var KTDatatableDataLocalDemo = function() {
    var local_data = $('#local_data'),
		tipos_vehiculo = local_data.data('tipos_vehiculo'),
		modificar_tipo_vehiculo = local_data.data('modificar_tipo_vehiculo'),
		deshabilitar_tipo_vehiculo = local_data.data('deshabilitar_tipo_vehiculo'),
		habilitar_tipo_vehiculo = local_data.data('habilitar_tipo_vehiculo');

	var demo = function() {

		var dataJSON = tipos_vehiculo;

		var datatable = $('.kt-datatable').KTDatatable({
			data: {
				type: 'local',
				source: dataJSON
			},

			sortable: false,

			pagination: false,

			columns: [
				{
					field: 'TipoVehiculoId',
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
					field: 'Estado',
					title: 'Estado',
					width: 80,
					template: function (row) {
						if (row.Estado){
							return '<span style="width: 145px;">' +
								       '<span class="kt-badge  kt-badge--success kt-badge--inline kt-badge--pill">Habilitado</span>' +
								   '</span>';
						}
						else {
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
								                 if(modificar_tipo_vehiculo === "True") {
													opciones += '<a href="modificar/' + row.TipoVehiculoId + '" class="dropdown-item"><i class="la la-edit"></i> Editar</a>';
												 }
							if (row.Estado){
								if(deshabilitar_tipo_vehiculo === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_deshabilitar(' + row.TipoVehiculoId + ')"' +
										' data-texto="el tipo de vehículo seleccionado "' +
										' data-href="deshabilitar/' + row.TipoVehiculoId + '"' +
										' id="btn_deshabilitar_' + row.TipoVehiculoId + '">' +
										' <i class="la la-remove"></i> Deshabilitar' +
										'</a>';
								}
							} else {
								if(habilitar_tipo_vehiculo === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_habilitar(' + row.TipoVehiculoId + ')"' +
										' data-texto="el tipo de vehículo seleccionado"' +
										' data-href="habilitar/' + row.TipoVehiculoId + '"' +
										' id="btn_habilitar_' + row.TipoVehiculoId + '">' +
										' <i class="la la-check"></i> Habilitar' +
										'</a>';
								}
							}

							return opciones;
                    }
				}
			]
		});
	};

	return {
		init: function() {
			demo();
		}
	};
}();

jQuery(document).ready(function() {
	KTDatatableDataLocalDemo.init();
});