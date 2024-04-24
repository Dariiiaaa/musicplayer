# music_player/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
from pygame import mixer

mixer.init()

def index(request):
    songs_dir = os.path.join(settings.BASE_DIR, 'static/music')  # Директорія з музичними файлами
    songs = os.listdir(songs_dir)  # Список пісень
    return render(request, 'music_player/index.html', {'songs': songs})

def play(request, song):
    song_path = os.path.join(settings.BASE_DIR, 'static/music', song)
    mixer.music.load(song_path)
    mixer.music.play()
    return HttpResponse(status=200)

def pause(request):
    mixer.music.pause()
    return HttpResponse(status=200)

def stop(request):
    mixer.music.stop()
    return HttpResponse(status=200)

def resume(request):
    mixer.music.unpause()
    return HttpResponse(status=200)


