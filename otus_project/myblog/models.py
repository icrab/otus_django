from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50)
    cost = models.IntegerField()
    max_students = models.IntegerField()

    def __str__(self):
        return self.title


class User(AbstractUser):
    GROUP_STUDENT = 0
    GROUP_TEACHER = 1
    GROUP_ADMIN = 2

    GROUP = (
        (GROUP_STUDENT, 'Студент'),
        (GROUP_TEACHER, 'Учитель'),
        (GROUP_ADMIN, 'Админ'),
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        validators=(
            UnicodeUsernameValidator,
            MinLengthValidator(4)
        )
    )

    password = models.CharField(
        max_length=128,
        validators=(MinLengthValidator(4), )
    )

    email = models.EmailField(unique=True)
    group = models.PositiveSmallIntegerField(choices=GROUP, default=GROUP_STUDENT)
    courses = models.ManyToManyField(Course, blank=True, related_name='users')

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Lesson(models.Model):
    DIFFICULTY_EASY = 1
    DIFFICULTY_MEDIUM = 2
    DIFFICULTY_HARD = 3

    DIFFICULTY = (
        (DIFFICULTY_EASY, 'Легкий'),
        (DIFFICULTY_MEDIUM, 'Средний'),
        (DIFFICULTY_HARD, 'Сложный'),
    )

    title = models.CharField(max_length=254)
    text = models.TextField()
    difficulty = models.PositiveSmallIntegerField(choices=DIFFICULTY)
    ts_created = models.DateTimeField(auto_now_add=True, null=True)
    ts_last_changed = models.DateTimeField(auto_now=True, null=True)

    course = models.ForeignKey(Course, null=True, related_name='lessons', on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title} : {self.text}'


