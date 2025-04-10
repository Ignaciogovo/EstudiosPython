from rest_framework import routers
from .api import ProjectViewSet


# Crea un router para gestionar las rutas de la API
router = routers.DefaultRouter()
# Registra la vista del modelo Project en la URL 'api/projects'
router.register('api/projects', ProjectViewSet, 'projects')

# Asigna las rutas generadas automáticamente por el router
urlpatterns = router.urls
