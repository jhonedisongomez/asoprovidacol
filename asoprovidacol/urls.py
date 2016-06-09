from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^' , include('home.urls')),
    url(r'^' , include('congress.urls')),
    url(r'^' , include('agenda.urls')),
    url(r'^' , include('profiles.urls')),
]
