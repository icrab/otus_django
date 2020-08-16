from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render

from .models import Course, Lesson, User


def all_courses(request):
    return render(request, 'myblog/all_courses.html')


def course_detail_view(request, pk):
    return render(request, 'myblog/course_detail.html')


def login(request):
    return render(request, 'myblog/login.html')


def account(request):
    return render(request, 'myblog/index.html')


class AllCourses(ListView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_courses = Course.objects.all()

        context.update({
            'all_courses': all_courses,
            'all_teachers': all_teachers,
            'all_students': all_students,
            'all_lessons': all_lessons,
        })

        return context


class CreateStudentView(CreateView):
    model = User
    fields = '__all__'

    def get_success_url(self):
        student = (self.object.pk, )
        return reverse('myblog:print_student', args=student)


class UpdateStudentView(UpdateView):
    model = User
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        user = (self.object.pk, )
        return reverse('myblog:print_student', args=user)


class DeleteStudentView(DeleteView):
    model = User
    success_url = reverse_lazy('myblog:all_students')


class CreateCourseView(CreateView):
    model = Course
    fields = '__all__'

    def get_success_url(self):
        course = (self.object.pk,)
        return reverse('myblog:print_course', args=course)


class CourseDetailView(DetailView):
    model = Course


class UpdateCourseView(UpdateView):
    model = Course
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        course = (self.object.pk, )
        return reverse('myblog:print_course', args=course)


class DeleteCourseView(DeleteView):
    model = Course
    success_url = reverse_lazy('myblog:all_courses')


