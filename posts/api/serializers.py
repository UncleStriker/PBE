from rest_framework.serializers import ModelSerializer
from posts.models import Post, Personas

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','content']

class PersonaSerializer(ModelSerializer):
    class Meta:
        model = Personas
        fields = ['id',
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
