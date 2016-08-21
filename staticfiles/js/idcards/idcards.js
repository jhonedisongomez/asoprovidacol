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
