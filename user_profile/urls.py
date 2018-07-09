from django.conf.urls import url
from django.urls import path

from .views import employee_create , employees_list , employee_delete , employee_update, employee_project_assign


urlpatterns = [
	url(r'^employees/$', employees_list , name = 'employees_list'),
	url(r'^employee/create/$' , employee_create , name = 'employee_create'),
	url(r'^employees/delete/$', employee_delete , name = 'employee_delete'),
	url(r'^employees/update/(?P<user_id>\d+)/$', employee_update , name = 'employee_update'),
	url(r'^employees/project/assign/(?P<user_id>\d+)/$', employee_project_assign , name = 'employee_project_assign'),
]	