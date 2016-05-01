from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
import json
from django.contrib.auth.models import User

class CongressView(TemplateView):
    template_name = 'congress/congress.html'
