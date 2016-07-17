from django.conf.urls import url
from .views import SignUpView, SignInView, AsocampusIndex


urlpatterns = [

    #url(r'^$', IndexView.as_view(), name='index'),

	url(r'^$' , 'django.contrib.auth.views.login',
		{'template_name':'home/index.html'}, name='login'),

	url(r'^logout/$' , 'django.contrib.auth.views.logout_then_login',
		name='logout'),

	url(r'^sign-up/$' , SignUpView.as_view(),name='sign-up'),
	url(r'^sign-in/$' , SignInView.as_view(),name='sign-in'),
	url(r'asocampus/$' , AsocampusIndex.as_view(),name='asocampus'),



]
