from django.urls import path
from .views import all_courses, login, course_detail_view, account

app_name = 'myblog'

urlpatterns = [
    path(
        '',
        account,
        name='account'
    )
]
