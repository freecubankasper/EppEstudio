'use strict';

var KTDatatableDataLocalDemo = function() {
    var local_data = $('#local_data'),
		articulos = local_data.data('articulos'),
		modificar_articulo = local_data.data('modificar_articulo'),
		deshabilitar_articulo = local_data.data('deshabilitar_articulo'),
		habilitar_articulo = local_data.data('habilitar_articulo'),
		eliminar_articulo = local_data.data('eliminar_articulo'),
		detalles_articulo = local_data.data('detalles_articulo');

	var demo = function() {

		var dataJSON = articulos;

		var datatable = $('.kt-datatable').KTDatatable({
			data: {
				type: 'local',
				source: dataJSON
			},

			sortable: false,

			pagination: false,

			columns: [
				{
					field: 'ArticuloId',
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
					field: 'TipoArticulo',
					title: 'Tipo de artículo',
				},
				{
					field: 'Marca',
					title: 'Marca comercial',
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
							                   if(detalles_articulo === "True") {
								               	 opciones += '<a href="detalles/' + row.ArticuloId + '" class="dropdown-item"><i class="la la-search"></i> Detalles</a>';
											   }
								               if(modificar_articulo === "True") {
								               	 opciones += '<a href="modificar/' + row.ArticuloId + '" class="dropdown-item"><i class="la la-edit"></i> Modificar</a>';
											   }

							if (row.Estado){
								if(deshabilitar_articulo=== "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_deshabilitar(' + row.ArticuloId + ')"' +
										' data-texto="el artículo seleccionado"' +
										' data-href="deshabilitar/' + row.ArticuloId + '"' +
										' id="btn_deshabilitar_' + row.ArticuloId + '">' +
										' <i class="la la-remove"></i> Deshabilitar' +
										'</a>';
								}
							} else {
								if(habilitar_articulo === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_habilitar(' + row.ArticuloId + ')"' +
										' data-texto="el artículo seleccionado"' +
										' data-href="habilitar/' + row.ArticuloId + '"' +
										' id="btn_habilitar_' + row.ArticuloId + '">' +
										' <i class="la la-check"></i> Habilitar' +
										'</a>';
								}
							}
                        if(eliminar_articulo === "True") {
							opciones += '<a href="javascript:;" class="dropdown-item"' +
								' onclick="mostrar_confirmacion_eliminar(' + row.ArticuloId + ')"' +
								' data-texto="el artículo seleccionado"' +
								' data-href="eliminar/' + row.ArticuloId + '"' +
								' id="btn_eliminar_' + row.ArticuloId + '">' +
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