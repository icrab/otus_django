from django.urls import path
from .views import CreateStudentView, PrintAllCourses, StudentDetailView, \
    PrintAllStudents, StudentsListView, DeleteStudentView, UpdateStudentView, \
    CreateCourseView, CourseDetailView, UpdateCourseView, DeleteCourseView

app_name = 'myblog'

urlpatterns = [
    path(
        '',
        PrintAllCourses.as_view(template_name='myblog/all_courses.html'),
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
        'all_students/',
        PrintAllStudents.as_view(template_name='myblog/all_students.html'),
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
    path(
        'all_students_pagination/',
        StudentsListView.as_view(),
        name='all_students_pagination'
    ),
]
