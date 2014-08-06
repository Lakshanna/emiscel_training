from django.conf.urls import patterns, include, url
from p4app.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'p4app.views.home', name='home'),
    url(r'^welcome/$', 'p4app.views.welcome', name='welcome'),

    # url(r'^blog/', include('blog.urls')),
    #url(r'^welcome/$', 'p4app.views.welcome',name='welcome'),
    #url(r'^myentry$',myentry.as_view()),
    url(r'^view/$', view.as_view()),
   	url(r'^userform/$', 'p4app.views.userform',name='userform'),
    url(r'^log/$', 'p4app.views.log',name='log'),
    url(r'^logout/$', 'p4app.views.user_logout',name='user_logout'),
    url(r'^p4app/', include("p4app.urls")),
    url(r'^admin/', include(admin.site.urls)),
)

# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()