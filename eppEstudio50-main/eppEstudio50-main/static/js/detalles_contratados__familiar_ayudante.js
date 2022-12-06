function crear_modal__detalles_equipamiento(element_id) {
    $('.modal_generico_mediano__content').html('');  // se reinicia la tabla por si se abrio previamente el modal generico
    // $('#modal_title').text(element_type);

    $.ajax({
        data: {'element_id': element_id},
        type: 'get',
        url: '/crear_modal_detalles_contratado_familiar_ayudante/',
        success: function (result) {

            let html = '' +
                '<div class="kt-portlet kt-portlet--tabs kt-portlet--height-fluid col-xl-11 col-md-11 kt-block-center">' +
                '                        <div class="kt-portlet__body">' +
                '                            <div class="col-xl-12 ">' +
                '                                <div class="row" style="margin-left: 1px">' +
                '                                    <div class="col-xl-12 col-md-12" style="padding: 10px;">' +
                '                                        <img style="width: 100%" src="/media/'+result['imagen']+'"/>'+
                '                                        <p><strong>Nombre:</strong> ' + result['nombre'] + '</p>' +
                '                                        <p><strong>Descripcion:</strong> ' + result['descripcion'] + '</p>' +
                '                                        <p><strong>Marca:</strong> ' + result['marca'] + '</p>' +
                '                                        <p><strong>Categoria:</strong> ' + result['categoria'] + '</p>' +
                '                                        <p><strong>Cantidad:</strong> ' + result['cantidad'] + '</p>'

            html += '                                    </div>' +
            '                        <div class=" kt-portlet__foot">' +
            '                            <div class="kt-portlet__foot--sm" style="display: inline-block">' +
            '                                <h1 style="font-size: 115%">Fecha de actualización: <small>' + result['fecha_actualizacion'] + '</small></h1>' +
            '                            </div>' +
              '<a id="detalles_cont_fa_{{ element.id }}"'+
            'class="c-content-isotope-overlay-btn btn c-btn-white c-btn-uppercase c-btn-bold c-btn-border-1x c-btn-square" onclick="crear_modal_adicionar_equipamiento(result)">Adicionar</a>'+
            '                        </div>' +
            '                    </div>';


            $('.loading_p').addClass('hidden_element');
            $('.loading_img').addClass('hidden_element');

            $('.modal_generico_mediano__content').html(html);
        },
        error: function(res) {
            console.log(`Error: ${res}`)
        }
    });
}


function crear_modal__detalles_talento(element_id) {
    $('.modal_generico_mediano__content').html('');  // se reinicia la tabla por si se abrio previamente el modal generico
    // $('#modal_title').text(element_type);

    $.ajax({
        data: {'element_id': element_id},
        type: 'get',
        url: '/crear_modal_detalles_talento/',
        success: function (result) {

            let html = '' +
                '<div class="kt-portlet kt-portlet--tabs kt-portlet--height-fluid col-xl-12 col-md-12 kt-block-center">' +
                '                        <div class="kt-portlet__body">' +
                '                            <div class="col-xl-12 ">' +
                '                                <div class="row">' +
                '                                    <div class="col-xl-12 col-md-12" style="padding: 10px;">' +
                '                                <div class="row">' +
                '<div class="col-xl-4 col-md-4" style="padding: 5px;">' +
                '                                        <img style="width: 100%" src="/media/'+result['imagen']+'"/>'+
                                '                                    </div>' +
                '<div class="col-xl-4 col-md-4" style="padding: 5px;">' +
                '                                        <img style="width: 100%" src="/media/'+result['imagen2']+'"/>'+
                                                '                                    </div>' +
                '<div class="col-xl-4 col-md-4" style="padding: 5px;">' +
                '                                        <img style="width: 100%" src="/media/'+result['imagen3']+'"/>'+
                                                '                                    </div>' +
                                '                                    </div>' +
                                '                                <div class="row">' +
                '<div class="col-xl-6 col-md-6" style="padding: 5px;">' +
                '                                        <img style="width: 100%" src="/media/'+result['imagen4']+'"/>'+
                                '                                    </div>' +
                '<div class="col-xl-6 col-md-6" style="padding: 5px;">' +
                '                                        <img style="width: 100%" src="/media/'+result['imagen5']+'"/>'+
                                                '                                    </div>' +
                                '                                    </div>' +


                '                                        <p><strong>Nombre:</strong> ' + result['nombre'] + '</p>' +
                '                                        <p><strong>Descripcion:</strong> ' + result['descripcion'] + '</p>'+
                '                                        <p><strong>Estatura:</strong> ' + result['estatura'] + '</p>'+
                '                                        <p><strong>Cadera:</strong> ' + result['cadera'] + '</p>'+
                '                                        <p><strong>Calzado:</strong> ' + result['calzado'] + '</p>'+
                '                                        <p><strong>Cintura:</strong> ' + result['cintura'] + '</p>'+
                '                                        <p><strong>Piel:</strong> ' + result['color_piel'] + '</p>'+
                '                                        <p><strong>Ojos:</strong> ' + result['color_ojos'] + '</p>'+
                '                                        <p><strong>Pelo:</strong> ' + result['tipo_pelo'] + '</p>'+
                '                                        <p><strong>Municipio:</strong> ' + result['municipio'] + '</p>'
                if (result['apodo'] != null){
                                    '                                        +<p><strong>Marca:</strong> ' + result['apodo'] + '</p>'

                }
                +'                                        <p><strong>Categoria:</strong> ' + result['categoria'] + '</p>'

            html += '                                    </div>' +
            '                        <div class=" kt-portlet__foot">' +
            '                            <div class="kt-portlet__foot--sm" style="display: inline-block">' +
            '                                <h1 style="font-size: 115%">Fecha de actualización: <small>' + result['fecha_actualizacion'] + '</small></h1>' +
            '                            </div>' +
              '<a id="detalles_cont_fa_{{ element.id }}"'+

            '                        </div>' +
            '                    </div>';


            $('.loading_p').addClass('hidden_element');
            $('.loading_img').addClass('hidden_element');

            $('.modal_generico_mediano__content').html(html);
        },
        error: function(res) {
            console.log(`Error: ${res}`)
        }
    });
}
