function createDate()
{
  var date = document.getElementById("input-date").value;
  var timeFrom = document.getElementById("input-from-time").value;
  var timeTo = document.getElementById("input-to-time").value;
  var cfrsTocken = document.getElementById("csrfmiddlewaretoken").value;

  var time = timeFrom + " - " +  timeTo;

  $.ajax({

    type: 'post',
    data: {'date': date, 'time':time ,'csrfmiddlewaretoken':cfrsTocken},
    url: '/asocampus/crear-fecha/',
    success: function(response){

      var message = response.message;
      var isError = response.is_error;
      var label = document.getElementById("labelMessage");

      if(!isError)
      {
        label.innerText = message;
        document.getElementById("input-date").value = "";
        document.getElementById("input-from-time").value = "";
        document.getElementById("input-to-time").value = "";
        document.getElementById("csrfmiddlewaretoken").value = "";



      }else
      {
        label.innerText = message;
      }


    }


  })
}

function createAgenda()
{
  var activityRoomPk = document.getElementById("id_activity_rooms").value;
  var agendaPk = document.getElementById("id_agendas").value;
  var cfrsTocken = document.getElementById("csrfmiddlewaretoken").value;

  $.ajax({

    type: 'post',
    data: {'activity_room_pk': activityRoomPk, 'agenda_pk':agendaPk ,'csrfmiddlewaretoken':cfrsTocken},
    url: '/asocampus/crear-agenda/',
    success: function(response){

      var message = response.message;
      var isError = response.is_error;
      var label = document.getElementById("labelMessage");

      if(!isError)
      {
        label.innerText = message;
        document.getElementById("create-agenda").reset();



      }else
      {
        label.innerText = message;
      }


    }


  })
}