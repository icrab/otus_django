from faker import Faker
from django.core.management import BaseCommand
import factory
from factory.django import DjangoModelFactory
from myblog.models import Course, Lesson, User

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
    username = factory.Faker('name')
    password = factory.Faker('password')
    email = factory.Faker('email')
    group = factory.Faker(
        'random_int',
        min=0,
        max=1,
    )

    class Meta:
        model = User

    @factory.post_generation
    def courses(self, create, extracted, **kwargs):
        if not create:
            return

        for _ in range(3):
            self.courses.add(CourseFactory())


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


def create_all():
    courses = CourseFactory.create_batch(9)
    all_courses = Course.objects.all()

    courses_iterator = factory.Iterator(all_courses)

    lessons = LessonFactory.create_batch(9, course=courses_iterator)
    users = UserFactory.create_batch(9)


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_all()
        self.stdout.write(self.style.SUCCESS('Done'))
