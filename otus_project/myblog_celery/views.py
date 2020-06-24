from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from otus_project.tasks import send_email


class ContactsView(FormView):
    template_name = 'myblog_celery/contacts.html'
    form_class = ContactForm

    def form_valid(self, form):
        form_data = form.cleaned_data
        send_email.delay(form_data)

        return HttpResponseRedirect(reverse_lazy('myblog_celery:send-success'))


class SendAccessView(TemplateView):
    template_name = 'myblog_celery/send-success.html'

