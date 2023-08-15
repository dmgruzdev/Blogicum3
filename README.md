# Социальная сеть для блогеров - Blogicum.
Это приложение с пользовательским интерфейсом. В нем реализована регистрация и аутентификация пользователей. Авторизованный пользователь может написать и отредактировать свои посты (текст + фотография), писать комментарии к постам, подписываться на страницы других пользователей. Посты могут быть привязаны к тематической группе. Доступны к просмотру: 
- список всех постов на главной странице,
- список постов конкретного автора, 
- список постов определенной тематической группы,
- новостная лента авторизованного пользователя - посты от авторов из подписок.

На каждую страницу выводится 5 последних постов, реализована пагинация. Список постов на главной странице сайта хранится в кэше и обновляется раз в 20 секунд.


## Технологии:
- Python 3.7
- Django 2.2
- Unittest
## Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/dmgruzdev/Blogicum3
```
```
cd yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```
