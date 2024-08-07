from django.http import HttpResponse
from django.shortcuts import render
from todos.models import Task



def home(request):
    tasks = Task.objects.filter(is_complete=False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_complete=True).order_by('-updated_at')
    return render(request, 'home.html', context={'tasks': tasks, 'completed_tasks': completed_tasks})
