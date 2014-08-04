from django.conf.urls import patterns, include, url
from bapp.views import *


urlpatterns = patterns('',
    url(
        regex=r'^entry/$',
        view=entry.as_view(),
        name='entry'
    ),
    url(
        regex=r'^edit/(?P<pk>\d+?)/update/$',
        view=edit.as_view(),
        name='edit'
    ),

    url(
        regex=r'^delete/(?P<pk>\d+?)/$',
        view=delete.as_view(),
        name='delete'
    ),
)