'use strict';

var KTDatatableDataLocalDemo = function() {
    var local_data = $('#local_data'),
		municipios = local_data.data('municipios'),
		modificar_municipio = local_data.data('modificar_municipio'),
		deshabilitar_municipio = local_data.data('deshabilitar_municipio'),
		habilitar_municipio = local_data.data('habilitar_municipio');

	var demo = function() {

		var dataJSON = municipios;

		var datatable = $('.kt-datatable').KTDatatable({
			data: {
				type: 'local',
				source: dataJSON
			},

			sortable: false,

			pagination: false,

			columns: [
				{
					field: 'MunicipioId',
					title: '#',
					sortable: false,
					width: 15,
					selector: {class: 'kt-checkbox--solid'},
					textAlign: 'center'
				},
				{
					field: 'Municipio',
					title: 'Municipio'
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
						                         if(modificar_municipio === "True") {
													opciones += '<a href="modificar/' + row.MunicipioId + '" class="dropdown-item"><i class="la la-edit"></i> Editar</a>';
												 }
							if (row.Estado){
								if(deshabilitar_municipio === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_deshabilitar(' + row.MunicipioId + ')"' +
										' data-texto="el municipio seleccionado"' +
										' data-href="deshabilitar/' + row.MunicipioId + '"' +
										' id="btn_deshabilitar_' + row.MunicipioId + '">' +
										' <i class="la la-remove"></i> Deshabilitar' +
										'</a>';
								}
							} else {
								if(habilitar_municipio === "True") {
								    opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_habilitar(' + row.MunicipioId + ')"' +
										' data-texto="el municipio seleccionado"' +
										' data-href="habilitar/' + row.MunicipioId + '"' +
										' id="btn_habilitar_' + row.MunicipioId +'">' +
										' <i class="la la-check"></i> Habilitar' +
										'</a>';
							}   }

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