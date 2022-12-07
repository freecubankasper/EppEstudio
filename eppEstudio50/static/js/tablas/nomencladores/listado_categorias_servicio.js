'use strict';

var KTDatatableDataLocalDemo = function() {
    var local_data = $('#local_data'),
		categorias_servicio = local_data.data('categorias_servicio'),
		modificar_categoria_servicio = local_data.data('modificar_categoria_servicio'),
		deshabilitar_categoria_servicio = local_data.data('deshabilitar_categoria_servicio'),
		habilitar_categoria_servicio = local_data.data('habilitar_categoria_servicio');

	var demo = function() {

		var dataJSON = categorias_servicio;

		var datatable = $('.kt-datatable').KTDatatable({
			data: {
				type: 'local',
				source: dataJSON
			},

			sortable: false,

			pagination: false,

			columns: [
				{
					field: 'CategoriaServicioId',
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
								                 if(modificar_categoria_servicio === "True") {
													opciones += '<a href="modificar/' + row.CategoriaServicioId + '" class="dropdown-item"><i class="la la-edit"></i> Editar</a>';
												 }
							if (row.Estado){
								if(deshabilitar_categoria_servicio === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_deshabilitar(' + row.CategoriaServicioId + ')"' +
										' data-texto="la categoría de servicio seleccionada "' +
										' data-href="deshabilitar/' + row.CategoriaServicioId  + '"' +
										' id="btn_deshabilitar_' + row.CategoriaServicioId  + '">' +
										' <i class="la la-remove"></i> Deshabilitar' +
										'</a>';
								}
							} else {
								if(habilitar_categoria_servicio === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_habilitar(' + row.CategoriaServicioId + ')"' +
										' data-texto="la categoría  de servicio seleccionada"' +
										' data-href="habilitar/' + row.CategoriaServicioId  + '"' +
										' id="btn_habilitar_' + row.CategoriaServicioId  + '">' +
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