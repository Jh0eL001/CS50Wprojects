from django.shortcuts import render
from django import forms
tasks = ['Task 1', 'Task 2', 'Task 3',]
# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
def index(request):
    return render(request, 'tasks/index.html', {
        'tasks': tasks  
    })

def add(request):
    return render(request, 'tasks/add.html')