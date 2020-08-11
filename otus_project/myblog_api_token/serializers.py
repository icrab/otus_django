from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from myblog.models import Course, Lesson, User


# set students as default group
#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        instance.groups.add(Group.objects.get(name='students'))

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
    courses = CourseSerializer(many=True)

    class Meta:
        model = User
        fields = 'id', 'username', 'password', 'email', 'courses'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user




