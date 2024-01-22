from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import NewTaskForm, EditTaskForm

# Create your views here.
@login_required
def detail(request, pk):
    task =  get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/details.html', {"task": task})


@login_required
def add(request):
    if request.method == 'POST':
        submittedTaskForm = NewTaskForm(request.POST, request.FILES)
        
        if submittedTaskForm.is_valid():
            task = submittedTaskForm.save(commit=False)
            task.created_by = request.user 
            task.save()
            
            return redirect("tasks:detail", pk=task.id)
    form = NewTaskForm()
    
    return render(request, 'tasks/form.html', {'form': form})


@login_required
def edit(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditTaskForm(request.POST, request.FILES, instance=task) 

        if form.is_valid():
            form.save()
            
            return redirect('tasks:detail', pk=pk)
    
    form = EditTaskForm(instance=task)
    return render(request, "tasks/edit.html", {'form': form})
     


@login_required
def delete(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    if task:
        task.delete()
    
    return redirect('/')