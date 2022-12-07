'use strict';

var KTDatatableDataLocalDemo = function() {
    var local_data = $('#local_data'),
		organismos = local_data.data('organismos'),
		modificar_organismo = local_data.data('modificar_organismo'),
		deshabilitar_organismo = local_data.data('deshabilitar_organismo'),
		habilitar_organismo = local_data.data('habilitar_organismo');

	var demo = function() {

		var dataJSON = organismos;

		var datatable = $('.kt-datatable').KTDatatable({
			data: {
				type: 'local',
				source: dataJSON
			},

			sortable: false,

			pagination: false,

			columns: [
				{
					field: 'OrganismoId',
					title: '#',
					sortable: false,
					width: 15,
					selector: {class: 'kt-checkbox--solid'},
					textAlign: 'center'
				},
				{
					field: 'Organismo',
					title: 'Organismo'
				},
				{
					field: 'Siglas',
					title: 'Siglas',
					width: 70
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
						                         if(modificar_organismo === "True") {
													opciones += '<a href="modificar/' + row.OrganismoId + '" class="dropdown-item"><i class="la la-edit"></i> Editar</a>';
												 }
							if (row.Estado){
								 if(deshabilitar_organismo === "True") {
									 opciones += '<a href="javascript:;" class="dropdown-item"' +
										 ' onclick="mostrar_confirmacion_deshabilitar(' + row.OrganismoId + ')"' +
										 ' data-texto="el organismo seleccionado"' +
										 ' data-href="deshabilitar/' + row.OrganismoId + '"' +
										 ' id="btn_deshabilitar_' + row.OrganismoId + '">' +
										 ' <i class="la la-remove"></i> Deshabilitar' +
										 '</a>';
								 }
							} else {
								if(habilitar_organismo === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_habilitar(' + row.OrganismoId + ')"' +
										' data-texto="el organismo seleccionado"' +
										' data-href="habilitar/' + row.OrganismoId + '"' +
										' id="btn_habilitar_' + row.OrganismoId + '">' +
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