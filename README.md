1) установить requirements.txt
2) зайти в папку otus_project
3) запустить:
- python manage.py makemigrations myblog
- python manage.py migrate
- python manage.py fill_dbs

получаем проект с 3 курсами, 7 преподавателями, 7 учениками и 7 уроками

создаем суперпользователя:
- python manage.py createsuperuser

устанавливаем redis, запускаем.
запускаем celery:
- celery -A otus_project worker

запускаем:
- python manage.py runserver

urls:
- <site_url>/ - управление курсами, 
- <site_url>/admin/ - админка
- <site_url>/contacts/ - отправка email
- <site_url>/api-token/ - Token auth
- <site_url>/oauth/ - Oauth2
