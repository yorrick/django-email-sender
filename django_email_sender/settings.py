# Developpement settings

from django_email_sender.settings_common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'docker',
        'USER': 'docker',
        'PASSWORD': 'docker',
        'HOST': '192.168.59.103',  # host of docker VM
        'PORT': '5432',
        },
    }

ALLOWED_HOSTS = []
