'use strict';

var KTDatatableDataLocalDemo = function() {
    var local_data = $('#local_data'),
		facturas = local_data.data('facturas'),
		deshabilitar_factura = local_data.data('deshabilitar_factura'),
		habilitar_factura = local_data.data('habilitar_factura'),
		eliminar_factura = local_data.data('eliminar_factura'),
		detalles_factura = local_data.data('detalles_factura');

	var demo = function() {

		var dataJSON = facturas;

		var datatable = $('.kt-datatable').KTDatatable({
			data: {
				type: 'local',
				source: dataJSON
			},

			sortable: false,

			pagination: false,

			columns: [
				{
					field: 'FacturaId',
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
					field: 'EstadoPago',
					title: 'Estado de pago',
					width: 80
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
					field: 'FechaPago',
					title: 'Fecha de pago'

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
								               if(detalles_factura === "True") {
								               	 opciones += '<a href="detalles/' + row.FacturaId + '" class="dropdown-item"><i class="la la-search"></i> Detalles</a>';
											   }

							if (row.Estado){
								if(deshabilitar_factura === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_deshabilitar(' + row.FacturaId + ')"' +
										' data-texto="la factura seleccionada"' +
										' data-href="deshabilitar/' + row.FacturaId + '"' +
										' id="btn_deshabilitar_' + row.FacturaId + '">' +
										' <i class="la la-remove"></i> Deshabilitar' +
										'</a>';
								}
							} else {
								if(habilitar_factura === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_habilitar(' + row.FacturaId + ')"' +
										' data-texto="la factura seleccionada"' +
										' data-href="habilitar/' + row.FacturaId + '"' +
										' id="btn_habilitar_' + row.FacturaId + '">' +
										' <i class="la la-check"></i> Habilitar' +
										'</a>';
								}
							}
                        if(eliminar_factura === "True") {
							opciones += '<a href="javascript:;" class="dropdown-item"' +
								' onclick="mostrar_confirmacion_eliminar(' + row.FacturaId + ')"' +
								' data-texto="la factura seleccionada"' +
								' data-href="eliminar/' + row.FacturaId + '"' +
								' id="btn_eliminar_' + row.FacturaId + '">' +
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