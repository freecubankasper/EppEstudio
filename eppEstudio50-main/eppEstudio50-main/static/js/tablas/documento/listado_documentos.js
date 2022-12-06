'use strict';

var KTDatatableDataLocalDemo = function() {
    var local_data = $('#local_data'),
		documentos = local_data.data('documentos'),
		modificar_documento = local_data.data('modificar_documento'),
		deshabilitar_documento = local_data.data('deshabilitar_documento'),
		habilitar_documento = local_data.data('habilitar_documento'),
		eliminar_documento = local_data.data('eliminar_documento');

	var demo = function() {

		var dataJSON = documentos;

		var datatable = $('.kt-datatable').KTDatatable({
			data: {
				type: 'local',
				source: dataJSON
			},

			sortable: false,

			pagination: false,

			columns: [
				{
					field: 'DocumentoId',
					title: '#',
					sortable: false,
					textAlign: 'center'
				},
				{
					field: 'Nombre',
					title: 'Nombre',
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
								               if(modificar_documento === "True") {
								               	 opciones += '<a href="modificar/' + row.DocumentoId + '" class="dropdown-item"><i class="la la-edit"></i> Modificar</a>';
											   }

							if (row.Estado){
								if(deshabilitar_documento === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_deshabilitar(' + row.DocumentoId + ')"' +
										' data-texto="el documento seleccionado"' +
										' data-href="deshabilitar/' + row.DocumentoId + '"' +
										' id="btn_deshabilitar_' + row.DocumentoId + '">' +
										' <i class="la la-remove"></i> Deshabilitar' +
										'</a>';
								}
							} else {
								if(habilitar_documento === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_habilitar(' + row.DocumentoId + ')"' +
										' data-texto="el documento seleccionado"' +
										' data-href="habilitar/' + row.DocumentoId + '"' +
										' id="btn_habilitar_' + row.DocumentoId + '">' +
										' <i class="la la-check"></i> Habilitar' +
										'</a>';
								}
							}
                        if(eliminar_documento === "True") {
							opciones += '<a href="javascript:;" class="dropdown-item"' +
								' onclick="mostrar_confirmacion_eliminar(' + row.DocumentoId + ')"' +
								' data-texto="el documento seleccionado"' +
								' data-href="eliminar/' + row.DocumentoId + '"' +
								' id="btn_eliminar_' + row.DocumentoId + '">' +
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
		init: function() {
			demo();
		}
	};
}();

jQuery(document).ready(function() {
	KTDatatableDataLocalDemo.init();
});