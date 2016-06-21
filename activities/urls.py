from django.conf.urls import url
from .views import ActivitiesView


urlpatterns = [

    url(r'^activities/$', ActivitiesView.as_view(),name='activities'),



]
