from django.conf.urls import url
from .views import ListRoomView

urlpatterns = [

    url(r'^list-rooms/$', ListRoomView.as_view(),name='list_rooms'),

]
