from django.shortcuts import render, redirect, get_object_or_404

from .models import Category, Tasks
from .forms import TasksForm

def task_list(request):
    tasks = Tasks.objects.all()
    return render(request, 'task/task_list.html', {'tasks':tasks})

def add_tasks(request):
    if request.method == 'POST':
        form= TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form= TasksForm()
    return render(request, 'task/add_task.html', {'form': form})


def completed_task(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id)
    if not task.is_completed:
        task.is_completed = True
        task.save()
    return redirect('task_list')