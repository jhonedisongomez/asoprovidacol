from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
import json

class IndexView(TemplateView):
    template_name = 'home/index.html'

class SignUpView(TemplateView):
    template_name = "home/sign-up-form.html"
    form_class = ""

class SignInView(TemplateView):
    template_name = "home/sign-in-form.html"
    form_class = ""

    def get(self, request, *args, **kwargs):

        if "username" in request.GET:
            try:

                message = ""
                is_error = False
                authenticated = False

                response_data = {}
                username = request.GET['username']
                password = request.GET['password']

                user = authenticate(username = username, password = password)

                if user is not None:

                    if user.is_active:
                        message = "bienvenido a nuestra plataforma"
                        authenticated = True
                        login(request, user)

                    else:
                        message = "este usuario esta desactivado por favor comuniquese con soporte"
                else:
                    message = "este usuario no existe en la base de datos"
            except Exception as e:

                is_error = True
                message = "error en el sistema por favor comuniquese con soporte"
                response_data['type_error'] = type(e).__name__

            response_data['authenticated'] = authenticated
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
