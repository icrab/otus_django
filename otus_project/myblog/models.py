from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50)
    cost = models.IntegerField()
    max_students = models.IntegerField()

    def __str__(self):
        return self.title


class User(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=50)

    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name


class Teacher(User):
    pass


class Student(User):
    pass


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

    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title} : {self.text}'
