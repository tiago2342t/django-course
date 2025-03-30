from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def hello(request, username):
    return HttpResponse('<h2>Hello %s</h2>' % username)

def projects(request):
    return render(request, 'projects.html')
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)

def tasks(request):
    return render(request, 'tasks.html')
    # task = Task.objects.get(title=title)
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse('Task: %s'% task.title)
