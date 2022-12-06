var provincia = $('#id_provincia'),
    municipio = $('#id_municipio'),
    entidad = $('#id_entidad'),
    organismo = $('#id_organismo'),
    groups = $('#id_groups');

provincia.on('change', function () {
        if ($(this).val() !== '') {
            provincia_municipio($(this).val());
            municipio.prop('disabled', false);
        } else {
            municipio.prop('disabled', true);
        }
});

function provincia_municipio(provincia_id) {
    $.ajax({
        data: {'id_provincia': provincia_id},
        url: '/usuarios/provincia_municipio/',
        type: 'get',
        success: function (municipios) {
            var html = '<option value="">Seleccione una opción...</option>';

            for (var i = 0; i < municipios.length; i++) {
                html += '<option value=' + municipios[i].id + '>' + municipios[i].nombre + '</option>';
            }
            municipio.html(html);
        }
    });
}


municipio.on('change', function () {
    if (organismo.val() !== '' && $(this).val() !== '') {
        municipio_entidad(organismo.val(), $(this).val());
        entidad.prop('disabled', false);
    } else {
        entidad.prop('disabled', true);
    }
});

organismo.on('change', function () {
    if ($(this).val() !== '' && municipio.val() !== '') {
        municipio_entidad($(this).val(), municipio.val());
        entidad.prop('disabled', false);
    } else {
        entidad.prop('disabled', true);
    }
});

function municipio_entidad(organismo_id, municipio_id) {
    $.ajax({
        data: {'id_organismo': organismo_id, 'id_municipio': municipio_id},
        url: '/usuarios/municipio_entidad/',
        type: 'get',
        success: function (entidades) {
            console.log(entidades);
            var html = '<option value="">Seleccione una opción...</option>';

            for (var i = 0; i < entidades.length; i++) {
                html += '<option value=' + entidades[i].id + '>' + entidades[i].nombre + '</option>';
            }
            entidad.html(html);
        }
    });
}

validar_roles(groups.val());

groups.on('change', function () {
    validar_roles($(this).val());
});

function validar_roles(groups_id) {
    if (["1", "2"].includes(groups_id[0]) === true) {
        organismo.prop('disabled', false);
        provincia.prop('disabled', true);
        municipio.prop('disabled', true);
        entidad.prop('disabled', true);

    } else if (["3"].includes(groups_id[0]) === true) {
        organismo.prop('disabled', false);
        provincia.prop('disabled', false);
        municipio.prop('disabled', false);
        entidad.prop('disabled', false);

    } else if (["4"].includes(groups_id[0]) === true) {
        organismo.prop('disabled', true);
        provincia.prop('disabled', false);
        municipio.prop('disabled', true);
        entidad.prop('disabled', true);

    } else if (["5"].includes(groups_id[0]) === true) {
        organismo.prop('disabled', true);
        provincia.prop('disabled', false);
        municipio.prop('disabled', false);
        entidad.prop('disabled', true);

    } else if (["6"].includes(groups_id[0]) === true) {
        organismo.prop('disabled', true);
        provincia.prop('disabled', true);
        municipio.prop('disabled', true);
        entidad.prop('disabled', true);
    }
}