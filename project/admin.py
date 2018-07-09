from django.contrib import admin

from project.models import ProjectDetails, ProjectEmployee,Task,TaskTime


admin.site.register(ProjectDetails)
admin.site.register(ProjectEmployee)
admin.site.register(Task)
admin.site.register(TaskTime)