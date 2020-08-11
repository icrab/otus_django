from django.contrib import admin

from .models import Course, Lesson, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def display_courses(self, obj: User):
        courses = obj.courses.all()
        return ', '.join((course.title for course in courses))

    list_display = 'id', 'username', 'group', 'display_courses'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    def text_short(self, obj):
        if len(obj.text) > 42:
            return f'{obj.text[:42]}...'
        return f'{obj.text}'

    list_display = 'id', 'title', 'text_short', \
                   'ts_created', 'ts_last_changed', 'course'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if request.method != 'GET':
            return Course.objects.filter()
        return Course.objects.filter().prefetch_related('users')

    def display_users(self, obj: Course):
        users = obj.users.all()
        return ', '.join((user.username for user in users))

    list_display = 'id', 'title', 'cost', 'max_students', 'display_users'
    list_display_links = 'id', 'title'



