function validateForm(){

	var isValidated = false;
	var countFieldVal = 0;
	varLabelError = "";
	var isChecked = false;

	var form = document.getElementById("create-payment");
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

		validatePersonPay();
	}


}


//validate if a person pay
function validatePersonPay()
{

  var activity = document.getElementById("id_activities").value;
  var email = document.getElementById("email").value;

  $.ajax({

    type: 'get',
    data: {'method': 'validatePayPerson(request)', 'email': email, 'activity': activity},
    url: '/asocampus/pago-de-actividad',
    success: function(response)
    {
      var isError = response.is_error;
      var message = response.message;
      var label = document.getElementById("labelMessage");

      if(!isError)
      {
        var isSignUpDb = response.is_sign_up_db;
        if(isSignUpDb)
        {
          var isSignUp = response.is_sign_up;
          if(isSignUp)
          {
            var isPaied = response.is_paied;
            if(isPaied)
            {
              //puede descargar la escarapela
              label.innerText = message;
              downLoadIdCard(email);
            }else{
              //se registra el pago
              //label.innerText = message;
              savePay(activity,email);
            }

          }else
          {
            //sign up the user
            label.innerText = message;
          }

        }else
        {
          //not found in the database
          label.innerText = message;

        }
      }else
      {
        label.innerText = message;
      }
    }



  });
}

//function to save the pay by the user
function savePay(activity, email)
{
  var label = document.getElementById("labelMessage");
  var cfrsTocken = document.getElementById("csrfmiddlewaretoken").value;
  $.ajax({
    type: 'post',
    data: {'method': 'savePAgePerson(request)', 'email': email, 'activity': activity,'csrfmiddlewaretoken':cfrsTocken},
    url: '/asocampus/pago-de-actividad/',
    success: function(response)
    {
      var isError = response.is_error;
      var message = response.message;

      if(!isError)
      {
        label.innerText = message;
        downLoadIdCard(email);
      }else
      {
      label.innerText = message;
      }
    }
  });
}

function downLoadIdCard(email)
{
  $.ajax({

    type: 'get',
    data:{'email':email},
    url: '/asocampus/consultar-escarapela/',
    success: function(response)
    {
      var isError = response.is_error;
      var message = response.message;
      var isDownloaded = response.is_downloaded;
      var isAuthenticated = response.is_authenticated;
      var isSignUp = response.is_sign_up;

      if(!isError)
      {
        if(isDownloaded)
        {
          alert(message);
        }else
        {
          if(isAuthenticated)
          {
            if(isSignUp)
            {
              var idCardCode = response.id_card_code
              $.ajax({

                type:'get',
                url: '/asocampus/descargar-escarapela/',
                data:{'id_card_code':idCardCode},
                contentType:'application/pdf',
                success:function(data)
                {
                  var file = new Blob([data], {type: 'application/pdf'});
                  saveAs(file, email + "-congreso-asoprivida-2016.pdf");
                }
              })
            }else
            {
              alert(message);
            }

          }else
          {
            alert(message);
          }

        }
      }else
      {
        alert(message);
      }

    }

  });
}
