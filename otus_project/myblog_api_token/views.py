from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .permissions import CustomDjangoModelPermissions
from rest_framework.permissions import AllowAny, IsAuthenticated

from myblog.models import Course, Lesson, User
from .serializers import (
                          UserSerializer,
                          CourseSerializer,
                          LessonSerializer,
                          UserRegistrationSerializer,
                          TokenSerializer
                        )


class CourseGuestViewSet(ModelViewSet):
    permission_classes = (AllowAny, )
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonRegisteredViewSet(ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class Logout(APIView):
    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserCreate(APIView):
    permission_classes = (AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_serializer = UserSerializer(data=serializer.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        user_id = user_serializer.data['id']
        token = Token.objects.create(user_id=user_id)
        token.save()

        return Response({
            'token': token.key,
        })


class SignUpOnCourse(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        if not request.user.is_authenticated:
            return Response('User us not authenticated', status=status.HTTP_401_UNAUTHORIZED)

        auth_user = request.user
        course_id = request.data['course']

        try:
            course = Course.objects.get(id=course_id)
            course.users.add(auth_user)
            course.save()

        except Exception:
            return Response('Failed', status=status.HTTP_400_BAD_REQUEST)

        return Response('Success!', status=status.HTTP_200_OK)


class StudentRegisteredCoursesViewSet(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        if not request.user.is_authenticated:
            return Response('User us not authenticated', status=status.HTTP_401_UNAUTHORIZED)

        auth_user = request.user

        courses = Course.objects.filter(users=auth_user.id)
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)


class CheckAuthToken(ObtainAuthToken):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        auth_user = request.user
        token = Token.objects.get(user=auth_user)
        return Response({
            'token': token.key,
        })


class RefreshAuthToken(ObtainAuthToken):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        auth_user = request.user
        Token.objects.filter(user=auth_user).delete()
        token, created = Token.objects.get_or_create(user=auth_user)
        return Response({
            'token': token.key,
        })