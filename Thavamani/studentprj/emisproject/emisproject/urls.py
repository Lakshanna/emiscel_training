from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls.static import static
from emisapp.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'emisapp.views.home', name='home'),
    url(r'^signup$', 'emisapp.views.signup', name='signup'),
    url(r'^new_stu$', new_stu.as_view()),
    url(r'^logot$', 'emisapp.views.logot', name='logot'),
    url(r'^admin/', include(admin.site.urls)),
    url(
    	regex=r'^edit_stu/(?P<pk>\d+?)/$',
    	view=edit_stu.as_view(),
    	name='edit_stu'),
	url(
    	regex=r'^edit_stu2/(?P<pk>\d+?)/$',
    	view=edit_stu2.as_view(),
    	name='edit_stu2'),   
    url(
    	regex=r'^edit_stu1/(?P<pk>\d+?)/$',
    	view=edit_stu1.as_view(),
    	name='edit_stu1'),
    url(r'^view_stu$', 'emisapp.views.view_stu',name='view_stu'),
    # url(
    #     regex=r'^del_stu/(?P<pk>\d+?)/$',
    #     view=del_stu.as_view(),
    #     name='del_stu'),



)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
