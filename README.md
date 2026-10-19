# Интернет-магазин настольных игр Django-проект

Учебный Django-проект: главная, каталог и «О нас». Одно собственное приложение `shop`, общий header/footer, адаптивная вёрстка без внешних библиотек и картинок.

## Запуск в Windows (PowerShell)

Требуется Python 3.10 или новее. Проверено на Python 3.13.14 и Django 5.2.18.

Распакуйте архив, откройте терминал в папке с `manage.py` и выполните:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

Откройте http://127.0.0.1:8000/. Остановка сервера: Ctrl+C.
Вызов Python по полному пути внутри `.venv` использует окружение без активации и без изменения политики PowerShell.
Если нужна явная активация: `.\.venv\Scripts\Activate.ps1` (если разрешено вашей политикой выполнения).

## Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Страницы

| URL | Страница |
| --- | --- |
| `/` | Главная |
| `/catalog/` | Каталог из шести демонстрационных игр |
| `/about/` | О нас |

## Проверка

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
```

## Структура

- `config/settings.py` — настройки проекта.
- `config/urls.py` — основной маршрутизатор, подключает `shop.urls`.
- `shop/urls.py` — три именованных маршрута.
- `shop/views.py` — три представления.
- `shop/data.py` — демонстрационная коллекция игр.
- `shop/templates/shop/` — общий шаблон и шаблоны страниц.
- `shop/static/shop/css/styles.css` — стили и адаптивная вёрстка.
- `shop/tests.py` — проверки страниц и маршрутизации.
- `REPORT_refactoring.docx` — отчёт по разделению шаблонов и статических файлов.

## Границы практической работы

Это учебная витрина без корзины, оплаты и реальных продаж. Изображения оформлены средствами CSS и типографики. Все игры и цены демонстрационные. `DEBUG=True` и учебный ключ рассчитаны на локальный запуск, а не на рабочий публичный сервер.

Виртуальное окружение создано и проверено на машине разработки. Оно не включено в ZIP: venv зависит от пути и операционной системы, поэтому на другом компьютере его создают заново приведёнными командами. База SQLite также создаётся командой `migrate`.

Проект подготовлен для размещения на GitHub. Учебный магазин называется «Ход за ходом».

## Практическая работа 20 октября 2026 года

+Общая структура находится только в `base.html`. Header и footer вынесены в `includes/header.html` и `includes/footer.html` и подключаются через `{% include %}`. Все три страницы наследуют `base.html`. Единственный файл CSS — `shop/static/shop/css/styles.css`. Встроенных стилей нет. JavaScript в проекте не используется, поэтому переносить JS-код и создавать `script.js` не требуется. Навигация работает обычными ссылками. Актуальный отчёт — `REPORT_refactoring.docx`.
