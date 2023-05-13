from django.urls import path
from . import views

urlpatterns = [
    path('getPosts/', views.getPosts)
    
]
