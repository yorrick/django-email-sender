from django.core.wsgi import get_wsgi_application
from dj_static import Cling
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_email_sender.settings_prod")
application = Cling(get_wsgi_application())
