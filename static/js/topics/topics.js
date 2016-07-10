function createTopic()
{
  var topicName = document.getElementById("topic-name").value;
  var professorName = document.getElementById("professor-name").value;
  var description = document.getElementById("topic-description").value;
  var cfrsTocken = document.getElementById("csrfmiddlewaretoken").value;

  $.ajax({

    type:'post',
    data:{'topic_name': topicName, 'professor_name': professorName, 'description': description, 'csrfmiddlewaretoken':cfrsTocken},
    url:'/asocampus/crear-tema/',
    success: function(response){

      var isError = response.is_error;
      var message = response.message;
      var label = document.getElementById("labelMessage");


      if(!isError){
        label.innerText = message;
        document.getElementById("topic-name").value = "";
        document.getElementById("professor-name").value = "";
        document.getElementById("description-topic").value = "";

      }else
      {
        label.innerText = message;
      }
    }

  });

}
