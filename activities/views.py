from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
import json
from django.contrib.auth.models import User
from .models import signUpActivities, Activities
from datetime import datetime
from profiles.models import IdCard
from topics.models import ActivityRoom
from .forms import VerifySignUpForm
from agenda.models import TopicAgenda
from rooms.models import Room
from agenda.models import Agenda, SignUpSchedule

from django.contrib.auth.mixins import LoginRequiredMixin


class ActivitiesView(TemplateView):
    template_name = 'activities/activity.html'
    class_form = ""

    def get(self, request, *args, **kwargs):

        dic = {}
        context_instance = RequestContext(request)
        template = self.template_name
        return render_to_response(template, dic,context_instance)

    def post(self, request, *args, **kwargs):

        try:

            authenticated = False
            response_data = {}
            message = ""
            is_error = False

            user = request.user
            #obj_user = User.objects.filter(username = username, is_active = True)

            if user.is_authenticated():
                authenticated = True

                #activity_Code = request.POST['activity_Code']

                date = datetime.today()
                year = str(date.year)

                obj_activity = Activities.objects.filter(year = year, active = True)
                activity_code = obj_activity[0].activities_code

                obj_sign_up_activities = signUpActivities.objects.filter(fk_activities_code = activity_code,fk_user = user ,active = True)
                if obj_sign_up_activities:
                    message = "ya estas inscrito en la base de datos"

                else:
                    obj_sign_up_activities = signUpActivities()
                    sign_up_code = obj_sign_up_activities.sign_up_code
                    obj_sign_up_activities.fk_activities_code = activity_code
                    obj_sign_up_activities.fk_user = request.user
                    obj_sign_up_activities.save()

                    obj_id_card = IdCard()
                    obj_id_card.created_at = datetime.today()
                    obj_id_card.fk_user_created = request.user
                    obj_id_card.fk_sign_activity_code = sign_up_code
                    obj_id_card.save()
                    message = "se ha registrado en nuestro congreso por favor revisa la agenda"

            else:
                message = "por favor inicie sesion para regitrarte en el congreso"

        except Exception as e:

            is_error = True
            message = "error en el sistema por favor comuniquese con soporte"
            response_data['type_error'] = type(e).__name__

        response_data['message'] = message
        response_data['is_error'] = is_error

        response_json = json.dumps(response_data)
        content_type = 'application/json'
        return HttpResponse(response_json, content_type)


class VerifySignUpActivity(LoginRequiredMixin,TemplateView):

    template_name = "activities/verify-sign-up-activity.html"
    form_class = VerifySignUpForm()
    login_url = "/index/"

    def get(self,request,*args,**kwargs):

        response_data = {}
        is_error = False
        exist = False

        if 'sign_up_code' in request.GET:

            try:

                sign_up_code = request.GET['sign_up_code']
                activity_id = request.GET['activity_id']
                room_id = request.GET['room_id']
                agenda_id = request.GET['agenda_id']

                obj_room = Room.objects.filter(pk = room_id)
                room_code = obj_room[0].room_code

                obj_activities = Activities.objects.filter(pk = activity_id)
                activities_code = obj_activities[0].activities_code

                obj_agenda = Agenda.objects.filter(pk = agenda_id)
                agenda_code = obj_agenda[0].agenda_code

                obj_activity_room = ActivityRoom.objects.filter(active = True, fk_room_code = room_code, fk_activity_code = activities_code)
                if(obj_activity_room):

                    for index,valActRoom in enumerate(obj_activity_room):

                        activity_room_code = valActRoom.activity_room_code
                        obj_topic_agenda = TopicAgenda.objects.filter(active = True, fk_agenda_code = agenda_code, fk_activity_room_code = activity_room_code)
                        if(obj_topic_agenda):

                            topic_agenda_code = obj_topic_agenda[0].topic_agenda_code
                            obj_sign_up_schedule = SignUpSchedule.objects.filter(action = True , fk_sign_up_code = sign_up_code, fk_topic_agenda = topic_agenda_code)
                            
                            if(obj_sign_up_schedule):

                                message = "el asistente ha separado cupo para este evento"

                            else:

                                message = "el asistente no ha separado cupo para este evento"


            except Exception as e:

                is_error = True
                message = "error en el sistema por favor comuniquese con soporte"
                response_data['type_error'] = type(e).__name__

        else:

            dic = {'form':self.form_class}
            context_instance = RequestContext(request)
            template = self.template_name
            return render_to_response(template, dic,context_instance)

        response_data['message'] = message
        response_data['is_error'] = is_error

        response_json = json.dumps(response_data)
        content_type = 'application/json'
        return HttpResponse(response_json, content_type)
