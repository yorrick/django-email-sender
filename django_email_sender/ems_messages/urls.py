from django.conf.urls import patterns, url
from django_email_sender.ems_messages import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)
