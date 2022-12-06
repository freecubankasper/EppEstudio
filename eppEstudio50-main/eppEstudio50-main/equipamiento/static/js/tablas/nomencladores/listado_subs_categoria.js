'use strict';

var KTDatatableDataLocalDemo = function() {
    var local_data = $('#local_data'),
		subs_categoria = local_data.data('subs_categoria'),
		modificar_sub_categoria = local_data.data('modificar_sub_categoria'),
		deshabilitar_sub_categoria = local_data.data('deshabilitar_sub_categoria'),
		habilitar_sub_categoria = local_data.data('habilitar_sub_categoria');

	var demo = function() {

		var dataJSON = subs_categoria;

		var datatable = $('.kt-datatable').KTDatatable({
			data: {
				type: 'local',
				source: dataJSON
			},

			sortable: false,

			pagination: false,

			columns: [
				{
					field: 'SubCategoriaId',
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
					field: 'CategoriaServicio',
					title: 'Categoría de servicio',
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
					field: 'Opciones',
					title: 'Opciones',
					width: 50,
					template: function (row) {
							var opciones = '<div class="dropdown">' +
											   '<a data-toggle="dropdown" class="btn btn-sm btn-clean btn-icon btn-icon-md">' +
												   '<i class="la la-cog"></i>' +
											   '</a>' +
											   '<div class="dropdown-menu dropdown-menu-right">';
								                 if(modificar_sub_categoria === "True") {
													opciones += '<a href="modificar/' + row.SubCategoriaId + '" class="dropdown-item"><i class="la la-edit"></i> Editar</a>';
												 }
							if (row.Estado){
								if(deshabilitar_sub_categoria === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_deshabilitar(' + row.SubCategoriaId + ')"' +
										' data-texto="la subcategoría de servicio seleccionada "' +
										' data-href="deshabilitar/' + row.SubCategoriaId + '"' +
										' id="btn_deshabilitar_' + row.SubCategoriaId + '">' +
										' <i class="la la-remove"></i> Deshabilitar' +
										'</a>';
								}
							} else {
								if(habilitar_sub_categoria === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_habilitar(' + row.SubCategoriaId + ')"' +
										' data-texto="la subcategoría de servicio seleccionada"' +
										' data-href="habilitar/' + row.SubCategoriaId + '"' +
										' id="btn_habilitar_' + row.SubCategoriaId + '">' +
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