from rest_framework.viewsets import ModelViewSet
from posts.models import Post,Persona
from posts.api.serializers import PostSerializer,PersonaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

@api_view(['GET'])
def getPosts(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addPost(request):
    data = request.data
    post = Post.objects.create(
        title = data['title'],
        content = data['content']
    )
    serializer = PostSerializer(post, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def addPersona(request):
    data = request.data
    persona = Persona.objects.create(
        nombre = data['nombre'],
        apellido = data['apellido'],
        rut = data['rut'],
        correo = data['correo']
    )


@api_view(['PUT'])
def updatePost(request):
    data = request.data
    post = Post.objects.get(id = data['id'])
    serializer = PostSerializer(instance = post, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)