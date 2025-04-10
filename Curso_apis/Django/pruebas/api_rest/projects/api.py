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