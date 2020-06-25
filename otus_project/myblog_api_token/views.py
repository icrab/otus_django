from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .permissions import CustomDjangoModelPermissions
from rest_framework.permissions import AllowAny

from myblog.models import Student, Teacher, Course
from .serializers import (
                          StudentSerializer,
                          TeacherSerializer,
                          CourseSerializer,
                         )


class BaseGuestViewSet(ReadOnlyModelViewSet):
    '''
    Base class for guest users
    '''
    permission_classes = (AllowAny, )


class TeacherGuestViewSet(BaseGuestViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseGuestViewSet(BaseGuestViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class BaseRegisteredViewSet(ModelViewSet):
    '''
    Base class for registered users with django permissions
    '''
    permission_classes = (CustomDjangoModelPermissions, )


class StudentRegisteredViewSet(BaseRegisteredViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherRegisteredViewSet(BaseRegisteredViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseRegisteredViewSet(BaseRegisteredViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

