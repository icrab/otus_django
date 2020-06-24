from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import (
                    StudentAdminViewSet,
                    TeacherAdminViewSet,
                    CourseAdminViewSet,
                    StudentUserViewSet,
                    TeacherUserViewSet,
                   )


router = DefaultRouter()
router.register('admin_student', StudentAdminViewSet, basename='admin_student')
router.register('admin_teacher', TeacherAdminViewSet, basename='admin_teacher')
router.register('admin_course', CourseAdminViewSet)
router.register('student', StudentUserViewSet, basename='student')
router.register('teacher', TeacherUserViewSet, basename='teacher')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.obtain_auth_token),
]
