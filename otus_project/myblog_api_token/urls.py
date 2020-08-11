from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import (
                    StudentRegisteredViewSet,
                    CourseRegisteredViewSet,
                    TeacherGuestViewSet,
                    CourseGuestViewSet,
                    LessonRegisteredViewSet,
                    SignUpOnCourse,
                   )


router = DefaultRouter()
router.register('course', CourseGuestViewSet, basename='course')
router.register('teacher', TeacherGuestViewSet, basename='teacher')
router.register('user_student', StudentRegisteredViewSet, basename='user_student')
router.register('user_course', CourseRegisteredViewSet, basename='user_course')
router.register('lessons', LessonRegisteredViewSet, basename='lessons')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.obtain_auth_token),
    path('sign_up_on_course/', SignUpOnCourse.as_view())
]
