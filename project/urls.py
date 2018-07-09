from django.conf.urls import url

from .views import project_list , project_create , project_delete , project_update , project_employee_list , project_employee_delete , task_add , task , task_delete , task_update , task_employee_list , task_details , activity_status_change , task_status_change


urlpatterns=[

	url(r'^$', project_list , name = 'project_list'),
	url(r'^create', project_create , name = 'project_create'),
	url(r'^delete', project_delete ,name = 'project_delete'),
	url(r'^(?P<project_id>\d+)/update/$' , project_update , name = 'project_update'),
	url(r'^employee/list/(?P<project_id>\d+)/$', project_employee_list , name = 'project_employee_list'),
	url(r'^employee/delete/', project_employee_delete , name = 'project_employee_delete'),
	url(r'^task/add/', task_add , name = 'task_add'),
	url(r'^task/(?P<project_id>\d+)/$', task , name = 'task'),
	url(r'^task/delete/(?P<task_id>\d+)', task_delete , name = 'task_delete'),
	url(r'^task/(?P<task_id>\d+)/update/$', task_update , name = 'task_update'),
	url(r'^task/employee/list/(?P<task_id>\d+)/$', task_employee_list , name = 'task_employee_list'),
	url(r'^task/details/(?P<task_id>\d+)/$', task_details , name = 'task_details'),
	url(r'^activity/status/change/', activity_status_change , name = 'activity_status_change'),
	url(r'^task/status/change/', task_status_change , name = 'task_status_change'),


]