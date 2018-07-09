import pytz
from datetime import datetime,timezone,timedelta

from django.urls import reverse,reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import ProjectDetails,ProjectEmployee,Task,TaskTime
from .forms import CreateTaskForm,UpdateTaskForm
from user_profile.models import User


class Projects(ListView):

	model = ProjectDetails
	template_name = "project/projects_list.html"

	def get_queryset(self):
		queryset = super(Projects, self).get_queryset()
		if self.request.user.role == 'manager':
			return queryset.filter(manager_id = self.request.user.id)
		else:
			project_employee_obj = ProjectEmployee.objects.filter(employee_id=self.request.user.id)
			return queryset.filter(id__in=[x.project_id for x in project_employee_obj])

		
project_list = login_required(Projects.as_view())


class CreateProject(CreateView):

	model = ProjectDetails
	fields = ['title','description','start_date','end_date','status']
	template_name = "project/create_project.html"
	success_url=reverse_lazy('projects:project_list')

	def form_valid(self, form):
		response = super().form_valid(form)
		project = self.object
		project.manager_id = self.request.user.id
		project.save()
		return response
	
project_create = login_required(CreateProject.as_view())


class UpdateProject(UpdateView):

	model = ProjectDetails
	fields = ['title','description','start_date','end_date']
	template_name = 'project/update_project.html'
	success_url = reverse_lazy('projects:project_list')

	def get(self, request , project_id , **kwargs):
		self.object = ProjectDetails.objects.get(id = project_id)
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		context = self.get_context_data(object = self.object, form = form)
		return self.render_to_response(context)

	def get_object(self,queryset=None):
		return ProjectDetails.objects.get(id = self.kwargs['project_id'])

project_update = login_required(UpdateProject.as_view())


class EmployeeList(View):
	
	def get(self, request, project_id , **kwargs):
		context = {}
		project_employee_obj = ProjectEmployee.objects.filter(project_id=project_id)
		employee_all = User.objects.filter(role='employee',manager_id=self.request.user.id)
		employee_list_dropdown = employee_all.exclude(id__in = [x.employee_id for x in project_employee_obj])
		context['project_employee_obj'] = project_employee_obj
		context['employee_list_dropdown'] = employee_list_dropdown
		return render(request, "project/get_employee_list.html", context = context)

	def post(self, request, project_id , **kwargs):
		employee_choice = request.POST['employee_choice']
		projectemployee = ProjectEmployee(employee_id = employee_choice, project_id = project_id)
		projectemployee.save()
		return HttpResponse()
	

project_employee_list = login_required(EmployeeList.as_view())


class Tasks(ListView):

	model = Task
	template_name = "project/newtasks.html"
	project_id=""
	utc=pytz.UTC

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		current_date=datetime.now().date()
		task_list=[]
		d=dict()
		if self.request.user.role=="manager":
			task_list= self.get_queryset().filter(project_id=self.kwargs['project_id'])
		else:
			task_list= self.get_queryset().filter(employee_id=self.request.user.id)
			for x in task_list:
				if x.start_date <= current_date and x.end_date >= current_date:
					if x.activity == "default":
						x.activity="Play"
						x.save()
				else:
					x.activity = "default"
				start_time=""
				total_time_task=timedelta()
				if x.activity == "Started":
					tasktime=TaskTime.objects.filter(task_id=x.id).order_by('-start_time')
					for t in tasktime:
						t.total_time = datetime.now(timezone.utc)-t.start_time
						t.save()
						break
				tasktime1=TaskTime.objects.filter(task_id=x.id)
				for y in tasktime1:
						if y.total_time is not None:
							total_time_task=total_time_task+y.total_time
				d[x.id]=total_time_task
		todo_list=[]
		doing_list=[]
		done_list=[]
		for x in task_list:
			if x.status=='Todo':
				todo_list.append(x)
			elif x.status=='Doing':
				doing_list.append(x)
			else:
				done_list.append(x)
		project_id=self.kwargs['project_id']
		context['project_id']=self.kwargs['project_id']
		context['todo_list']=todo_list
		context['doing_list']=doing_list
		context['done_list']=done_list
		context['total_time']=d
		return context
		
task = login_required(Tasks.as_view())


class UpdateTask(UpdateView):

	model = Task
	form_class = UpdateTaskForm
	template_name = 'project/update_task.html'
		
	def get_object(self,queryset=None):
		return Task.objects.get(id=self.kwargs['task_id'])

	def get_success_url(self):
		return reverse('projects:task',kwargs={'project_id':self.kwargs['task_id']})

task_update = login_required(UpdateTask.as_view())


class EmployeeTaskList(View):
	
	def get(self, request, **kwargs):
		taskid=self.kwargs['task_id']
		task_obj=Task.objects.get(id=taskid)
		project_id=task_obj.project_id
		context = {}
		employee_project=ProjectEmployee.objects.filter(project_id=project_id)
		employee_project_list=[]
		for x in employee_project:
			employee_project_list.append(x.employee)
		employee_task=task_obj.employee
		if employee_task is not None:
			employee_project_list.remove(employee_task)
		context['employee_project_list']=employee_project_list
		if task_obj.employee is not None:
			context['selected_employee']=task_obj.employee.get_full_name()
		return render(request, "project/get_employee_task_list.html", context=context)

	def post(self, request , task_id , **kwargs):
		if request.method == 'POST':
			employee_choice=request.POST.get('employee_choice')
			task = Task.objects.get(id = task_id)
			task.employee_id=employee_choice
			task.save()
			return HttpResponse()
		else:
			HttpResponse()

task_employee_list = login_required(EmployeeTaskList.as_view())


class AddTask(CreateView):

	model = Task
	form_class=	CreateTaskForm
	template_name = "project/add_task.html"

	def form_valid(self, form):
		response = super().form_valid(form)
		task = self.object
		task.status=self.request.POST.get('status')
		task.project_id=self.request.POST.get('project_id')
		task.save()
		return response

	def get_success_url(self):
		return reverse('projects:task', kwargs={'project_id':self.request.POST.get('project_id')})

task_add = login_required(AddTask.as_view())


class TaskDetails(View):

	def get(self, request, task_id ,  **kwargs):
		task_obj=Task.objects.get(id = task_id)
		context={}
		context['task']=task_obj
		return render(request, "project/show_task_details.html", context=context)

task_details = login_required(TaskDetails.as_view())


class TaskDelete(View):

	def get(self, request , task_id , **kwargs):
		if request.is_ajax():
			try:
				task = Task.objects.get(id = task_id)
			except Task.DoesNotExist:
				return HttpResponse("Task does not exist")
			task.delete()    
			return HttpResponse("Task deleted successfully")

task_delete	= login_required(TaskDelete.as_view())

class TaskStatusChange(View):

	def get(self , request , **kwargs ):
		task_obj = Task.objects.get(id = self.request.GET.get('task_id') )
		task_obj.status  = self.request.GET.get('status')
		task_obj.save()
		return HttpResponse("SUCCESS")	


task_status_change = login_required(TaskStatusChange.as_view())

def project_delete(request):

	if request.is_ajax():
		project_id = request.GET['project_id']
		try:
			project = ProjectDetails.objects.get(id=project_id)
		except ProjectDetails.DoesNotExist:
			return HttpResponse("Project does not exist")
		project.delete()    
		return HttpResponse("Project deleted successfully")


def project_employee_delete(request):
	if request.is_ajax():
		project_id = request.GET['project_id']
		employee_id=request.GET['employee_id']
		project = ProjectEmployee.objects.get(employee_id=employee_id,project_id=project_id)
		project.delete()    
		return HttpResponse("Employee deleted successfully")


def activity_status_change(request):
	utc=pytz.UTC

	if request.is_ajax():
		task_id = request.GET.get('task_id')
		task={}
		try:
			task = Task.objects.get(id=task_id)
		except Task.DoesNotExist:
			return HttpResponse("Task does not exist")
		task.activity = request.GET['activity_status']
		task.save()
		if task.activity == "Started":
			tasktime=TaskTime(task_id=task_id,start_time=datetime.now(timezone.utc))
			tasktime.save()
		if task.activity == "Play":
			tasktime=TaskTime.objects.filter(task_id=task_id).order_by('-start_time')
			for x in tasktime:
				x.end_time=datetime.now(timezone.utc)
				x.total_time=x.end_time-x.start_time
				x.save()
				break
		return HttpResponse()

