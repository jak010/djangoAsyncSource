from .base import *

from .etc.CELERY import *

import random

INSTALLED_APPS += [
    'django_celery_beat',
    'django_celery_results',
    'api',
    'channels',

]

CELERY_BEAT_SCHEDULE = {
    'test': {
        'task': 'api.tasks.add',
        'schedule': 1,
        'args': (random.randint(1, 10), random.randint(1, 10))
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

ASGI_APPLICATION = "config.routing.application"
