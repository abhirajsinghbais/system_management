from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _



from project import choices
from user_profile.models import User



class ProjectDetails(models.Model):
	title = models.CharField(_('title'), max_length=30,blank=False)
	description = models.CharField( _('description'), max_length=200,blank=False)
	status = models.CharField(_('status'), max_length=30, blank=False, choices=choices.STATUS_CHOICES)
	start_date = models.DateField(_('start_date'),blank=True)
	end_date = models.DateField(_('end_date'),blank=True)
	manager = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

class ProjectEmployee(models.Model):
	employee = models.ForeignKey(User, on_delete=models.CASCADE)
	project = models.ForeignKey(ProjectDetails, on_delete=models.CASCADE)

class Task(models.Model):
	title = models.CharField(_('title'), max_length=30,blank=False)
	description = models.CharField( _('description'), max_length=200,blank=False)
	status = models.CharField(_('status'), max_length=30, blank=False, choices=choices.STATUS_CHOICES)
	start_date = models.DateField(_('start_date'),blank=True)
	end_date = models.DateField(_('end_date'),blank=True)
	project = models.ForeignKey(ProjectDetails, on_delete=models.CASCADE,null=True)
	employee= models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	activity = models.CharField( _('activity'), max_length=30,blank=True,choices=choices.ACTIVITY_CHOICES,default=choices.ACTIVITY_CHOICES[0][0])

class TaskTime(models.Model):
	task = models.ForeignKey(Task, on_delete=models.CASCADE,null=True)
	start_time=models.DateTimeField(_('start_time'),blank=True,null=True)
	end_time=models.DateTimeField(_('end_time'),blank=True,null=True)
	total_time=models.DurationField(_('total_time'),blank=True,null=True)

