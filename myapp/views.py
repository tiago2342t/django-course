from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render

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
    # task = Task.objects.get(title=title)
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse('Task: %s'% task.title)
