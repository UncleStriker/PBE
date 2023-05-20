from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    def __str__(self):
        return self.body


class Persona(models.Model):
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    correo = models.TextField()

    def __str__(self):
        return self.body

