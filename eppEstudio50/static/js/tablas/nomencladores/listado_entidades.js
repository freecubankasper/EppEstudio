'use strict';

let KTDatatableDataLocalDemo = function() {
    let local_data = $('#local_data'),
		entidades = local_data.data('entidades'),
		modificar_entidad = local_data.data('modificar_entidad'),
		deshabilitar_entidad = local_data.data('deshabilitar_entidad'),
		habilitar_entidad = local_data.data('habilitar_entidad'),
		detalles_entidad = local_data.data('detalles_entidad'),
		exportar_certificado_entidad = local_data.data('exportar_certificado_entidad');

	let demo = function() {

		let dataJSON = entidades;

		let datatable = $('.kt-datatable').KTDatatable({
			data: {
				type: 'local',
				source: dataJSON
			},

			sortable: false,

			pagination: false,

			columns: [
				{
					field: 'EntidadId',
					title: '#',
					sortable: false,
					width: 15,
					selector: {class: 'kt-checkbox--solid'},
					textAlign: 'center'
				},
				{
					field: 'Entidad',
					title: 'Entidad'
				},
				{
					field: 'TipoEntidad',
					title: 'Tipo de entidad'
				},
				{
					field: 'Pais',
					title: 'País'
				},
				{
					field: 'Estado',
					title: 'Estado',
					width: 80,
					template: function (row) {
						if (row.Estado){
							return '<span style="width: 145px;">' +
								       '<span class="kt-badge  kt-badge--success kt-badge--inline kt-badge--pill">Habilitada</span>' +
								   '</span>';
						}
						else {
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
					field: 'Opciones',
					title: 'Opciones',
					width: 50,
					template: function (row) {
							let opciones = '<div class="dropdown">' +
											   '<a data-toggle="dropdown" class="btn btn-sm btn-clean btn-icon btn-icon-md">' +
												   '<i class="la la-cog"></i>' +
											   '</a>' +
											   '<div class="dropdown-menu dropdown-menu-right">';
								                  if(detalles_entidad === "True") {
								                  	opciones += '<a href="detalles/' + row.EntidadId + '" class="dropdown-item"><i class="la la-search"></i> Detalles</a>';
												  }
						                         if(modificar_entidad === "True") {
													opciones += '<a href="modificar/' + row.EntidadId + '" class="dropdown-item"><i class="la la-edit"></i> Editar</a>';
												 }
						                         if(exportar_certificado_entidad === "True") {
													opciones += '<a href="certificado_entidad/' + row.EntidadId + '" class="dropdown-item"><i class="la la-file-pdf-o"></i> Exportar certificado de la entidad</a>';
												 }
							if (row.Estado){
								if(deshabilitar_entidad === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_deshabilitar(' + row.EntidadId + ')"' +
										' data-texto="la entidad seleccionada"' +
										' data-href="deshabilitar/' + row.EntidadId + '"' +
										' id="btn_deshabilitar_' + row.EntidadId + '">' +
										' <i class="la la-remove"></i> Deshabilitar' +
										'</a>';
								}
							} else {
								if(habilitar_entidad === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_habilitar(' + row.EntidadId + ')"' +
										' data-texto="la entidad seleccionada"' +
										' data-href="habilitar/' + row.EntidadId + '"' +
										' id="btn_habilitar_' + row.EntidadId + '">' +
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