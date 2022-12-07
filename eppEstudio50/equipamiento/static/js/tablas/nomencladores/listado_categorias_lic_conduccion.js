'use strict';

var KTDatatableDataLocalDemo = function() {
    var local_data = $('#local_data'),
		categorias_lic_conduccion = local_data.data('categorias_lic_conduccion'),
		modificar_categoria_lic_conduccion = local_data.data('modificar_categoria_lic_conduccion'),
		deshabilitar_categoria_lic_conduccion = local_data.data('deshabilitar_categoria_lic_conduccion'),
		habilitar_categoria_lic_conduccion = local_data.data('habilitar_categoria_lic_conduccion');

	var demo = function() {

		var dataJSON = categorias_lic_conduccion;

		var datatable = $('.kt-datatable').KTDatatable({
			data: {
				type: 'local',
				source: dataJSON
			},

			sortable: false,

			pagination: false,

			columns: [
				{
					field: 'CategoriaLicenciaId',
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
							var opciones = '<div class="dropdown">' +
											   '<a data-toggle="dropdown" class="btn btn-sm btn-clean btn-icon btn-icon-md">' +
												   '<i class="la la-cog"></i>' +
											   '</a>' +
											   '<div class="dropdown-menu dropdown-menu-right">';
								                 if(modificar_categoria_lic_conduccion === "True") {
													opciones += '<a href="modificar/' + row.CategoriaLicenciaId + '" class="dropdown-item"><i class="la la-edit"></i> Editar</a>';
												 }
							if (row.Estado){
								if(deshabilitar_categoria_lic_conduccion === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_deshabilitar(' + row.CategoriaId + ')"' +
										' data-texto="la categoría de la licencia de conducción seleccionada "' +
										' data-href="deshabilitar/' + row.CategoriaLicenciaId + '"' +
										' id="btn_deshabilitar_' + row.CategoriaLicenciaId + '">' +
										' <i class="la la-remove"></i> Deshabilitar' +
										'</a>';
								}
							} else {
								if(habilitar_categoria_lic_conduccion === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_habilitar(' + row.CategoriaLicenciaId + ')"' +
										' data-texto="la categoría de la licencia de conducción seleccionada"' +
										' data-href="habilitar/' + row.CategoriaLicenciaId + '"' +
										' id="btn_habilitar_' + row.CategoriaLicenciaId + '">' +
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