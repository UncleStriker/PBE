from django.db import models

# Create your models here.


class Asignatura(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=20)
    semestre = models.IntegerField()
    def __str__(self):
        return(self.body)
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=13)
    email = models.CharField(max_length=50)
    def __str__(self):
        return(self.body)

class Calificacion(models.Model):
    id_alumno = models.BigIntegerField()
    id_asignatura = models.BigIntegerField()
    id_examen = models.BigIntegerField()
    valor = models.IntegerField()
    def __str__(self):
        return(self.body)

class Asistencia(models.Model):
    fecha = models.DateTimeField()
    id_alumno = models.BigIntegerField()
    id_asignatura = models.BigIntegerField()
    valor = models.IntegerField()
    def __str__(self):
        return(self.body)
    
class Examen(models.Model):
    numero = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return(self.body)
