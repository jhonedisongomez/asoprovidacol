function createRoom()
{
  var roomName = document.getElementById("room-name").value;
  var address = document.getElementById("address").value;
  var capacity = document.getElementById("capacity").value;
  var section = document.getElementById("id_municipios").value;
  var cfrsTocken = document.getElementById("csrfmiddlewaretoken").value;

  $.ajax({

    type: 'post',
    data: {'room_name': roomName, 'address': address, 'capacity': capacity,'section': section, 'csrfmiddlewaretoken': cfrsTocken},
    url: '/asocampus/crear-salon/',
    success: function(response){

      var isError = response.is_error;
      var message = response.message;
      var label = document.getElementById("labelMessage");

      if(!isError)
      {
        label.innerText = message;
        document.getElementById("room-name").value = "";
        document.getElementById("address").value = "";
        document.getElementById("capacity").value = "";
        
      }else
      {
        alert(message);
      }
    }

  });

}
