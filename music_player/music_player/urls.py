# music_player/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play/<str:song>/', views.play, name='play'),
    path('pause/', views.pause, name='pause'),
    path('stop/', views.stop, name='stop'),
    path('resume/', views.resume, name='resume'),
   
]
