from decimal import Decimal
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


class Publisher(models.Model):
    name = models.CharField('Название издателя', max_length=100, unique=True,
                            validators=[MinLengthValidator(2)])
    email = models.EmailField('Email')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Название категории', max_length=80, unique=True,
                            validators=[MinLengthValidator(2)])

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField('Название игры', max_length=100, unique=True,
                            validators=[MinLengthValidator(2)])
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT,
                                  verbose_name='Издатель', related_name='games')
    price = models.DecimalField('Цена, руб.', max_digits=8, decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.01'))])
    categories = models.ManyToManyField(Category, through='GameCategory',
                                        related_name='games', verbose_name='Категории')

    def __str__(self):
        return self.name


class GameDetails(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE,
                                related_name='details', verbose_name='Игра')
    min_players = models.PositiveSmallIntegerField('Минимум игроков',
                        validators=[MinValueValidator(1), MaxValueValidator(20)])
    max_players = models.PositiveSmallIntegerField('Максимум игроков',
                        validators=[MinValueValidator(1), MaxValueValidator(20)])
    duration = models.PositiveSmallIntegerField('Длительность, мин.',
                        validators=[MinValueValidator(1), MaxValueValidator(1440)])

    def __str__(self):
        return str(self.game)


class GameCategory(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['game', 'category'],
                                               name='unique_game_category')]

    def __str__(self):
        return f'{self.game} — {self.category}'
