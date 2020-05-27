from faker import Faker
from django.core.management import BaseCommand
import factory
from factory.django import DjangoModelFactory
from myblog.models import Course, User, Teacher, Student, Lesson

fake = Faker()


class CourseFactory(DjangoModelFactory):
    class Meta:
        model = Course

    title = factory.Faker('word')
    cost = factory.Faker(
           'random_int',
           min=20000,
           max=100000,
    )
    max_students = factory.Faker(
        'random_int',
        min=10,
        max=20,
    )


class UserFactory(DjangoModelFactory):
    first_name = factory.Faker('first_name')
    first_name = factory.Faker('name')
    email = factory.Faker('email')
    city = factory.Faker('city')

    course = factory.SubFactory(CourseFactory)


class TeacherFactory(UserFactory):
    class Meta:
        model = Teacher


class StudentFactory(UserFactory):
    class Meta:
        model = Student


class LessonFactory(DjangoModelFactory):
    class Meta:
        model = Lesson

    title = factory.Faker('word')
    text = factory.Faker('text')
    difficulty = factory.Iterator(Lesson.DIFFICULTY, getter=lambda s: s[0])
    ts_created = factory.Faker(
        'date_time_between',
        start_date='-2w',
        end_date='-1d',
    )
    ts_last_changed = factory.Faker(
        'date_time_between',
        start_date='-2w',
        end_date='-1d',
    )

    teacher = factory.SubFactory(TeacherFactory)
    course = factory.SubFactory(CourseFactory)


def create_all():
    courses = CourseFactory.create_batch(3)
    all_courses = Course.objects.all()
    courses_iterator = factory.Iterator(all_courses)

    teachers = TeacherFactory.create_batch(6, course=courses_iterator)
    students = StudentFactory.create_batch(6, course=courses_iterator)

    all_teachers = Teacher.objects.all()
    teachers_iterator = factory.Iterator(all_teachers)
    lessons = LessonFactory.create_batch(6, course=courses_iterator, teacher=teachers_iterator)


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_all()
        self.stdout.write(self.style.SUCCESS('Done'))
