from rest_framework import serializers
from myblog.models import Course, Lesson, User
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password



class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = 'id', 'title', 'text', 'difficulty'


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = 'id', 'title', 'cost', 'lessons'


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = 'key'


class UserSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = 'id', 'username', 'password', 'email', 'courses'
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(
                      required=True,
                      validators=(UniqueValidator(queryset=User.objects.all()), )
                      )
    email = serializers.EmailField(
                      required=True,
                      validators=(UniqueValidator(queryset=User.objects.all()), )
                      )
    password = serializers.CharField(min_length=4)
    confirm_password = serializers.CharField(min_length=4)





