from django import forms
from .models import Publisher, Category, Game, GameDetails, GameCategory


class NamedForm(forms.ModelForm):
    """Общая проверка названий для трёх справочников."""
    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if len(name) < 2:
            raise forms.ValidationError('Введите название длиной не менее 2 символов.')
        if self._meta.model.objects.filter(name__iexact=name).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Запись с таким названием уже существует.')
        return name


class PublisherForm(NamedForm):
    class Meta:
        model = Publisher
        fields = ['name', 'email']
        error_messages = {'email': {'invalid': 'Введите корректный email, например name@example.ru.'}}


class CategoryForm(NamedForm):
    class Meta:
        model = Category
        fields = ['name']


class GameForm(NamedForm):
    class Meta:
        model = Game
        fields = ['name', 'publisher', 'price']
        error_messages = {'price': {
            'invalid': 'Введите цену числом, например 1200.50.',
            'min_value': 'Цена должна быть больше нуля.',
        }}


class GameDetailsForm(forms.ModelForm):
    class Meta:
        model = GameDetails
        fields = ['game', 'min_players', 'max_players', 'duration']

    def clean_game(self):
        game = self.cleaned_data['game']
        if GameDetails.objects.filter(game=game).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Для этой игры характеристики уже добавлены.')
        return game

    def clean(self):
        data = super().clean()
        minimum = data.get('min_players')
        maximum = data.get('max_players')
        if minimum is not None and maximum is not None and maximum < minimum:
            self.add_error('max_players', 'Максимум игроков не может быть меньше минимума.')
        return data


class GameCategoryForm(forms.ModelForm):
    class Meta:
        model = GameCategory
        fields = ['game', 'category']

    def clean(self):
        data = super().clean()
        if data.get('game') and data.get('category'):
            if GameCategory.objects.filter(game=data['game'], category=data['category']).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('Эта игра уже входит в выбранную категорию.')
        return data
