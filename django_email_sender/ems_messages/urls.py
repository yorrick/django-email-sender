from django.conf.urls import patterns, url
from django_email_sender.ems_messages import views
from django.views.decorators.cache import cache_page


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', cache_page(60 * 15)(views.DetailView.as_view()), name='detail'),
)
