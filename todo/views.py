from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            return redirect('index')
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)

def complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('index')

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('index')

