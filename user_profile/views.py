from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView,CreateView,View
from django.contrib.auth.decorators import login_required

from . import send_email
from .models import  User
from project.models import ProjectEmployee, ProjectDetails


class LendingPage(TemplateView):
	template_name = "user_profile/lending_page.html"

lending_page = login_required(LendingPage.as_view())


class EmployeeCreate(CreateView):
	model = User
	fields = ['email', 'first_name', 'last_name']
	template_name = "user_profile/create_employee.html"
	success_url = reverse_lazy('home:employees_list')

	def form_valid(self, form):
		response = super(EmployeeCreate, self).form_valid(form)
		user = self.object
		user.role = "employee"
		user.manager_id = self.request.user.id
		user.save()
		send_email.send_reset_password_email('baisabhi@yopmail.com',user,True) # TODO: Need to do with allouth
		return response

employee_create = login_required(EmployeeCreate.as_view())


class Employees(ListView):
	model = User
	template_name = "user_profile/employee_list.html"

	def get_queryset(self):
		queryset = super(Employees, self).get_queryset()
		return queryset.filter(role = 'employee',manager_id=self.request.user.id)

employees_list = login_required(Employees.as_view())


class UpdateUser(UpdateView):
	model = User
	fields = ['first_name', 'last_name']
	template_name = 'user_profile/update_user.html'
	success_url=reverse_lazy('home:employees_list')

	def get_object(self, queryset=None):
		return User.objects.get(id=self.kwargs['user_id'])

employee_update = login_required(UpdateUser.as_view())


class AssignEmployeeProject(View):
	
	def get(self, request , user_id , **kwargs):
		if request.is_ajax():
			context = {}
			project_list = ProjectEmployee.objects.filter(employee_id = user_id)
			all_projects = ProjectDetails.objects.filter(manager_id = self.request.user.id)
			project_dropdown_list=all_projects.exclude(id__in=[x.project_id for x in project_list])
			context['project_list_dropdown'] = project_dropdown_list
			context['project_list'] = project_list
			return render(request, "user_profile/assign_employee_project.html", context=context)

	def post(self, request, **kwargs):
			projectemployee=ProjectEmployee(employee_id=self.kwargs['user_id'],project_id=request.POST['project_choice'])
			projectemployee.save()
			return HttpResponse()

employee_project_assign = login_required(AssignEmployeeProject.as_view())

class EmployeeDelete(View):

	def get(self, request , **kwargs):
		if request.is_ajax():
			user_id = request.GET['user_id']
			user = User.objects.get(id = user_id)
			user.delete()	
			return HttpResponse("User deleted successfully")

employee_delete = login_required(EmployeeDelete.as_view())