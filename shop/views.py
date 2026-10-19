from django.shortcuts import render


def home(request):
    return render(request, 'shop/home.html')


def catalog(request):
    games = [
        {'name': 'Шахматы', 'description': 'Классическая игра для двух игроков.', 'price': 1200},
        {'name': 'Домино', 'description': 'Настольная игра для всей семьи.', 'price': 500},
        {'name': 'Лото', 'description': 'Игра с бочонками и карточками для компании.', 'price': 800},
    ]
    return render(request, 'shop/catalog.html', {'games': games})


def about(request):
    return render(request, 'shop/about.html')
