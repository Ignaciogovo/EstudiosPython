from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200) # 

    def __str__(self): # Nombramos de forma automatica el objeto con el valor de name
        return(self.name)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    Project = models.ForeignKey(Project, on_delete=models.CASCADE) # clave foranea, si hace on_delete modo cascada si se borra un proyecto se borra una cascada
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.title + " - " + self.Project.name