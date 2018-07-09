from django.forms import ModelForm, Textarea
from .models import Task


class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'start_date','end_date')
        widgets = {
            'description': Textarea(attrs={'cols': 29, 'rows': 7}),
        }
class UpdateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'start_date','end_date','status')
        widgets = {
            'description': Textarea(attrs={'cols': 29, 'rows': 7}),
        }