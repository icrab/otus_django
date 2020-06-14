from logging.config import dictConfig
from .base import BASE_DIR
from pathlib import Path

LOG_PATH = BASE_DIR + '/logs'
Path(LOG_PATH).mkdir(parents=True, exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
            },
        },
    'handlers': {
        'celery': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/celery.log',
            'formatter': 'simple',
            'maxBytes': 1024 * 1024 * 100,  # 100 mb
        },
    },
    'loggers': {
        'celery': {
            'handlers': ['celery', ],
            'level': 'INFO',
        },
    }
}

dictConfig(LOGGING)

CELERYD_HIJACK_ROOT_LOGGER = False
