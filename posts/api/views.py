from rest_framework.viewsets import ModelViewSet
from posts.models import Post, Personas 
from posts.api.serializers import PostSerializer, PersonaSerializer

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PersonaApiViewSet(ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = Personas.objects.all()