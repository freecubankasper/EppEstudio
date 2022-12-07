function mostrar_confirmacion_eliminar_seleccionados(verbose_name) {

    var tbody_tabla = document.querySelectorAll("tbody"),
        elements = tbody_tabla[0].getElementsByClassName('kt-datatable__row--active'),
        ids = [];

    if (elements.length > 0){
        for (var i = 0; i < elements.length; i++){
            ids.push(elements[i].getElementsByTagName("input")[0].value);
        }
    }

    swal({
        title: '¿Desea eliminar ' + verbose_name + '?',
        type: 'warning',
        showCancelButton: true,
        showConfirmButton: true,
        allowOutsideClick: false,
        confirmButtonText: 'Aceptar',
        cancelButtonText: 'Cancelar',
        cancelButtonClass: 'btn-secondary'
    }, function () {
        if (ids.length > 0) {
            var href = $('#btn_eliminar_seleccionados').data('href');
            $.ajax({
                data: {'ids': ids.toString()},
                url: href,
                type: 'get',
                success: function () {
                location.reload(true);
                }
            });
        }
    });
}

function mostrar_confirmacion_eliminar(id) {
    var verbose_name = $('#btn_eliminar_' + id).data('texto');
    swal({
        title: '¿Desea eliminar ' + verbose_name + '?',
        type: 'warning',
        showCancelButton: true,
        showConfirmButton: true,
        allowOutsideClick: false,
        confirmButtonText: 'Aceptar',
        cancelButtonText: 'Cancelar',
        cancelButtonClass: 'btn-secondary'
    }, function () {
        var href = $('#btn_eliminar_' + id).data('href');
        $.ajax({
            type: 'GET',
            url: href,
            success: function () {
                location.reload(true);
            }
        });
    });
}

function mostrar_confirmacion_habilitar(id) {
    var verbose_name = $('#btn_habilitar_' + id).data('texto');
    swal({
        title: '¿Desea habilitar ' + verbose_name + '?',
        type: 'warning',
        showCancelButton: true,
        showConfirmButton: true,
        allowOutsideClick: false,
        confirmButtonText: 'Aceptar',
        cancelButtonText: 'Cancelar',
        cancelButtonClass: 'btn-secondary'
    }, function () {
        var href = $('#btn_habilitar_' + id).data('href');
        $.ajax({
            type: 'GET',
            url: href,
            success: function () {
                location.reload(true);
            }
        });
    });
}

function mostrar_confirmacion_deshabilitar(id) {
    var verbose_name = $('#btn_deshabilitar_' + id).data('texto');
    swal({
        title: '¿Desea deshabilitar ' + verbose_name + '?',
        type: 'warning',
        showCancelButton: true,
        showConfirmButton: true,
        allowOutsideClick: false,
        confirmButtonText: 'Aceptar',
        cancelButtonText: 'Cancelar',
        cancelButtonClass: 'btn-secondary'
    }, function () {
        var href = $('#btn_deshabilitar_' + id).data('href');
        $.ajax({
            type: 'GET',
            url: href,
            success: function () {
                location.reload(true);
            }
        });
    });
}

function mostrar_confirmacion_deshabilitar_persona(id) {
    var verbose_name = $('#btn_deshabilitar_persona_' + id).data('texto');
    swal({
        title: '¿Desea deshabilitar ' + verbose_name + '?',
        type: 'warning',
        showCancelButton: true,
        showConfirmButton: true,
        allowOutsideClick: false,
        confirmButtonText: 'Aceptar',
        cancelButtonText: 'Cancelar',
        cancelButtonClass: 'btn-secondary'
    }, function () {
        var href = $('#btn_deshabilitar_persona_' + id).data('href');
        $.ajax({
            type: 'GET',
            url: href,
            success: function () {
                location.reload(true);
            }
        });
    });
}

function mostrar_confirmacion_renovacion(id) {
    var verbose_name = $('#btn_renovar_' + id).data('texto');
    swal({
        title: '¿Desea renovar ' + verbose_name + '?',
        type: 'warning',
        showCancelButton: true,
        showConfirmButton: true,
        allowOutsideClick: false,
        confirmButtonText: 'Aceptar',
        cancelButtonText: 'Cancelar',
        cancelButtonClass: 'btn-secondary'
    }, function () {
        var href = $('#btn_renovar_' + id).data('href');
        $.ajax({
            type: 'GET',
            url: href,
            success: function () {
                location.reload(true);
            }
        });
    });
}

function mostrar_confirmacion_cancelacion(id) {
    var verbose_name = $('#btn_cancelar_' + id).data('texto');
    swal({
        title: '¿Desea cancelar ' + verbose_name + '?',
        type: 'warning',
        showCancelButton: true,
        showConfirmButton: true,
        allowOutsideClick: false,
        confirmButtonText: 'Aceptar',
        cancelButtonText: 'Cancelar',
        cancelButtonClass: 'btn-secondary'
    }, function () {
        var href = $('#btn_cancelar_' + id).data('href');
        $.ajax({
            type: 'GET',
            url: href,
            success: function () {
                location.reload(true);
            }
        });
    });
}