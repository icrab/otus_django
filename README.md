1) установить requirements.txt
2) зайти в папку otus_project
3) запустить:
python manage.py makemigrations myblog
python manage.py migrate
python mangage.py fill_dbs

получаем проект с 3 курсами, 7 преподавателями, 7 учениками и 7 уроками

создаем суперпользователя:
python manage.py createsuperuser

запускаем:
python manage.py runserver

переходим по ссылке по умолчанию - управление курсами, /admin/ - админка.
