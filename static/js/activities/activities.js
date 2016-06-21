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
