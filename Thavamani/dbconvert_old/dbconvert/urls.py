from django.conf.urls import patterns, include, url
from dbconvertapp.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dbconvertapp.views.home1', name='home1'),
    # url(r'^blog/', include('blog.urls')),
	# url(r'^showdetails$', 'dbconvertapp.views.showdetails', name='showdetails'),
    url(r'^calc$', 'dbconvertapp.views.calc', name='calc'),
	url(
    	regex=r'^showdetails$',
    	view=showdetails.as_view(),
    	name='showdetails'),
    url(
        regex=r'^$',
        view=home1.as_view(),
        name='home1'),
	url(
    	regex=r'^calc1$',
    	view=calc1.as_view(),
    	name='calc1'),

    # url(r'^new_stu$', new_stu.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
