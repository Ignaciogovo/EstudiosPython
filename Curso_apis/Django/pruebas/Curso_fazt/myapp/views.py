from django.http import HttpResponse,JsonResponse
from .models import Task, Project
from django.shortcuts import get_object_or_404,render
from .forms import CreateNewTask
# Create your views here.
def hello(request):
    title = 'Django course!'
    return(render(request,'index.html',{
        'titulo' : title
        }))



def projects(request):
    project = Project.objects.all()
    return(render(request,'projects.html',{
        'projects' : project
        }))


def project(request,id):
    project = get_object_or_404(Project,id = id)
    return(HttpResponse('proyecto: %s' % project.name) )


def tasks(request):
    tasks = Task.objects.all()
    return(render(request,'tasks.html',{
        'tasks' : tasks
        }))



def create_task(request):
    print(request.GET['title'])
    return( render(request,'create_task.html',{
                       'form': CreateNewTask()
                   }))