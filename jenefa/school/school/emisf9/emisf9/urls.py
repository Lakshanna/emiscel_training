from django.conf.urls import patterns, include, url
from myapp.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myapp.views.home',name='home'),
    url(r'^myapp/', include("myapp.urls")),
    url(r'^entry$',entry.as_view()),
    # url(r'^view$',view.as_view()),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^loging/', 'myapp.views.loging', name='loging'),
    url(r'^logot/$', 'myapp.views.logot', name='logot'),
)
