from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
import json
from django.contrib.auth.models import User
from .models import signUpCongress, Congress
from datetime import datetime
from profiles.models import IdCard


class CongressView(TemplateView):
    template_name = 'congress/congress.html'
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

                date = datetime.today()
                year = str(date.year)

                obj_congress = Congress.objects.filter(year = year, active = True)
                congress_code = obj_congress[0].congress_code

                obj_sign_up_congress = signUpCongress.objects.filter(fk_congress_code = congress_code,fk_user = user ,active = True)
                if obj_sign_up_congress:
                    message = "ya estas inscrito en la base de datos"

                else:
                    obj_sign_up_congress = signUpCongress()
                    sign_up_code = obj_sign_up_congress.sign_up_code
                    obj_sign_up_congress.fk_congress_code = congress_code
                    obj_sign_up_congress.fk_user = request.user
                    obj_sign_up_congress.save()

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
