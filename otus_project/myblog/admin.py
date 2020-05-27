from django.contrib import admin

from .models import Course, Teacher, Student, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'cost', 'max_students'
    list_display_links = 'id', 'title'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    def text_short(self, obj):
        if len(obj.text) > 42:
            return f'{obj.text[:42]}...'
        return f'{obj.text}'

    list_display = 'id', 'title', 'text_short', \
                   'teacher', 'ts_created', 'ts_last_changed'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name'
    list_display_links = 'id', 'first_name'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name'
    list_display_links = 'id', 'first_name'
