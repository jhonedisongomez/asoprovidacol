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
            window.location.reload();
          }

        }else{
          alert(message);
        }
      }

    });
  }
}
