from django.urls import path
from .views import all_courses, login, course_detail_view, auth, \
    CreateStudentView, AllCourses, \
    DeleteStudentView, UpdateStudentView, CreateCourseView, \
    CourseDetailView, UpdateCourseView, DeleteCourseView

app_name = 'myblog'

urlpatterns = [
    path(
        'all_courses/',
        all_courses,
        name='all_courses'
    ),
    path(
        'create_course/',
        CreateCourseView.as_view(),
        name='create_course'
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
        'auth/',
        auth,
        name='auth'
    ),
    path(
        'create_student/',
        CreateStudentView.as_view(),
        name='create_student'
    ),
    path(
        'print_course/<int:pk>/',
        course_detail_view,
        name='print_course'
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
