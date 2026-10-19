from django.db import migrations


def fill_tables(apps, schema_editor):
    Publisher = apps.get_model('shop', 'Publisher')
    Category = apps.get_model('shop', 'Category')
    Game = apps.get_model('shop', 'Game')
    Details = apps.get_model('shop', 'GameDetails')
    Link = apps.get_model('shop', 'GameCategory')
    db = schema_editor.connection.alias
    # Учебные издатели и контактные адреса, не реальные компании.
    rows = [
        ('Мир стратегии', 'strategy@example.com', 'Стратегические', 'Шахматы', '1200.00', 2, 2, 60),
        ('Семейный вечер', 'family@example.com', 'Семейные', 'Лото', '800.00', 2, 6, 30),
        ('Клуб настольных игр', 'club@example.com', 'Классические', 'Домино', '500.00', 2, 4, 20),
    ]
    for publisher, email, category, title, price, minimum, maximum, duration in rows:
        pub, _ = Publisher.objects.using(db).get_or_create(name=publisher, defaults={'email': email})
        cat, _ = Category.objects.using(db).get_or_create(name=category)
        game, _ = Game.objects.using(db).get_or_create(name=title, defaults={'publisher': pub, 'price': price})
        Details.objects.using(db).get_or_create(game=game, defaults={
            'min_players': minimum, 'max_players': maximum, 'duration': duration,
        })
        Link.objects.using(db).get_or_create(game=game, category=cat)


class Migration(migrations.Migration):
    dependencies = [('shop', '0002_alter_category_options_alter_game_options_and_more')]
    operations = [migrations.RunPython(fill_tables, migrations.RunPython.noop)]
