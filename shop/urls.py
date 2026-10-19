from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('publishers/', views.publishers, name='publishers'),
    path('categories/', views.categories, name='categories'),
    path('details/', views.details, name='details'),
    path('game-categories/', views.game_categories, name='game_categories'),
    path('about/', views.about, name='about'),
]
