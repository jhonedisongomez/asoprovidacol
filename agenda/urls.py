from django.conf.urls import url
from .views import AgendaView

urlpatterns = [
    url(r'^agenda-congreso/$', AgendaView.as_view(),name='agenda_congress'),

]
