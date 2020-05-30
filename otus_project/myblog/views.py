from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.views.generic import FormView, CreateView, DeleteView, UpdateView, DetailView, TemplateView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy

from .models import Course, Teacher, Student, Lesson
from .forms import ContactForm
from otus_project.tasks import send_email


class AllCourses(ListView):
    model = Course

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


class AllStudents(ListView):
    model = Student
    context_object_name = 'students'


class CreateStudentView(CreateView):
    model = Student
    fields = '__all__'

    def get_success_url(self):
        student = (self.object.pk, )
        return reverse('myblog:print_student', args=student)


class StudentDetailView(DetailView):
    model = Student


class UpdateStudentView(UpdateView):
    model = Student
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        user = (self.object.pk, )
        return reverse('myblog:print_student', args=user)


class DeleteStudentView(DeleteView):
    model = Student
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


class ContactsView(FormView):
    template_name = 'myblog/contacts.html'
    form_class = ContactForm

    def form_valid(self, form):
        form_data = form.cleaned_data
        send_email.delay(form_data)

        return HttpResponseRedirect(reverse_lazy('myblog:send-success'))



class SendAccessView(TemplateView):
    template_name = 'myblog/send-success.html'


