#### Instalación:
pip install djangorestframework


#### Configuración:
añadir en setting.py la app:

```python
INSTALLED_APPS = [
    'rest_framework'
]
``` 


#### archivo serializers.py
Convierte los objetos Project en JSON y viceversa, permitiendo que los datos se transmitan a través de la API.

```python
from rest_framework import serializers
from .models import Project

# Serializador para transformar el modelo Project a JSON
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # Define los campos a incluir en la representación JSON
        fields = ('id', 'title', 'description', 'technology', 'create_at')
        # Hace que el campo 'created_at' sea de solo lectura
        read_only_fields = ('create_at',)
```


#### archivo api:
Crea una vista basada en ModelViewSet, que gestiona las operaciones CRUD sobre el modelo Project.
```python
from .models import Project
from rest_framework import viewsets,permissions
from .serializers import ProjectSerializer


# Vista basada en ViewSet para la API de Project
class ProjectViewSet(viewsets.ModelViewSet):
    # Consulta todos los objetos de la base de datos
    queryset = Project.objects.all()
    # Permite el acceso a cualquier usuario sin restricciones
    permission_classes = [permissions.AllowAny]
    # Especifica el serializador que se usará para transformar los datos
    serializer_class = ProjectSerializer
```


#### Archivo urls.py (Dentro de la app)
Configura las rutas de la API utilizando un router, permitiendo acceder a los endpoints de Project.
```python
from rest_framework import routers
from .api import ProjectViewSet


# Crea un router para gestionar las rutas de la API
router = routers.DefaultRouter()
# Registra la vista del modelo Project en la URL 'api/projects'
router.register('api/projects', ProjectViewSet, 'projects')

# Asigna las rutas generadas automáticamente por el router
urlpatterns = router.urls
```


#### Significado de CRUD
- **POST** → Crea un nuevo registro.  
- **GET** → Obtiene uno o varios registros.  
- **PUT** → Actualiza **todo** el registro, sobrescribiendo los datos.  
- **PATCH** → Actualiza **parcialmente** un registro, modificando solo los campos enviados.  
- **DELETE** → Elimina un registro.