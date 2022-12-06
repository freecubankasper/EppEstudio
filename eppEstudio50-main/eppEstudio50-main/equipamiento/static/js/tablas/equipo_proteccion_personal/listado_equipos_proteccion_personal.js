'use strict';

var KTDatatableDataLocalDemo = function() {
    var local_data = $('#local_data'),
		equipos_proteccion_personal = local_data.data('equipos_proteccion_personal'),
		modificar_equipo_proteccion_personal = local_data.data('modificar_equipo_proteccion_personal'),
		deshabilitar_equipo_proteccion_personal = local_data.data('deshabilitar_equipo_proteccion_personal'),
		habilitar_equipo_proteccion_personal = local_data.data('habilitar_equipo_proteccion_personal'),
		eliminar_equipo_proteccion_personal = local_data.data('eliminar_equipo_proteccion_personal'),
		detalles_equipo_proteccion_personal = local_data.data('detalles_equipo_proteccion_personal'),
		renovar_equipo_proteccion_personal = local_data.data('renovar_equipo_proteccion_personal'),
		exportar_certificado_epp = local_data.data('exportar_certificado_epp');


	var demo = function() {

		var dataJSON = equipos_proteccion_personal;

		var datatable = $('.kt-datatable').KTDatatable({
			data: {
				type: 'local',
				source: dataJSON
			},

			sortable: false,

			pagination: false,

			columns: [
				{
					field: 'EquipoProteccionPersonalId',
					title: '#',
					sortable: false,
					width: 15,
					selector: {class: 'kt-checkbox--solid'},
					textAlign: 'center'
				},
				{
					field: 'Nombre',
					title: 'Nombre'
				},
				{
					field: 'Categoria',
					title: 'Categoría',
					width: 80
				},
				{
					field: 'Factura',
					title: 'Factura',
					width: 80
				},
				{
					field: 'Renovado',
					title: 'Renovado',
					width: 80
				},
                {
					field: 'Entidad',
					title: 'Entidad',
					width: 80
				},
				{
					field: 'Estado',
					title: 'Estado',
					width: 80,
					template: function (row) {
						if (row.Estado){
							return '<span style="width: 145px;">' +
								       '<span class="kt-badge  kt-badge--success kt-badge--inline kt-badge--pill">Vigente</span>' +
								   '</span>';
						}
						else {
							return '<span style="width: 145px;">' +
								       '<span class="kt-badge  kt-badge--danger kt-badge--inline kt-badge--pill">Vencido</span>' +
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
								               if(detalles_equipo_proteccion_personal === "True") {
								               	 opciones += '<a href="detalles/' + row.EquipoProteccionPersonalId + '" class="dropdown-item"><i class="la la-search"></i> Detalles</a>';
											   }
						                      if(row.Factura === "No facturado" && modificar_equipo_proteccion_personal === "True") {
												 opciones += '<a href="modificar/' + row.EquipoProteccionPersonalId + '" class="dropdown-item"><i class="la la-edit"></i> Editar</a>';
											  }
						                      if(row.Factura !== "No facturado" && row.Renovado ==="No" && !row.Estado && renovar_equipo_proteccion_personal === "True") {
												 opciones += '<a href="renovar/' + row.EquipoProteccionPersonalId + '" class="dropdown-item"><i class="la la-check-square"></i> Renovar EPP</a>';
											  }
						                      if(exportar_certificado_epp === "True" && row.Estado ==="True") {
												 opciones += '<a href="certificado_epp/' + row.EquipoProteccionPersonalId + '" class="dropdown-item"><i class="la la-file-pdf-o"></i> Exportar Certificado del EPP</a>';
											  }
                        if(eliminar_equipo_proteccion_personal === "True") {
							opciones += '<a href="javascript:;" class="dropdown-item"' +
								' onclick="mostrar_confirmacion_eliminar(' + row.EquipoProteccionPersonalId + ')"' +
								' data-texto="el equipo de protección personal seleccionado"' +
								' data-href="eliminar/' + row.EquipoProteccionPersonalId + '"' +
								' id="btn_eliminar_' + row.EquipoProteccionPersonalId + '">' +
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