from django.shortcuts import render
from .data import GAMES

def home(request):
    return render(request, 'shop/home.html', {'page': 'home', 'games': GAMES[:3]})

def catalog(request):
    return render(request, 'shop/catalog.html', {'page': 'catalog', 'games': GAMES})

def about(request):
    return render(request, 'shop/about.html', {'page': 'about'})
