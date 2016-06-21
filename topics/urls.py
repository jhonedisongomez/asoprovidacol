from django.conf.urls import url
from .views import CreateActivity


urlpatterns = [

    url(r'^crear-actividad-por-tema/$', CreateActivity.as_view(),name='create-activity-thopic'),



]
