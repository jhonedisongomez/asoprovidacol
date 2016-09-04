function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function generalValidations(field,typeValidation)
{
	var isValid = false;
	var message = "";
	var responseData = {};

	/*
	validations type:
		- is number(document number, phones)
		- is null(birthday,first name, last name,address)
		- is email
		- is select(radio buttons and select combos)
	*/

	switch(typeValidation)
	{
		case 'isNumber':

			if(!isNaN(field.value) && field.value != '')
			{
				isValid = true;
				message = "";

			}else
			{
				isValid = false;
				message = "por favor ingrese un numero entero";
			}

		break;

		case 'isSelected':

			if(field.selectedIndex != 0)
			{
				isValid = true;
			}else
			{

				isValid = false;
				message = "por favor seleccione una opcion";
			}

		break;

		case 'isEmail':

			var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
			if(re.test(field.value))
			{
				isValid = true;
			}else
			{

				isValid = false;
				message = "por favor ingrese un email valido";
			}

		break;

		case 'isString':

			if(field.value != '' && isNaN(field.value))
			{
				isValid = true;
			}else
			{

				isValid = false;
				message = "por favor solo ingrese letras";
			}

		break;

		case 'isNotNull':

			if(field.value != '')
			{
				isValid = true;
			}else
			{

				isValid = false;
				message = "este campo no puede estar vacio";
			}

		break;

		case 'isChecked':
			if(field.checked)
			{
				isValid = true;
			}else
			{
				message = "por favor seleccione una opcion";
			}

		break;
	}
	responseData['message'] = message;
	responseData['isValid'] = isValid;
	return responseData;
}
