from django.contrib import admin
from .models import Asignatura, Alumno, Calificacion, Asistencia, Examen

# Register your models here.

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo', 'semestre',]
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['nombre','rut','direccion','telefono','email']
@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ['id_alumno','id_asignatura','id_examen','valor']
@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ['fecha','id_alumno','id_asignatura','valor',]
@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    list_display = ['numero','descripcion']
