from django.contrib import admin
from .models import Publisher, Category, Game, GameDetails, GameCategory
from .forms import PublisherForm, CategoryForm, GameForm, GameDetailsForm, GameCategoryForm


admin.site.site_header = 'Магазин настольных игр'
admin.site.site_title = 'Админ-панель магазина'
admin.site.index_title = 'Управление магазином'


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    form = PublisherForm
    list_display = ('name', 'email')
    list_filter = ('games__categories',)
    search_fields = ('name', 'email')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ('name',)
    list_filter = ('games__publisher',)
    search_fields = ('name',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    form = GameForm
    list_display = ('name', 'publisher', 'price')
    list_filter = ('publisher', 'categories')
    search_fields = ('name', 'publisher__name')
    list_select_related = ('publisher',)


@admin.register(GameDetails)
class GameDetailsAdmin(admin.ModelAdmin):
    form = GameDetailsForm
    list_display = ('game', 'min_players', 'max_players', 'duration')
    list_filter = ('min_players', 'max_players', 'duration')
    search_fields = ('game__name',)
    list_select_related = ('game',)


@admin.register(GameCategory)
class GameCategoryAdmin(admin.ModelAdmin):
    form = GameCategoryForm
    list_display = ('game', 'category')
    list_filter = ('category', 'game__publisher')
    search_fields = ('game__name', 'category__name')
    list_select_related = ('game', 'category')
