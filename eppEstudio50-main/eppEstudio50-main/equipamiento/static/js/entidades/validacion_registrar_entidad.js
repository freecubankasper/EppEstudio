var pais = $('#id_pais'),
    municipio = $('#id_municipio'),
    cod_reeup = $('#id_cod_reeup'),
    organismo = $('#id_organismo'),
    num_lic_comercial_camara_comercio = $('#id_num_lic_comercial_camara_comercio'),
    num_acta_protocolizacion = $('#id_num_acta_protocolizacion'),
    identificacion_fiscal = $('#id_identificacion_fiscal'),
    num_escritura_publica = $('#id_num_escritura_publica'),
    tipo_entidad_nacional = $('#id_tipo_entidad_nacional'),
    tipo_entidad_extranjera = $('#id_tipo_entidad_extranjera');

tipo_entidad_nacional.prop('disabled', true);
tipo_entidad_extranjera.prop('disabled', true);

validar_pais();

pais.on('change', function () {
    validar_pais();
});

tipo_entidad_nacional.on('change', function () {
    validar_pais();
});

tipo_entidad_extranjera.on('change', function () {
    validar_pais();
});

function validar_pais() {
    if (["","247"].includes(pais.val()) === false) {
        cod_reeup.prop('disabled', true);
        cod_reeup.val("");
        let default_option = new Option("Seleccione una opción...","",true,true);
        organismo.prop('disabled', true);
        organismo.append(default_option).trigger('change');
        municipio.prop('disabled', true);
        municipio.append(default_option).trigger('change');
        identificacion_fiscal.prop('disabled', true);
        identificacion_fiscal.val("");
        num_escritura_publica.prop('disabled', true);
        num_escritura_publica.val("");
        num_lic_comercial_camara_comercio.prop('disabled', false);
        num_acta_protocolizacion.prop('disabled', false);
        tipo_entidad_extranjera.prop('disabled', false);
        tipo_entidad_extranjera.prop('required', true);
        tipo_entidad_nacional.prop('disabled', true);
        tipo_entidad_nacional.append(default_option).trigger('change');

    } else if (["247"].includes(pais.val()) === true && ["5","6"].includes(tipo_entidad_nacional.val()) === true) {
        num_acta_protocolizacion.prop('disabled', true);
        num_lic_comercial_camara_comercio.prop('disabled', true);
        cod_reeup.prop('disabled', true);
        organismo.prop('disabled', true);
        tipo_entidad_nacional.prop('disabled', false);
        identificacion_fiscal.prop('disabled', true);
        num_escritura_publica.prop('disabled', false);
        num_escritura_publica.prop('required', true);
        num_lic_comercial_camara_comercio.val("");
        num_acta_protocolizacion.val("");
        identificacion_fiscal.val("");
        cod_reeup.val("");
        let default_option = new Option("Seleccione una opción...","",true,true);
        organismo.append(default_option).trigger('change');

    } else if (["247"].includes(pais.val()) === true && ["3","4"].includes(tipo_entidad_nacional.val()) === true) {
        num_acta_protocolizacion.prop('disabled', true);
        num_lic_comercial_camara_comercio.prop('disabled', true);
        cod_reeup.prop('disabled', true);
        organismo.prop('disabled', true);
        tipo_entidad_nacional.prop('disabled', false);
        num_escritura_publica.prop('disabled', true);
        identificacion_fiscal.prop('disabled', false);
        identificacion_fiscal.prop('required', true);
        num_lic_comercial_camara_comercio.val("");
        num_acta_protocolizacion.val("");
        num_escritura_publica.val("");
        cod_reeup.val("");
        let default_option = new Option("Seleccione una opción...","",true,true);
        organismo.append(default_option).trigger('change');

    } else if (["247"].includes(pais.val()) === true && ["1","7"].includes(tipo_entidad_nacional.val()) === true) {
        num_acta_protocolizacion.prop('disabled', true);
        num_lic_comercial_camara_comercio.prop('disabled', true);
        num_escritura_publica.prop('disabled', true);
        identificacion_fiscal.prop('disabled', true);
        tipo_entidad_nacional.prop('disabled', false);
        cod_reeup.prop('disabled', false);
        organismo.prop('disabled', false);
        municipio.prop('disabled', false);
        cod_reeup.prop('required', true);
        organismo.prop('required', true);
        municipio.prop('required', true);
        num_lic_comercial_camara_comercio.val("");
        num_acta_protocolizacion.val("");
        num_escritura_publica.val("");
        identificacion_fiscal.val("");

    } else if (["247"].includes(pais.val()) === true) {
        cod_reeup.prop('disabled', false);
        organismo.prop('disabled', false);
        identificacion_fiscal.prop('disabled', false);
        municipio.prop('disabled', false);
        num_escritura_publica.prop('disabled', false);
        num_lic_comercial_camara_comercio.prop('disabled', true);
        num_acta_protocolizacion.prop('disabled', true);
        tipo_entidad_nacional.prop('disabled', false);
        tipo_entidad_nacional.prop('required', true);
        tipo_entidad_extranjera.prop('disabled', true);
        let default_option = new Option("Seleccione una opción...","",true,true);
        tipo_entidad_extranjera.append(default_option).trigger('change');

    }
}


