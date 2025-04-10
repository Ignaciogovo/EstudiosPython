python -m django --version



##### Crear un proyecto:
django-admin startproject nombre-proyecto


##### Levantar web:
python manage.py runserver


#### Estructura proyecto:
db.sqlite3 --> Base de datos para desarrollo

settings.py --> Archivo para configurar el proyecto
    Variables:
        DEBUG = True    (En desarrollo o no)
        ALLOWED_HOSTS = [] Ips permitidas
        DATABASES = {} Variable de conexión bbdd


#### Aplicaciones        
Django permite realizar aplicaciones dentro de un proyecto para ofrecer distintas tareas, como login, blog, tareas:

django-admin startapp nombre-aplicación



#### Crear tablas a partir de django:
--hacer cambios de objetos:
    python manage.py makemigrations 

-- Ejecutar las migraciones
    python manage.py migrate



Primero crear una clase en el fichero models.py de una app con esta estructura

```python
class Project(models.Model):
    name = models.CharField(max_length=200) 
```


-- Añadir la app en la variable INSTALLED_APPS de settings.py del proyecto principal

-- Hacer cambios de la app 
    python manage.py makemigrations nombre-app





#### Acceder bbdd desde la shell de django:
-- Añadir un valor:
```python
p = Project(name="aplicación movil")
# insertarlo en la base de datos 
p.save()

```
-- Listar valores de una tabla

Project.objects.all()

-- Listar un valor de la tabla
Project.objects.get(id=1)
Project.objects.get(name = "aplicación movil")


-- Listar y añadir filas que tengan esa clave foranea

-- Añadir un valor:
```python
p = Project.objects.get(id=1)
# listar todos las filas
p.nombre_objeto_set.all()
op.nombre_objeto_set.create(title = "Titulo 1")

```

-- like 'hola%' en django:
    Project.objects.filter(name__startswith="Apli")
O tambien:
```python
p = Project.objects
p.filter(name__startswith="Apli")

```

#### Listar en views.py los valores de una clase de una tabla de bbdd
```python
from django.forms.models import model_to_dict
task = get_object_or_404(Task,pk = id, user = request.user)
print(model_to_dict(task))

```


#### Pagina admin:
crear usuario para la pagina:
    python manage.py createsuperuser

añadir un objeto para añadir en la base de datos.
Dentro del admin.py de la *aplicación*:

```python
from .models import Project, Task
# Register your models here.

admin.site.register(Project)
```



#### Formularios en django:
Se crea un archivo forms.py
```python
from django import forms
class CreateNewTask():
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.Textarea(label="Descripcion tarea", required= False)

```



#### Proteger rutas logearse:
```python
from django.contrib.auth.decorators import login_required

@login_required ## Se añade delante de cada función que requiera estar logeado
def tasks(request):
        tasks = Task.objects.filter(user=request.user)
        return(render(request,'tasks.html',{
            'tasks' : tasks
        }))

```
-- Modificar archivo settings.py para redireccionar la página login:
LOGIN_URL = '/signin'


#### Conectar con mysql
 -- Se instala pymysql
 pip install pymysql

 -- Modificar __init__.py del proyecto y añadir:
```python
import pymysql
pymysql.install_as_MySQLdb()
```
 -- Modificar setting.py:
 ```python
 DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nombreDB',
            'USER': 'nombreusuario',
            'PASSWORD': 'pass',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
```