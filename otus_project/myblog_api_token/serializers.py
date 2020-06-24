from rest_framework import serializers
from myblog.models import Student, Teacher, Course


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = 'id', 'first_name', 'last_name', 'email'


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = 'id', 'first_name', 'last_name', 'email'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = 'title', 'cost', 'max_students'

