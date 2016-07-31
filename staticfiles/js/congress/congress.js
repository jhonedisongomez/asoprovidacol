function signUpCongress()
{
  var username = document.getElementById("username").value;
  var csrftoken = getCookie('csrftoken');

  $.ajax({

    type : 'post',
    data : {'username':username,'csrfmiddlewaretoken': csrftoken},
    url : "/congreso2016/",
    success: function(response)
    {
      var isError = response.is_error;
      var message = response.message;

      if(!isError)
      {
        alert(message);
      }else
      {
        alert(message);
      }
    }
  });
}

function agendaLoad()
{
  $.ajax({
    type: 'get',
    data: {'load':true},
    url: "/agenda-congreso/",
    success: function(response)
    {
      var isError = response.is_error;
      var message = response.message;

      if(!isError)
      {
        alert("hello you can load the data in the tables");
      }else
      {
        alert(message);
      }
    }
  });
}
