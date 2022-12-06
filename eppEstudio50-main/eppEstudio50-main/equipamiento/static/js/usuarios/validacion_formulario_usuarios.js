$("#form_usuario").validate({
    rules: {
        first_name: 'required',
        last_name: 'required',
        username: {
            required: true,
            // regexp: /^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$/
            regx: /^[a-zA-Z0-9]{8,20}$/
        },
        email: {
            required: true,
            email: true
        },
        password1: 'required',
        password2: {
            required: true,
            minlength: 8,
            equalTo: '#id_password1'
        },
        categoria_usuario: 'required'
    },
    messages:{
        username: {
            regx: "Introduza un nombre de usuario válido. Este valor puede contener únicamente letras, números y los caracteres . y _"
        },
        password2: {
            minlength: "Esta contraseña es demasiado corta. Debe contener al menos {0} caracteres.",
            equalTo: "Los dos campos de contraseña no coinciden. Por favor, rectifíquelos."
        }
    }
});


