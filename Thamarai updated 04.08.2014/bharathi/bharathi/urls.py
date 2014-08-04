from django.conf.urls import patterns, include, url
from django.contrib import admin
from bapp.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bapp.views.userlogin', name='userlogin'),
    url(r'^home$', 'bapp.views.home', name='home'),
    url(r'^signup/$', 'bapp.views.signup', name='signup'),
    url(r'^login/$', 'bapp.views.userlogin', name='userlogin'),
    url(r'^logout/$','bapp.views.userlogout',name='userlogout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^bapp/", include("bapp.urls")),
    url(r'^view/$', view.as_view()),
    url(r'^markview/$', markview.as_view()),
    url(r'^classview/$', classview.as_view()),	      
)
    
    
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
