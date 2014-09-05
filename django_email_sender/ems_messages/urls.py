from django.conf.urls import patterns, url
from django_email_sender.ems_messages import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<message_id>\d+)/$', views.detail, name='detail'),
    url(r'^create$', views.create, name='create'),
)
