from django.urls import path
from .views import all_students, login, \
    CreateStudentView, AllCourses, StudentDetailView, \
    DeleteStudentView, UpdateStudentView, CreateCourseView, \
    CourseDetailView, UpdateCourseView, DeleteCourseView

app_name = 'myblog'

urlpatterns = [
    path(
        '',
        AllCourses.as_view(),
        name='all_courses'
    ),
    path(
        'create_course/',
        CreateCourseView.as_view(),
        name='create_course'
    ),
    path(
        'print_course/<int:pk>/',
        CourseDetailView.as_view(),
        name='print_course'
    ),
    path(
        'update_course/<int:pk>/',
        UpdateCourseView.as_view(),
        name='update_course'
    ),
    path(
        'delete_course/<int:pk>/',
        DeleteCourseView.as_view(),
        name='delete_course'
    ),
    path(
        'login/',
        login,
        name='login'
    ),
    path(
        'all_students/',
        all_students,
        name='all_students'
    ),
    path(
        'create_student/',
        CreateStudentView.as_view(),
        name='create_student'
    ),
    path(
        'print_student/<int:pk>/',
        StudentDetailView.as_view(),
        name='print_student'
    ),
    path(
        'update_student/<int:pk>/',
        UpdateStudentView.as_view(),
        name='update_student'
        ),
    path(
        'delete_student/<int:pk>/',
        DeleteStudentView.as_view(),
        name='delete_student'
    ),
]
