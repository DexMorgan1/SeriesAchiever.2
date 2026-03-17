import os
import requests
import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Show, Episode

def index(request):
    shows = Show.objects.all()
    return render(request, 'tracker/index.html', {'shows': shows})

def add_show(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        query = body.get('query')
        api_key = os.environ.get('TMDB_API_KEY') 
        url = f"https://api.themoviedb.org/3/search/tv?api_key={api_key}&query={query}"
        response = requests.get(url).json()
        return JsonResponse({'results': response.get('results', [])})
    return render(request, 'tracker/add_show.html')

def mark_watched(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        episode_id = body.get('episode_id')
        episode = get_object_or_404(Episode, id=episode_id)
        episode.watched = not episode.watched 
        episode.save()
        return JsonResponse({'status': 'success', 'watched': episode.watched})
      
