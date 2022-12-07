'use strict';

var KTDatatableDataLocalDemo = function() {
    var local_data = $('#local_data'),
		usuarios = local_data.data('usuarios'),
		user_id = local_data.data('user_id'),
		modificar_usuario = local_data.data('modificar_usuario'),
		modificar_contrasena_usuario_actual = local_data.data('modificar_contrasena_usuario_actual'),
		modificar_contrasena = local_data.data('modificar_contrasena'),
		deshabilitar_usuario = local_data.data('deshabilitar_usuario'),
		habilitar_usuario = local_data.data('habilitar_usuario'),
		eliminar_usuario = local_data.data('eliminar_usuario'),
		detalles_usuario = local_data.data('detalles_usuario');

	var demo = function() {

		var dataJSON = usuarios;

		var datatable = $('.kt-datatable').KTDatatable({
			data: {
				type: 'local',
				source: dataJSON
			},

			sortable: false,

			pagination: false,

			columns: [
				{
					field: 'UsuarioId',
					title: '#',
					sortable: false,
					width: 15,
					selector: {class: 'kt-checkbox--solid'},
					textAlign: 'center'
				},
				{
					field: 'NombreUsuario',
					title: 'Nombre de usuario'
				},
				{
					field: 'NombreApellidos',
					title: 'Nombre y apellidos'
				},
                {
					field: 'Correo',
					title: 'Correo'
				},
                {
					field: 'Telefono',
					title: 'Teléfono',
					width: 80
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
					field: 'Opciones',
					title: 'Opciones',
					width: 50,
					template: function (row) {
							var opciones = '<div class="dropdown">' +
											   '<a data-toggle="dropdown" class="btn btn-sm btn-clean btn-icon btn-icon-md">' +
												   '<i class="la la-cog"></i>' +
											   '</a>' +
											   '<div class="dropdown-menu dropdown-menu-right">';
								                 if(detalles_usuario === "True") {
													opciones += '<a href="detalles/' + row.UsuarioId + '" class="dropdown-item"><i class="la la-search"></i> Detalles</a>';
												 }
								                 if(modificar_usuario === "True") {
													opciones += '<a href="modificar/' + row.UsuarioId + '" class="dropdown-item"><i class="la la-edit"></i> Editar</a>';
												 }

							if (row.UsuarioId === user_id) {
								if(modificar_contrasena_usuario_actual === "True") {
									opciones += '<a href="modificar_contrasena_usuario_actual/' + row.UsuarioId + '" class="dropdown-item"><i class="la la-key"></i> Cambiar contraseña</a>';
								}
							} else {
								if(modificar_contrasena === "True") {
									opciones += '<a href="modificar_contrasena/' + row.UsuarioId + '" class="dropdown-item"><i class="la la-key"></i> Cambiar contraseña</a>';
								}
							}

							if (row.Estado){
								if(deshabilitar_usuario === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_deshabilitar(' + row.UsuarioId + ')"' +
										' data-texto="el usuario seleccionado"' +
										' data-href="deshabilitar/' + row.UsuarioId + '"' +
										' id="btn_deshabilitar_' + row.UsuarioId + '">' +
										' <i class="la la-remove"></i> Deshabilitar' +
										'</a>';
								}
							} else {
								if(habilitar_usuario === "True") {
									opciones += '<a href="javascript:;" class="dropdown-item"' +
										' onclick="mostrar_confirmacion_habilitar(' + row.UsuarioId + ')"' +
										' data-texto="el usuario seleccionado"' +
										' data-href="habilitar/' + row.UsuarioId + '"' +
										' id="btn_habilitar_' + row.UsuarioId + '">' +
										' <i class="la la-check"></i> Habilitar' +
										'</a>';
								}
							}
                         if(eliminar_usuario === "True") {
							 opciones += '<a href="javascript:;" class="dropdown-item"' +
								 ' onclick="mostrar_confirmacion_eliminar(' + row.UsuarioId + ')"' +
								 ' data-texto="el usuario seleccionado"' +
								 ' data-href="eliminar/' + row.UsuarioId + '"' +
								 ' id="btn_eliminar_' + row.UsuarioId + '">' +
								 ' <i class="la la-trash"></i> Eliminar</a>' +
								 ' </div>' +
								 '</div>';
							 return opciones;
						 }
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