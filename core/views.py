from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from tasks.models import Priority, Task
from .forms import SignUpForm

# Create your views here.
@login_required
def index(request):
    query = request.GET.get('query', '')
    priority = request.GET.get('priority', 0)
    tasks = Task.objects.filter(created_by=request.user)
    
    if query:
        tasks = tasks.filter(Q(title__icontains=query) | Q(description__icontains=query))
        
    if priority:
        tasks = tasks.filter(priority=priority)
    
    priority = Priority.objects.all()

    context = {
        "priorities": priority,
        "tasks": tasks,
    }
    return render(request, 'core/index.html', context)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
        
    form = SignUpForm()
    
    return render(request, 'core/register.html', {'form': form})
