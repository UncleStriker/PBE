from django.urls import path
from . import views

urlpatterns = [
    path('getPosts/', views.getPosts),
    path('addPost/', views.addPost),
    path('addPersona/', views.addPersona),
    path('updatePost/', views.updatePost)
    
    
]
