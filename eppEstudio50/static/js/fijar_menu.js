let body = $('.body-class-main'),
    active_class_name = 'kt-aside--minimize',
    cookie_name = 'menu_fijado',
    cookie = getCookie(cookie_name);

if (cookie === 'True') {
    body.removeClass(active_class_name);
} else if (cookie === 'False') {
    body.addClass(active_class_name);
}

function fijar_menu() {

    let clases = body.attr('class').split(' ');

    if( clases.indexOf(active_class_name) > 0){
        setCookie(cookie_name, 'False;');
    } else {
        setCookie(cookie_name, 'True;');
    }
}

function getCookie(cookie_name) {

    let nameEQ = cookie_name + '=',
        cookies_list = document.cookie.split(';'),
        cookie;

    for (let i = 0; i < cookies_list.length; i ++) {
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
    let date = new Date(),
        year = date.getFullYear(),
        month = date.getMonth(),
        day = date.getDate(),
        expire_date = new Date(year + 1, month, day);  // Tiempo de expiración de la cookie: 1 año

    document.cookie = cookie_name + '=' + cookie_value + '; expires=' + expire_date.toUTCString();
}