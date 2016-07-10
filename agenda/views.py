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
from activities.models import Activities,signUpActivities
from agenda.models import TopicAgenda
from .forms import CreateAgendaForm

from django.db.models import Count
from country.models import section

def reservarCupo(self):

    response_data = {}
    is_error = False
    message = ""

    try:

        user = self.request.user

        if user.is_authenticated():

            agenda = self.request.POST['agendaId']
            obj_topic_agenda = TopicAgenda.objects.filter(pk = agenda)

            fk_activity_room_code = obj_topic_agenda[0].fk_activity_room_code
            obj_activity_room = ActivityRoom.objects.filter(activity_room_code = fk_activity_room_code,active = True)
            room_code = obj_activity_room[0].fk_room_code

            obj_room = Room.objects.filter(room_code = room_code,active = True)
            capacity = obj_room[0].capacity

            topic_agenda_code = obj_topic_agenda[0].topic_agenda_code

            date = datetime.today()
            year = date.year

            obj_activities = Activities.objects.filter(year = year, active = True)
            activities_code = obj_activities[0].activities_code

            obj_sign_up_activities = signUpActivities.objects.filter(active = True,fk_activities_code = activities_code,fk_user = user)

            if obj_sign_up_activities:

                sign_up_code = obj_sign_up_activities[0].sign_up_code

                obj_signUpSchedule = SignUpSchedule.objects.filter(action = True, fk_topic_agenda = topic_agenda_code,fk_sign_up_code = sign_up_code)
                if obj_signUpSchedule:

                    message = "usted ya se inscribio a esta actividad por favor eliga otra"
                else:
                    obj_signUpSchedule = SignUpSchedule.objects.filter(fk_topic_agenda = topic_agenda_code)
                    if obj_signUpSchedule:

                        obj_signUpSchedule = SignUpSchedule.objects.filter(fk_topic_agenda = topic_agenda_code).order_by('-id')[0]
                        count_sign_up = obj_signUpSchedule.count
                        count_sign_up = len(count_sign_up)

                        if count_sign_up == capacity:

                            message = "no se puede inscribir a esta actividad, no hay cupos"
                        else:

                            count_sign_up = obj_signUpSchedule.count
                            count_sign_up = list(count_sign_up)
                            count_sign_up.append(str(len(count_sign_up) + 1))
                            count_sign_up = str(count_sign_up)

                            obj_signUpSchedule = SignUpSchedule()
                            obj_signUpSchedule.count = count_sign_up
                            obj_signUpSchedule.fk_user_created = user
                            obj_signUpSchedule.fk_sign_up_code = sign_up_code
                            obj_signUpSchedule.fk_topic_agenda = topic_agenda_code
                            obj_signUpSchedule.save()

                            message = "se ha separado el cupo para este evento"
                    else:

                        count_sign_up = ['1']
                        count_sign_up = str(count_sign_up)

                        obj_signUpSchedule = SignUpSchedule()
                        obj_signUpSchedule.count = count_sign_up
                        obj_signUpSchedule.fk_user_created = user
                        obj_signUpSchedule.fk_sign_up_code = sign_up_code
                        obj_signUpSchedule.fk_topic_agenda = topic_agenda_code
                        obj_signUpSchedule.save()

                        message = "se ha separado el cupo para este evento"
            else:
                message = "usted no esta inscrito al evento por favor realize esta accion para separar los cupos"
        else:

            message = "por favor inicia sesion o registrate para separar el cupo"
    except Exception as e:

        is_error = True
        message = "error en reservar cupo, por favor comuniquese con soporte"
        response_data['type_error'] = type(e).__name__

    response_data['message'] = message
    response_data['is_error'] = is_error

    #response_json = json.dumps(response_data)
    #content_type = 'application/json'
    return response_data#HttpResponse(response_json, content_type)


def cancelarCupo(self):

    response_data = {}
    is_error = False
    message = ""

    try:

        user = self.request.user

        agenda = self.request.POST['agendaId']
        obj_topic_agenda = TopicAgenda.objects.filter(pk = agenda)
        topic_agenda_code = obj_topic_agenda[0].topic_agenda_code

        if user.is_authenticated():

            obj_sign_up_activities = signUpActivities.objects.filter(active = True,fk_user = user)
            sign_up_code = obj_sign_up_activities[0].sign_up_code
            obj_signUpSchedule = SignUpSchedule.objects.filter(action = True,fk_topic_agenda = topic_agenda_code, fk_sign_up_code = sign_up_code)

            if obj_signUpSchedule:

                obj_signUpScheduleCount = SignUpSchedule.objects.filter(fk_topic_agenda = topic_agenda_code).order_by('-id')[0]
                count_sign_up = obj_signUpScheduleCount.count
                count_sign_up = list(count_sign_up)
                count_sign_up.pop()
                count_sign_up = str(count_sign_up)

                obj_signUpSchedule[0].action = False
                obj_signUpSchedule[0].save(update_fields =['action'])

                obj_signUpSchedule = SignUpSchedule()
                obj_signUpSchedule.count
                obj_signUpSchedule.action = False
                obj_signUpSchedule.fk_sign_up_code = sign_up_code
                obj_signUpSchedule.fk_topic_agenda = topic_agenda_code
                obj_signUpSchedule.fk_user_created = user
                obj_signUpSchedule.save()
                message = "ha cancelado el cupo para esta actividad"
            else:
                message = "usted no tiene cupo separado para esta actividad"
        else:

            message = "por favor inicia sesion para cancelar algun cupo"

    except Exception as e:

        is_error = True
        message = "error en cancelar cupo, por favor comuniquese con soporte"
        response_data['type_error'] = type(e).__name__

    response_data['message'] = message
    response_data['is_error'] = is_error
    return response_data

#agenda that the user did from the activities agenda
class AgendaViewUser(TemplateView, LoginRequiredMixin):

    template_name = "agenda/activities-agenda.html"
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

        response_json = json.dumps(response_data)
        content_type = 'application/json'
        HttpResponse(response_json, content_type)


#that is the general agenda with the topics and places
class AgendaView(TemplateView):

    template_name = "agenda/activities-agenda.html"
    form_class = ""

    def get(self, request, *args, **kwargs):

        if "load" in request.GET:

            try:
                response_data = {}
                message = ""
                is_error = False
                list_town = {}
                dates = []
                list_date = {}
                after_date = ""
                list_time = {}
                times = []
                schedules = []
                list_agenda = {}
                agendas = []

                date = datetime.today()
                year = date.year
                obj_activities = Activities.objects.filter(year = year, active = True)
                activities_code = obj_activities[0].activities_code

                obj_activity_room = ActivityRoom.objects.filter(fk_activity_code = activities_code,active = True).values('fk_room_code').annotate(counter = Count('fk_room_code'))

                for ix_act_room, act_room in enumerate(obj_activity_room):

                    list_town = {}
                    dates = []
                    times = []

                    counter =  act_room['counter']#count the activicy for each topic

                    room_code = act_room['fk_room_code']

                    obj_room = Room.objects.filter(room_code = room_code,active = True)
                    room_name = obj_room[0].room_name
                    capacity = obj_room[0].capacity

                    section_code = obj_room[0].fk_section_code

                    obj_section = section.objects.filter(section_code = section_code, active = True)
                    town = obj_section[0].section_name

                    list_town['town'] = town

                    obj_activity_room = ActivityRoom.objects.filter(fk_room_code = room_code , active = True)

                    for ix_act_room,val_act_room in enumerate(obj_activity_room):
                        list_date = {}

                        activity_room_code = val_act_room.activity_room_code
                        topic_code = val_act_room.fk_topic_code
                        obj_topic = Topic.objects.filter(topic_code = topic_code,active = True)
                        topic_name = obj_topic[0].topic_name

                        list_date['topic'] = topic_name

                        obj_topic_agenda = TopicAgenda.objects.filter(fk_activity_room_code = activity_room_code,active = True)
                        agenda_topic_pk = obj_topic_agenda[0].pk
                        topic_agenda_code = obj_topic_agenda[0].topic_agenda_code
                        agenda_code = obj_topic_agenda[0].fk_agenda_code

                        obj_agenda = Agenda.objects.filter(agenda_code = agenda_code ,active = True)
                        obj_signUpSchedule = SignUpSchedule.objects.filter(action = True, fk_topic_agenda = topic_agenda_code)
                        if obj_signUpSchedule:

                            obj_signUpSchedule = SignUpSchedule.objects.filter(action = True, fk_topic_agenda = topic_agenda_code).order_by('-id')[0]

                            place = obj_signUpSchedule.count
                            place = eval(place)
                            place = len(place)

                        else:
                            place = 0

                        place = capacity - place

                    date = str(obj_agenda[0].date)
                    time = obj_agenda[0].schedule

                    list_date['date'] = date
                    list_date['time'] = time
                    list_date['agendaPk'] = agenda_topic_pk
                    list_date['room_name'] = room_name
                    list_date['places'] = place
                    dates.append(list_date)

                    after_date = date
                list_town['schedule'] = dates
                list_time = {}

                schedules.append(list_town)

            except Exception as e:

                is_error = True
                message = "error en el sistema por favor comuniquese con soporte"
                response_data['type_error'] = type(e).__name__

            response_data['message'] = message
            response_data['is_error'] = is_error
            response_data['list_schedule'] = schedules


            response_json = json.dumps(response_data)
            content_type = 'application/json'
            return HttpResponse(response_json, content_type)
        else:

            dic = {}
            context_instance = RequestContext(request)
            template = self.template_name
            return render_to_response(template, dic,context_instance)

    def post(self, request, *args, **kwargs):

        response_data = {}
        method = self.request.POST['method']

        response_data = eval(method + "Cupo(self)")
        content_type = 'application/json'
        response_json = json.dumps(response_data)
        return HttpResponse(response_json, content_type)

class CreateDateView(TemplateView, LoginRequiredMixin):

    template_name = "agenda/create-date.html"
    login_url = "/"
    form_class = ""

    def get(self, request, *args, ** kwargs):

        dic = {}
        context_instance = RequestContext(request)
        template = self.template_name
        return render_to_response(template, dic,context_instance)

    def post(self, request, *args, **kwargs):

        try:

            response_data = {}
            message = ""
            is_error = False

            user = request.user
            time = request.POST['time']
            date = request.POST['date']

            date = datetime.strptime(date , "%Y-%m-%d")

            obj_agenda = Agenda()
            obj_agenda.schedule = time
            obj_agenda.date = date
            obj_agenda.fk_user_created = user
            obj_agenda.save()

            message = "se ha guardado la nueva fecha en la base de datos"

        except Exception as e:

            is_error = True
            message = "Error en el sistema guardando los datos, por favor comuniquese con soporte"
            response_data['type_error'] = type(e).__name__

        response_data['message'] = message
        response_data['is_error'] = is_error


        response_json = json.dumps(response_data)
        content_type = 'application/json'
        return HttpResponse(response_json, content_type)

class CreateAgendaView(TemplateView, LoginRequiredMixin):

    template_name = "agenda/create-agenda.html"
    form_class = CreateAgendaForm()
    login_url = "/"

    def get(self, request, *args, **kwargs):

        dic = {'form': self.form_class}
        context_instance = RequestContext(request)
        template = self.template_name
        return render_to_response(template, dic,context_instance)


    def post(self, request, *args, **kwargs):

        try:

            response_data = {}
            message = ""
            is_error = False

            agenda_pk = request.POST['agenda_pk']
            obj_agenda = Agenda.objects.filter(pk = agenda_pk)
            agenda_code = obj_agenda[0].agenda_code

            activity_room_pk = request.POST['activity_room_pk']
            obj_activity_room = ActivityRoom.objects.filter(pk = activity_room_pk)
            activity_room_code = obj_activity_room[0].activity_room_code

            user = request.user
            obj_topic_agenda = TopicAgenda()
            obj_topic_agenda.fk_agenda_code = agenda_code
            obj_topic_agenda.fk_activity_room_code = activity_room_code
            obj_topic_agenda.fk_user_created = user
            obj_topic_agenda.save()

            message = "se ha guardado en la base de datos"

        except Exception as e:

            is_error = True
            message = "Error en el sistema guardando los datos, por favor comuniquese con soporte"
            response_data['type_error'] = type(e).__name__

        response_data['message'] = message
        response_data['is_error'] = is_error


        response_json = json.dumps(response_data)
        content_type = 'application/json'
        return HttpResponse(response_json, content_type)

class ListScheduleView(TemplateView):

    template_name = "activities/verify-sign-up-activity.html"
    form_class = ""

    def get(self, request, *args, **kwargs):

        message = ""
        is_error = False
        response_data = {}
        list_agenda = []
        try:

            room_id = request.GET['room_pk']

            obj_room = Room.objects.filter(pk = room_id)
            room_code = obj_room[0].room_code

            obj_activity_room = ActivityRoom.objects.filter(active = True, fk_room_code = room_code)
            if(obj_activity_room):

                for index,valActRoom in enumerate(obj_activity_room):

                    agenda_data = {}
                    activity_room_code = valActRoom.activity_room_code
                    print activity_room_code
                    obj_topic_agenda = TopicAgenda.objects.filter(active = True, fk_activity_room_code = activity_room_code)
                    print obj_topic_agenda
                    agenda_code = obj_topic_agenda[0].fk_agenda_code
                    obj_agenda = Agenda.objects.filter(agenda_code = agenda_code, active = True)

                    date = str(obj_agenda[0].date) + "/" + str(obj_agenda[0].schedule)
                    agenda_data['agenda_pk'] = obj_agenda[0].pk
                    agenda_data['date'] = date
                    list_agenda.append(agenda_data)

            else:


                message = "no existen datos"

        except Exception as e:

            is_error = True
            message = "error en el sistema listando los horarios, por favor comuniquese con soporte"
            response_data['type_error'] = type(e).__name__

        response_data['message'] = message
        response_data['is_error'] = is_error
        response_data['list_agenda'] = list_agenda


        response_json = json.dumps(response_data)
        content_type = 'application/json'
        return HttpResponse(response_json, content_type)
