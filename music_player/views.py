from django.shortcuts import render

def index(request):
    songs = []  # Замініть це на вашу логіку отримання списку пісень
    return render(request, 'music_player/index.html', {'songs': songs})
import os
from django.shortcuts import render, redirect
from django.conf import settings

def index(request):
    songs_dir = os.path.join(settings.BASE_DIR, 'music')  # Директорія з музичними файлами
    songs = os.listdir(songs_dir)  # Список пісень
    return render(request, 'music_player/index.html', {'songs': songs})

def upload_songs(request):
    if request.method == 'POST' and request.FILES.getlist('songs'):
        songs_dir = os.path.join(settings.BASE_DIR, 'music')
        for song_file in request.FILES.getlist('songs'):
            with open(os.path.join(songs_dir, song_file.name), 'wb+') as destination:
                for chunk in song_file.chunks():
                    destination.write(chunk)
    return redirect('index')
