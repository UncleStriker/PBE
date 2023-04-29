from rest_framework.routers import DefaultRouter
from posts.api.views import PostApiViewSet, PersonaApiViewSet

router_post = DefaultRouter()

router_post.register(prefix='post', basename='post', viewset=PostApiViewSet)
router_post.register(prefix='persona', basename='persona', viewset= PersonaApiViewSet)