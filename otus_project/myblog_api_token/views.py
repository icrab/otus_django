from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.permissions import (
                                        IsAuthenticated,
                                        IsAdminUser,
                                        AllowAny,
                                        )
from .permissions import CustomDjangoModelPermissions

from myblog.models import Student, Teacher, Course
from django.contrib.auth.models import User
from .serializers import (
                          StudentSerializer,
                          TeacherSerializer,
                          CourseSerializer,
                         )


class BaseAdminViewSet(ModelViewSet):
    '''
    Childs of this class require admin permission
    '''
    permission_classes = (IsAdminUser, )


class StudentAdminViewSet(BaseAdminViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherAdminViewSet(BaseAdminViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseAdminViewSet(BaseAdminViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class BaseUserViewSet(ModelViewSet):
    '''
    Childs of this class require django model permission
    '''
    permission_classes = (CustomDjangoModelPermissions, )


class StudentUserViewSet(BaseUserViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherUserViewSet(BaseUserViewSet):
    queryset = Teacher.objects.all()
    serializer_class = StudentSerializer
