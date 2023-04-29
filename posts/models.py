from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()


class Personas(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    rut = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    codigo_postal = models.IntegerField()
    pais = models.CharField(max_length=50)
    sexo = models.CharField(max_length=15)
    nacionalidad = models.CharField(max_length=20)

class sucursal(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    fono = models.IntegerField(max_length=20)
    cantidad_trabajadores = models.IntegerField(max_length=255)
    codigo_postal = models.IntegerField()
    hora_atencion = models.TimeField()    
