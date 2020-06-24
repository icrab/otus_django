from django.urls import path, include
from .views import UserList, UserDetails, GroupList, StudentList, TeacherList

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('students/', StudentList.as_view()),
    path('teachers/', TeacherList.as_view()),
    path('groups/', GroupList.as_view()),
]