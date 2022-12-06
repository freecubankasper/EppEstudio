'use strict';

var KTDatatableDataLocalDemo = function() {
    var local_data = $('#local_data'),
		numeros_prefactura = local_data.data('numeros_prefactura'),
		modificar_numero_prefactura = local_data.data('modificar_numero_prefactura'),
		deshabilitar_numero_prefactura = local_data.data('deshabilitar_numero_prefactura'),
		habilitar_numero_prefactura = local_data.data('habilitar_numero_prefactura'),
		eliminar_numero_prefactura = local_data.data('eliminar_numero_prefactura');

	var demo = function() {

		var dataJSON = numeros_prefactura;

		var datatable = $('.kt-datatable').KTDatatable({
			data: {
				type: 'local',
				source: dataJSON
			},

			sortable: false,

			pagination: false,

			columns: [
				{
					field: 'NumeroPrefacturaId',
					title: '#',
					sortable: false,
					width: 50,
					textAlign: 'center'
				},
				{
					field: 'NumeroPrefactura',
					title: 'Número de prefactura',
					width: 80,
				},
				{
					field: 'Entidad',
					title: 'Entidad',
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
								               if(modificar_numero_prefactura === "True") {
								               	 opciones += '<a href="modificar/' + row.NumeroPrefacturaId + '" class="dropdown-item"><i class="la la-edit"></i> Modificar</a>';
											   }

							if (row.Estado){
								if(deshabilitar_numero_prefactura === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_deshabilitar(' + row.NumeroPrefacturaId + ')"' +
										' data-texto="el número de prefactura seleccionado"' +
										' data-href="deshabilitar/' + row.NumeroPrefacturaId + '"' +
										' id="btn_deshabilitar_' + row.NumeroPrefacturaId + '">' +
										' <i class="la la-remove"></i> Deshabilitar' +
										'</a>';
								}
							} else {
								if(habilitar_numero_prefactura === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_habilitar(' + row.NumeroPrefacturaId + ')"' +
										' data-texto="el número de prefactura seleccionado"' +
										' data-href="habilitar/' + row.NumeroPrefacturaId + '"' +
										' id="btn_habilitar_' + row.NumeroPrefacturaId + '">' +
										' <i class="la la-check"></i> Habilitar' +
										'</a>';
								}
							}
                        if(eliminar_numero_prefactura === "True") {
							opciones += '<a href="javascript:;" class="dropdown-item"' +
								' onclick="mostrar_confirmacion_eliminar(' + row.NumeroPrefacturaId + ')"' +
								' data-texto="el número de prefactura seleccionado"' +
								' data-href="eliminar/' + row.NumeroPrefacturaId + '"' +
								' id="btn_eliminar_' + row.NumeroPrefacturaId + '">' +
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