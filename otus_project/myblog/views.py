from django.views.generic import TemplateView, CreateView, DeleteView,\
    UpdateView, DetailView
from django.views.generic.list import ListView

from .models import Course, Teacher, Student, Lesson


class PrintAllCourses(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_courses = Course.objects.all()
        all_teachers = Teacher.objects.all()
        all_students = Student.objects.all()
        all_lessons = Lesson.objects.all()

        context.update({
            'all_courses': all_courses,
            'all_teachers': all_teachers,
            'all_students': all_students,
            'all_lessons': all_lessons,
        })

        return context


class PrintAllStudents(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        all_students = Student.objects.all()

        context.update({'students': all_students})

        return context


class CreateStudentView(CreateView):
    model = Student
    fields = '__all__'

    def get_success_url(self):
        return f'/print_student/{self.object.pk}/'


class StudentDetailView(DetailView):
    model = Student


class UpdateStudentView(UpdateView):
    model = Student
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return f'/print_student/{self.object.pk}/'


class DeleteStudentView(DeleteView):
    model = Student
    success_url = '/all_students/'


class CreateCourseView(CreateView):
    model = Course
    fields = '__all__'

    def get_success_url(self):
        return f'/print_course/{self.object.pk}'


class CourseDetailView(DetailView):
    model = Course


class UpdateCourseView(UpdateView):
    model = Course
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return f'/print_course/{self.object.pk}'


class DeleteCourseView(DeleteView):
    model = Course
    success_url = '/'


class StudentsListView(ListView):
    model = Student
    context_object_name = 'students'
    paginate_by = 3
