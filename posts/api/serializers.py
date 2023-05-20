from rest_framework.serializers import ModelSerializer
from posts.models import Post 
from posts.models import Persona

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','content']

class PersonaSerializer(ModelSerializer):
    class Meta:
        model = Persona
        fields =  ['nombre','apellido','rut','correo',]