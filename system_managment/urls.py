from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from user_profile.views import lending_page


urlpatterns = [
	url(r'^$' , lending_page , name = 'lending_page'),
	url(r'^profile/' , include(('user_profile.urls','home') , namespace = 'home')),
	url(r'^accounts/' , include('allauth.urls')),
	url(r'^projects/' , include(('project.urls','project'), namespace = 'projects')),
	url(r'^admin/', admin.site.urls),
]