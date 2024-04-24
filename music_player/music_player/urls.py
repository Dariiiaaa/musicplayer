from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_songs/', views.upload_songs, name='upload_songs'),
]
