from .celery import app
from django.core.mail import send_mail

admin_email = 'admin@example.com'


def send_success_email(user_email):
    from_email = admin_email
    subject = 'Your message was delivered!'
    message = 'Наши специалисты свяжутся с вами в ближайшее время'
    to_email = (user_email,)

    send_mail(subject, message, from_email, to_email)


@app.task
def send_email(form_data):
    from_email = form_data['from_email']
    subject = form_data['subject']
    message = form_data['message']
    to_email = (admin_email, )

    send_mail(subject, message, from_email, to_email)
    send_success_email(from_email)

