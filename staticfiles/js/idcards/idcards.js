function validateForm(){

	var isValidated = false;
	var countFieldVal = 0;
	varLabelError = "";
	var isChecked = false;

	var form = document.getElementById("renovate-idcard");
	for(var ixForm = 0; ixForm <form.length; ixForm++)
	{
		var field = form[ixForm];
		var tagName = field.tagName;

		if(tagName == "INPUT" || tagName == "SELECT")
		{
			var classList = field.classList;
			for(var ixClass = 0; ixClass < classList.length; ixClass++)
			{
				var validateType = classList[ixClass];


				switch(validateType)
				{

					case "isString":
					case "isNotNull":
					case "isNumber":
					case "isEmail":
					case "isSelected":

						var idField = field.id;
						var idLabel = idField + "LabelError";
						labelError = document.getElementById(idLabel);

						dataResponse = generalValidations(field,validateType);

						if(dataResponse.isValid)
						{
							countFieldVal++;
							labelError.innerHTML = "";
						}else
						{

							labelError.innerHTML = dataResponse.message;
							countFieldVal--;

						}

					break;
				}

			}

		}

	}

	if(countFieldVal == 2)
	{

		renovateIdCard();
	}


}


function renovateIdCard()
{
  var activity = document.getElementById("id_activities").value;
  var email = document.getElementById("email").value;
  var label = document.getElementById("labelMessage");
  $.ajax({

    type: 'get',
    data: {'activity':activity,'email': email, 'method': 'renovateIdCard(request)'},
    url:'/asocampus/renovacion-escarapela',
    success: function(response){

      var isError = response.is_error;
      var message = response.message;

      if(!isError)
      {
        document.getElementById("email").value = "";
        label.innerHTML = message;
        downLoadIdCard(email);

      }else
      {
        label.innerHTML = message;
      }
    }



  })
}
