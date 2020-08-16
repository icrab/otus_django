from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import (
                    CourseGuestViewSet,
                    SignUpOnCourse,
                    StudentRegisteredCoursesViewSet,
                    UserCreate,
                    RefreshAuthToken,
                    CheckAuthToken,
                    Logout,
                   )


router = DefaultRouter()
router.register('courses', CourseGuestViewSet, basename='courses')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.obtain_auth_token),
    path('sign_up_on_course/', SignUpOnCourse.as_view()),
    path('user_courses/', StudentRegisteredCoursesViewSet.as_view()),
    path('refresh_auth_token/', RefreshAuthToken.as_view()),
    path('check_auth_token/', CheckAuthToken.as_view()),
    path('register/', UserCreate.as_view()),
    path('logout/', Logout.as_view()),
]
