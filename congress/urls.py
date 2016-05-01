from django.conf.urls import url
from .views import CongressView


urlpatterns = [

    url(r'^congreso2016/$', CongressView.as_view(),name='congress'),


]
