var REMEMBER_SESSION_COOKIE_NAME = 'remember_session',
    id_checkbox_remember_user = $('#id_checkbox_remember_user'),
    remember_user_coockie_value = getCookie(REMEMBER_SESSION_COOKIE_NAME);


if (remember_user_coockie_value === 'True'){
    id_checkbox_remember_user.prop('checked', true);
}
else {
    id_checkbox_remember_user.prop('checked', false);
}

function getCookie(cookie_name) {

    var nameEQ = cookie_name + '=',
        cookies_list = document.cookie.split(';'),
        cookie;

    for (var i = 0; i < cookies_list.length; i ++) {
        cookie = cookies_list[i];

        while (cookie.charAt(0) === ' ') {
            cookie = cookie.substring(1, cookie.length);
        }

        if (cookie.indexOf(nameEQ) === 0) {
            return cookie.substring(nameEQ.length, cookie.length);
        }
    }
}


function setCookie(cookie_name, cookie_value) {
    var date = new Date(),
        year = date.getFullYear(),
        month = date.getMonth(),
        day = date.getDate(),
        expire_date = new Date(year + 1, month, day);  // Tiempo de expiración de la cookie: 1 año

    document.cookie = cookie_name + '=' + cookie_value + '; expires=' + expire_date.toUTCString();
}


function remember_session(value) {
    if (value.checked){
        setCookie(REMEMBER_SESSION_COOKIE_NAME, 'True;');
    }
    else {
        setCookie(REMEMBER_SESSION_COOKIE_NAME, 'False;');
    }
}
