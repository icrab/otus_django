from .base import *
from .other_settings import *

SECRET_KEY = '*b9*qnqg8kyx$ye5inwo^3b15%79zbv*+u)*l2c0%xwyj_to#%'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS += [
                  'corsheaders',
                  ]

MIDDLEWARE += [
              'corsheaders.middleware.CorsMiddleware',
              'django.middleware.common.CommonMiddleware',
              ]

CORS_ORIGIN_ALLOW_ALL = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

BROKER_URL = 'redis://127.0.0.1:6379/0'
BROKER_TRANSPORT = 'redis'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'app-messages'
