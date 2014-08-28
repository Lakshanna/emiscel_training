from django.conf.urls import patterns, include, url
from myapp.views import *

urlpatterns = patterns('',
	url(regex=r'^entry/',
		view=entry.as_view(),
		name='entry'),

	)