from django.conf.urls import patterns, include, url
from studentapp.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home1$', 'studentapp.views.home1', name='home1'),
    #url(r'^chpwd$', 'studentapp.views.chpwd', name='chpwd'),
    url(r'^signup$', 'studentapp.views.signup', name='signup'),
    url(r'^logot$', 'studentapp.views.logot', name='logot'),
    url(r'^new_stu$', new_stu.as_view()),
    url(
    	regex=r'^edit_stu/(?P<pk>\d+?)/$',
    	view=edit_stu.as_view(),
    	name='edit_stu'),
    #url(r'^edit_stu/(?P<pk>\d+)/$',edit_stu.as_view()),
    url(r'^view_stu$', 'studentapp.views.view_stu',name='view_stu'),
    url(
        regex=r'^del_stu/(?P<pk>\d+?)/$',
        view=del_stu.as_view(),
        name='del_stu'),
    url(r'^admin/', include(admin.site.urls)),
)
