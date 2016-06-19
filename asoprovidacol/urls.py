from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin452039/', admin.site.urls),
    url(r'^' , include('home.urls')),
    url(r'^' , include('activities.urls')),
    url(r'^' , include('agenda.urls')),
    url(r'^asocampus/' , include('agenda.urls')),
    url(r'^' , include('profiles.urls')),
]
