from django.http import HttpResponse
from django.shortcuts import render

from .models import Course, Teacher, Student, Lesson


def index_view(request):
    all_courses = Course.objects.all()
    all_teachers = Teacher.objects.all()
    all_students = Student.objects.all()
    all_lessons = Lesson.objects.all()

    context = {
        'all_courses': all_courses,
        'all_teachers': all_teachers,
        'all_students': all_students,
        'all_lessons': all_lessons,
    }

    return render(request, 'myblog/index.html', context=context)


