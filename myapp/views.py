from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask

# Create your views here.
def index(request):
    title = 'Django course!!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'santi'
    return render(request, 'about.html', {
        'username': username
    })

def hello(request, username):
    return HttpResponse('<h2>Hello %s</h2>' % username)

def projects(request):
    # projects = list(Project.objects.values())
    projects=Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })
    # return JsonResponse(projects, safe=False)

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })
    
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('/tasks/')
