from django.conf.urls import url
from .views import AgendaView, CreateDateView

urlpatterns = [
    url(r'^agenda-congreso/$', AgendaView.as_view(),name='agenda_congress'),
    url(r'crear-fecha/$', CreateDateView.as_view(),name='create-agenda'),


]
