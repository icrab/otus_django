from rest_framework import serializers
from myblog.models import Course, Lesson, User
from django.db import models


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = 'id', 'title', 'text', 'difficulty'


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = 'id', 'title', 'cost', 'lessons'


class UserSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = 'id', 'username', 'password', 'email', 'courses'
        extra_kwargs = {
            'password': {'write_only': True},
        }


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate_email(self, email):
        existing = User.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Someone with that email "
                "address has already registered. Was it you?")

        return email

    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")

        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")

        return data



