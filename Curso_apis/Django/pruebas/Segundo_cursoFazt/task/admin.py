from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin): ## Para poder ver el valor de create en la pagina admin
    readonly_fields = ("created",) # readonly_fields: solo lectura no se puede editar

admin.site.register(Task,TaskAdmin)