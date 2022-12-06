"use strict";

var KTBootstrapNotifyDemo = function () {
    
    var message = $('#messages').data("messages");

    if(message !== undefined) {

        var demo = function () {
            $('[data-switch=true]').bootstrapSwitch();  // init bootstrap switch

            var message_level = $('#messages').data("message_level");
            var type = "";
            var icono = "";

            if (message_level === 40){
                type = "danger";
                icono = "la la-exclamation-triangle";
            }
            else{
                type = "success";
                icono = "la la-check";
            }

            var content = {};
            content.message = message;
            content.icon = 'icon ' + icono;

            var notify = $.notify(content, {
                type: type,
                allow_dismiss: true,
                spacing: 10,
                timer: 3000,
                placement: {
                    from: "bottom",
				    align: "right"
                },
                offset: {
                    x: 30,
                    y: 30
                },
                delay: 1000,
                z_index: 10000,
                animate: {
                    enter: 'animated fadeInRight',
                    exit: 'animated zoomOutRight'
                }
            });
        };

        return {
            init: function () {
                demo();
            }
        };
    }

    return { init: function () {} };
}();

jQuery(document).ready(function() {    
    KTBootstrapNotifyDemo.init();
});