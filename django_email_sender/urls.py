from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_email_sender.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('django_email_sender.ems_messages.urls', namespace="message")),
    url(r'^admin/', include(admin.site.urls)),
)
