from django.conf.urls import patterns, include, url
from p4app.views import *

urlpatterns = patterns('',
	url(
		regex = r'^myentry$',
		view = myentry.as_view(),
		name = 'myentry'
	),
	url(
		regex = r'^edit/(?P<pk>\d+?)/update/$',
		view = edit.as_view(),
		name = 'myedit'
	),

	url(
		regex = r'^delete/(?P<pk>\d+?)/$',
		view = delete.as_view(),
		name = 'delete'
	),
)