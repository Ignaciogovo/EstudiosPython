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