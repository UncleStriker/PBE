from django.contrib import admin
from posts.models import Post, Personas
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    lis_display = ['id', 'title']

@admin.register(Personas)
class PersonaAdmin(admin.ModelAdmin):
    lis_display = ['id',
                    'nombre',
                    'apellidos',
                    'rut',
                    'direccion',
                    'ciudad',
                    'fecha_nacimiento',
                    'codigo_postal',
                    'pais',
                    'sexo',
                    'nacionalidad']