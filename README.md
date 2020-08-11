1) установить requirements.txt
2) зайти в папку otus_project
3) запустить:
- python manage.py makemigrations myblog
- python manage.py migrate
- python manage.py fill_dbs

создаем суперпользователя:
- python manage.py createsuperuser

запускаем:
- python manage.py runserver

urls:
- <site_url>/admin/ - админка
- <site_url>/api-token/ - Token auth


React:
build:
cd otus_project/frontend/login/
npm run dev

cd otus_project/frontend/courses/
npm run dev

cd otus_project/frontend/course/
npm run dev

urls:
- <site_url>/login/ - login, get data by token
- <site_url>/all_courses/ - all courses
- <site_url>/print_course/pk/ - single course
 
