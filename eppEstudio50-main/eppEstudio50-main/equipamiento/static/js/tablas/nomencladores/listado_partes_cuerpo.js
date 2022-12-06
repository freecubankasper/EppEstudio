'use strict';

var KTDatatableDataLocalDemo = function() {
    var local_data = $('#local_data'),
		partes_cuerpo = local_data.data('partes_cuerpo'),
		modificar_parte_cuerpo = local_data.data('modificar_parte_cuerpo'),
		deshabilitar_parte_cuerpo = local_data.data('deshabilitar_parte_cuerpo'),
		habilitar_parte_cuerpo = local_data.data('habilitar_parte_cuerpo');

	var demo = function() {

		var dataJSON = partes_cuerpo;

		var datatable = $('.kt-datatable').KTDatatable({
			data: {
				type: 'local',
				source: dataJSON
			},

			sortable: false,

			pagination: false,

			columns: [
				{
					field: 'ParteCuerpoId',
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
								                 if(modificar_parte_cuerpo === "True") {
													opciones += '<a href="modificar/' + row.ParteCuerpoId + '" class="dropdown-item"><i class="la la-edit"></i> Editar</a>';
												 }
							if (row.Estado){
								if(deshabilitar_parte_cuerpo === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_deshabilitar(' + row.ParteCuerpoId + ')"' +
										' data-texto="la parte del cuerpo seleccionada "' +
										' data-href="deshabilitar/' + row.ParteCuerpoId + '"' +
										' id="btn_deshabilitar_' + row.ParteCuerpoId + '">' +
										' <i class="la la-remove"></i> Deshabilitar' +
										'</a>';
								}
							} else {
								if(habilitar_parte_cuerpo === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_habilitar(' + row.ParteCuerpoId + ')"' +
										' data-texto="la parte del cuerpo seleccionada"' +
										' data-href="habilitar/' + row.ParteCuerpoId + '"' +
										' id="btn_habilitar_' + row.ParteCuerpoId + '">' +
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