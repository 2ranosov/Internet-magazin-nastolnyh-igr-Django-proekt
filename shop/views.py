from django.shortcuts import render, redirect
from .models import Publisher, Category, Game, GameDetails, GameCategory
from .forms import PublisherForm, CategoryForm, GameForm, GameDetailsForm, GameCategoryForm


def home(request):
    return render(request, 'shop/home.html')


def about(request):
    return render(request, 'shop/about.html')


def table_page(request, form_class, records, template, route):
    # Не используем request.POST or None: пустой POST тоже должен пройти проверку.
    form = form_class(request.POST if request.method == 'POST' else None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('shop:' + route)
    return render(request, 'shop/' + template, {'form': form, 'records': records})


def publishers(request):
    return table_page(request, PublisherForm, Publisher.objects.order_by('id'),
                      'publishers.html', 'publishers')


def categories(request):
    return table_page(request, CategoryForm, Category.objects.order_by('id'),
                      'categories.html', 'categories')


def catalog(request):
    records = Game.objects.select_related('publisher').prefetch_related('categories').order_by('id')
    return table_page(request, GameForm, records, 'catalog.html', 'catalog')


def details(request):
    records = GameDetails.objects.select_related('game').order_by('id')
    return table_page(request, GameDetailsForm, records, 'details.html', 'details')


def game_categories(request):
    records = GameCategory.objects.select_related('game', 'category').order_by('id')
    return table_page(request, GameCategoryForm, records, 'game_categories.html', 'game_categories')
