import interface.news_handler
import interface.score_handler
from interface.config import API_KEY, SOURCES, TERMS
from django.shortcuts import render


# Create your views here.

def index(request):
    data = {}
    return render(request, 'index.html', data)

def settings(request):
    data = {}
    data['api-key'] = API_KEY
    data['sources'] = SOURCES
    data['terms'] = TERMS
    return render(request, 'settings.html', data)

def result(request):
    data = {}
    return render(request, 'results.html', data)