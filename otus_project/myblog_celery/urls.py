from django.urls import path
from .views import ContactsView, SendAccessView

app_name = 'myblog_celery'

urlpatterns = [
    path(
        '',
        ContactsView.as_view(),
        name='contacts'
    ),
    path(
        'send-success/',
        SendAccessView.as_view(),
        name='send-success',
    ),
]

