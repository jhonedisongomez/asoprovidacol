from django.conf.urls import url
from .views import SignUpView


urlpatterns = [

    #url(r'^$', IndexView.as_view(), name='index'),

	url(r'^$' , 'django.contrib.auth.views.login',
		{'template_name':'home/index.html'}, name='login'),

	url(r'^logout/$' , 'django.contrib.auth.views.logout_then_login',
		name='logout'),

	url(r'^sign-up/$' , SignUpView.as_view(),name='sign-up'),

]
