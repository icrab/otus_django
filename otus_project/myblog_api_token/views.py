from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import CustomDjangoModelPermissions
from rest_framework.permissions import AllowAny

from myblog.models import Course, Lesson, User
from .serializers import (
                          UserSerializer,
                          CourseSerializer,
                          LessonSerializer,
                        )


class BaseGuestViewSet(ReadOnlyModelViewSet):
    '''
    Base class for guest users
    '''
    permission_classes = (AllowAny, )


class TeacherGuestViewSet(BaseGuestViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BaseGuestViewSet(ReadOnlyModelViewSet):
    '''
    Base class for guest users
    '''
    permission_classes = (AllowAny, )


class CourseGuestViewSet(BaseGuestViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class BaseRegisteredViewSet(ModelViewSet):
    '''
    Base class for registered users with django permissions
    '''


class StudentRegisteredViewSet(BaseRegisteredViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CourseRegisteredViewSet(BaseRegisteredViewSet):
    permission_classes = (CustomDjangoModelPermissions, )

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonRegisteredViewSet(BaseRegisteredViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class SignUpOnCourse(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return Response('User us not authenticated', status=401)

        auth_user = request.user
        course_id = request.data['course']

        try:
            course = Course.objects.get(id=course_id)
            course.users.add(auth_user)
            course.save()

        except Exception:
            return Response('Failed', status=400)

        return Response('Success!', status=200)

