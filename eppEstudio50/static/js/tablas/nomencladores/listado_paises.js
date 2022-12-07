'use strict';

var KTDatatableDataLocalDemo = function() {
    var local_data = $('#local_data'),
		paises = local_data.data('paises'),
		modificar_pais = local_data.data('modificar_pais'),
		deshabilitar_pais = local_data.data('deshabilitar_pais'),
		habilitar_pais = local_data.data('habilitar_pais');

	var demo = function() {

		var dataJSON = paises;

		var datatable = $('.kt-datatable').KTDatatable({
			data: {
				type: 'local',
				source: dataJSON
			},

			sortable: false,

			pagination: false,

			columns: [
				{
					field: 'PaisId',
					title: '#',
					sortable: false,
					width: 15,
					selector: {class: 'kt-checkbox--solid'},
					textAlign: 'center'
				},
				{
					field: 'Pais',
					title: 'País'
				},
				{
					field: 'Nacionalidad',
					title: 'Nacionalidad'
				},
				{
					field: 'Siglas',
					title: 'Siglas'
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
								                 if(modificar_pais === "True") {
													opciones += '<a href="modificar/' + row.PaisId + '" class="dropdown-item"><i class="la la-edit"></i> Editar</a>';
												 }
							if (row.Estado){
								if(deshabilitar_pais === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_deshabilitar(' + row.PaisId + ')"' +
										' data-texto="el país seleccionado "' +
										' data-href="deshabilitar/' + row.PaisId + '"' +
										' id="btn_deshabilitar_' + row.PaisId + '">' +
										' <i class="la la-remove"></i> Deshabilitar' +
										'</a>';
								}
							} else {
								if(habilitar_pais === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_habilitar(' + row.PaisId + ')"' +
										' data-texto="el país seleccionado"' +
										' data-href="habilitar/' + row.PaisId + '"' +
										' id="btn_habilitar_' + row.PaisId + '">' +
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