from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
# create
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('task_list')
    else:
        form = TaskForm()
        
    return render(request, 'create_task.html', {'form': form})

# read
def task_list(request):
    task = Task.objects.all()
    
    return render(request, 'task_list.html', {'task_list': task})

# update
def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
            form.save()
            
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
        
    return render(request, 'edit_task.html', {'form': form})

# delete
def delete_task(request, pk):
    Task.objects.get(pk=pk).delete()
    
    return redirect('task_list')

# toggle complete
def toggle_complete(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = not task.completed
    task.save()
    
    return redirect('task_list')