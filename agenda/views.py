from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
import json
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin
from .models import Agenda, SignUpSchedule
from datetime import datetime

from topics.models import Topic, ActivityRoom#, RoomTopic
from rooms.models import Room
from congress.models import Congress
from agenda.models import TopicAgenda

#agenda that the user did from the congress agenda
class AgendaViewUser(TemplateView, LoginRequiredMixin):

    template_name = "agenda/agenda.html"
    form_class = ""
    login_url = "/"

    #def get(self, request, *args, **kwargs):

    def post(self, request, *args, **kwargs):

        username = ""
        user = ""
        #get data from the form

        if "username" in request.POST:
            username = request.POST['username']
            user = User.objects.filter(username = username, is_active = True)

        else:
            user = request.user

        professor_activity = request.POST['professor_activity']
        agenda = request.POST['agenda']

        if user:

            #validate if the user has been saved in the event
            obj_sign_up_schedule = SignUpSchedule.objects.filter(fk_user_assistent = user[0] ,active = True)
            if obj_sign_up_schedule:

                message = "usted ya esta registrado en este evento"

            else:

                obj_sign_up_schedule = SignUpSchedule()
                obj_sign_up_schedule.fk_user_created = request.user
                obj_sign_up_schedule.fk_professor_activity = professor_activity
                obj_sign_up_schedule.fk_user_assistent = user
                obj_sign_up_schedule.fk_agenda = agenda
                obj_sign_up_schedule.save()

                message = "se ha hecho la inscripcion"
        else:
            message = "este usuario no existe en la base de datos por favor registrelo"


#that is the general agenda with the topics and places
class AgendaView(TemplateView):

    template_name = "agenda/congress-agenda.html"
    form_class = ""

    def get(self, request, *args, **kwargs):

        if "load" in request.GET:

            #try:
            response_data = {}
            message = ""
            is_error = False
            list_date = []
            date = ""
            after_date = ""

            date = datetime.today()
            year = date.year
            obj_congress = Congress.objects.filter(year = year, active = True)
            congress_code = obj_congress[0].congress_code

            #obj_congress = Congress.objects.filter(congress_code = '3487ff79-7415-4317-8756-44a9c285a12c',active = True)
            obj_activity_room = ActivityRoom.objects.filter(fk_activity_code = '3487ff79-7415-4317-8756-44a9c285a12c',active = True)
            #print obj_activity_room
            for index,valActRoom in enumerate(obj_activity_room):

                activity_room_code = valActRoom.activity_room_code

                obj_topic_agenda = TopicAgenda.objects.filter(fk_activity_room_code = activity_room_code ,active = True)
                for ix_topic_agenda,val_top_agenda in enumerate(obj_topic_agenda):
                    print val_top_agenda
            """except Exception as e:

                is_error = True
                message = "error en el sistema por favor comuniquese con soporte"
                response_data['type_error'] = type(e).__name__"""

            response_data['message'] = message
            response_data['is_error'] = is_error

            response_json = json.dumps(response_data)
            content_type = 'application/json'
            return HttpResponse(response_json, content_type)
        else:

            dic = {}
            context_instance = RequestContext(request)
            template = self.template_name
            return render_to_response(template, dic,context_instance)
