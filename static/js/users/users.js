function signIn()
{
  var getUsername = document.getElementsByName("username")[0];
  var getPassword = document.getElementsByName("password")[0];
  var validateUsername = getUsername.validate();
  var validatePassword = getPassword.validate();

  if(validateUsername && validatePassword)
  {
    var username = getUsername.value;
    var password = getPassword.value;
    $.ajax({
      type: 'get',
      data: {'username':username,'password':password},
      url: '/sign-in/',

      success: function(response)
      {
        var isError = response.is_error;
        var message = response.message;

        if(!isError)
        {
          var authenticated = response.authenticated;

          if(!authenticated)
          {
            alert(message);
          }else
          {
            window.location.replace("http://localhost:8000/");
          }

        }else{
          alert(message);
        }
      }

    });
  }
}

function searchEmail()
{
  var getEmail = document.getElementById("email");
  var validateEmail = getEmail.validate();
  if(validateEmail)
  {
    var email = getEmail.value;

    $.ajax({

      type: 'get',
      data:{'email': email},
      url: '/sign-up/',
      success: function(response)
      {
        var isError = response.is_error;
        var message = response.message;

        if(!isError)
        {
          var exist = response.exist;
          if(exist)
          {
            document.getElementById("first_name").readonly = true;
            document.getElementById("last_name").readonly = true;
            document.getElementById("password").readonly = true;
            document.getElementById("again_password").readonly = true;
            document.getElementById("save_form").disabled = true;
            document.getElementById("cancel").disabled = true;


            alert(message);
          }else
          {
            document.getElementById("first_name").readonly = false
            document.getElementById("last_name").readonly = false
            document.getElementById("password").readonly = false
            document.getElementById("again_password").readonly = false
            document.getElementById("save_form").disabled = false
            document.getElementById("cancel").disabled = false
            alert(message);

            var nameMatch = email.match(/^([^@]*)@/);
            var name = nameMatch ? nameMatch[1] : null;
            document.getElementById("username").value = name;
          }
        }else
        {
          alert(message);
        }
      }

    });
  }
}

function signUp()
{
  var getEmail = document.getElementById("email");
  var getFirstName = document.getElementById("first_name");
  var getLastName = document.getElementById("last_name");
  var getUsername = document.getElementById("username");
  var getPassword = document.getElementById("password");
  var getAgainPassword = document.getElementById("again_password");

  var validateEmail = getEmail.validate();
  var validateFirstName = getFirstName.validate();
  var validateLastName = getLastName.validate();
  var validateUsername = getUsername.validate();
  var validatePassword = getPassword.validate();
  var validateAgainPassword = getAgainPassword.validate();

  if(validatePassword ==validateAgainPassword)
  {
    if(validateEmail && validateFirstName && validateLastName && validateUsername && validatePassword && validateAgainPassword)
    {

      var email = getEmail.value;
      var firstName = getFirstName.value;
      var lastName = getLastName.value;
      var username = getUsername.value;
      var password = getPassword.value;
      var csrftoken = getCookie('csrftoken');

      $.ajax({

        type: 'post',
        data:{'email':email,
              'first_name':firstName,
              'last_name':lastName,
              'username':username,
              'password':password,
              'csrfmiddlewaretoken': csrftoken},

        url: '/sign-up/',

        success: function(response)
        {
          var isError = response.is_error;
          var message = response.message;

          if(!isError)
          {

            document.getElementById("first_name").readonly = true;
            document.getElementById("last_name").readonly = true;
            document.getElementById("password").readonly = true;
            document.getElementById("again_password").readonly = true;
            document.getElementById("save_form").disabled = true;
            document.getElementById("cancel").disabled = true;

            document.getElementById("first_name").value = "";
            document.getElementById("last_name").value = "";
            document.getElementById("password").value = "";
            document.getElementById("again_password").value = "";

            alert(message);

          }else
          {
            alert(message);
          }
        }
      });

    }


  }else
  {
    alert("las contraseñas no coinciden")
  }


}
