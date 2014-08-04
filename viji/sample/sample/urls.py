from django.conf.urls import patterns, include, url
from myap.views import *
from vijiapp.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')), 
    url(r'^$', 'myap.views.home', name='home'),
    url(r'^loging', 'myap.views.loging', name='loging'),
    url(r'^entscr/$', entscr.as_view()),
    url(r'^viewscr/$', 'myap.views.viewscr',name='viewscr'),
    url(r'^logot/$', 'myap.views.logot', name='logot'),






    url(r'^$', IndexClass.as_view()),
    url(r"^vijiapp/",include("vijiapp.urls")),
#    url(r'^timeshow/$', 'myap.views.timeshow', name='timeshow'),
     # url(r'^blog/', include('blog.urls')),

#    url(r'^test/$', 'myap.views.test', name='test'),

    url(r'^entry/$', 'myap.views.entry', name='entry'),

    url(r'^log/$', 'myap.views.log', name='log'),
    url(r'^logsuccess/$', 'myap.views.logsuccess', name='logsuccess'),
    url(r'^restricted/$', 'myap.views.restricted', name='restricted'),


)
