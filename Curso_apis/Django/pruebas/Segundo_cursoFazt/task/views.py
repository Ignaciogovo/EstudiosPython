from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Formulario para crear usuario
from django.contrib.auth.models import User  # Objeto de usuario
from django.contrib.auth import login, logout,authenticate # Genera una cookie para mantener la sesión del usuario
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return(render(request,'home.html'))



def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form' : UserCreationForm(),
            'mss': ''
        })
    else:
        if request.POST['password2'] == request.POST['password1']:
            try:
                # Registrar usuario:
                user = User.objects.create_user(username = request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return(redirect(tasks))
            except:
                return render(request, 'signup.html', {
                    'form' : UserCreationForm(),
                    'mss': 'Usuario ya creado'
                })
        else:
            return render(request, 'signup.html', {
                'form' : UserCreationForm(),
                'mss': 'Las contraseñas no coinciden'
            })


@login_required
def tasks(request):
        tasks = Task.objects.filter(user=request.user)
        return(render(request,'tasks.html',{
            'tasks' : tasks
        }))


@login_required
def signout(request):
    logout(request)
    return(redirect(home))


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form' : AuthenticationForm(),
            'mss': ''
        })
    else:
        user = authenticate( request, username = request.POST["username"], password = request.POST["password"])

        if user is not None:
            try:
                login(request,user)
                return(redirect(tasks))
            except:
                return render(request, 'signin.html', {
                    'form' : AuthenticationForm(),
                    'mss': 'Error con el usuario'
                })
        else:
            return render(request, 'signin.html', {
                'form' : AuthenticationForm(),
                'mss': 'Usuario o contraseña es incorrecto'
            })



#CREATE
@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form' : TaskForm(),
            'mss': ''
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return(redirect(tasks))
        except:
            return render(request, 'create_task.html', {
                'form' : TaskForm(),
                'mss': 'Error al crear tarea'
            })

# UPDATE
@login_required
def task_detail(request,id):
    if request.method == 'GET':
        task = get_object_or_404(Task,pk = id, user = request.user)
        form = TaskForm(instance=task)
        return(render(request,'task_detail.html',{
            'task': task,
            'form' : form
        }))
    else:
        task = get_object_or_404(Task,pk = id, user = request.user)
        form = TaskForm(request.POST,instance=task)
        form.save()
        return(redirect(tasks))
    
@login_required
def task_completed(request,id):
    task = get_object_or_404(Task,pk = id, user = request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return(redirect(tasks))

        
@login_required
def task_deleted(request,id):
    task = get_object_or_404(Task,pk = id, user = request.user)
    if request.method == 'POST':
        task.delete()
        return(redirect(tasks))
        