from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.api.serializers import PostSerializer
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