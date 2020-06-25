from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import (
                    StudentRegisteredViewSet,
                    TeacherRegisteredViewSet,
                    CourseRegisteredViewSet,
                    TeacherGuestViewSet,
                    CourseGuestViewSet
                   )


router = DefaultRouter()
router.register('course', CourseGuestViewSet, basename='course')
router.register('teacher', TeacherGuestViewSet, basename='teacher')
router.register('user_student', StudentRegisteredViewSet, basename='user_student')
router.register('user_teacher', TeacherRegisteredViewSet, basename='user_teacher')
router.register('user_course', CourseRegisteredViewSet, basename='user_course')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.obtain_auth_token),
]
