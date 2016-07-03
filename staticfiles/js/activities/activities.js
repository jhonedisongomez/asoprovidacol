function createActivityRoom()
{
  var room = document.getElementById("id_rooms").value;
  var activity = document.getElementById("id_activities").value;
  var topic = document.getElementById("id_topics").value
  var cfrsTocken= document.getElementById("csrfmiddlewaretoken").value;

  $.ajax({

    type: 'post',
    data: {'room': room, 'activity': activity, 'topic': topic, 'csrfmiddlewaretoken': cfrsTocken},
    url: '/asocampus/crear-actividad-por-tema/',
    success: function(response)
    {
      var message = response.message;
      var isError = response.is_error;
      var label = document.getElementById("labelMessage");

      if(!isError)
      {
        label.innerText = message;
        var form = document.getElementById("create-activity-room");
        form.reset();

      }else
      {
        alert(message);
      }
    }
  });


}


function loadRoom()
{
  var municipio = document.getElementById("id_municipios").value;

  $.ajax({

    type: 'get',
    url: '/asocampus/list-rooms/',
    data:{'section': municipio},
    success: function(response)
    {
      var isError = response.is_error;
      var message = response.message;
      var combo = document.getElementById("room_id");
      if(!isError)
      {

        var roomList = response.rooms_list;

        var option = document.createElement("option");
        option.value = "";
        option.innerHTML = "por favor seleccione una opcion"
        combo.appendChild(option);

        for(var index = 0; index < roomList.length; index ++)
        {
          var option = document.createElement("option");
          option.value = roomList[index].room_pk;
          option.innerHTML = roomList[index].room_name;

          combo.appendChild(option);
        }


      }else
      alert(message);
      {
      }
    }
  });
}


function agendaList()
{
  var activitiesPk = document.getElementById("id_activities").value;
  var roomPk = document.getElementById("room_id").value;

  $.ajax({

    type: 'get',
    data: {'room_pk': roomPk},
    url: '/asocampus/list-schedule/',
    success: function(response)
    {
      var isError = response.is_error;
      var message = response.messge;

      if(!isError)
      {
        var agendaList = response.list_agenda;
        var combo = document.getElementById("agenda-id");

        for(var index = 0; index < agendaList.length; index ++)
        {
          var option = document.createElement("option");
          option.value = agendaList[index].agenda_pk;
          option.innerHTML = agendaList[index].date;

          combo.appendChild(option);
        }
      }else
      {
        alert(message);
      }
    }

  });

}


function validateSignUpActivity()
{
  var signUpCode = document.getElementById("sign-up-code").value;
  var date = document.getElementById("agenda-id").value;
  var activity = document.getElementById("id_activities").value;
  var roomPk = document.getElementById("room_id").value;

  $.ajax({
    type: 'get',
    data: {'sign_up_code': signUpCode, 'activity_id': activity, 'room_id': roomPk, 'agenda_id': date},
    url: '/asocampus/verificar-inscripcion/',
    success: function(response)
    {
      var isError = response.is_error;
      var message = response.message;

      if(!isError)
      {
        console.log(message);
      }else
      {
        console.log(message);
      }
    }
  });

}
