# Production settings

from django_email_sender.settings_common import *

import dj_database_url

DATABASES['default'] =  dj_database_url.config()

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

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
