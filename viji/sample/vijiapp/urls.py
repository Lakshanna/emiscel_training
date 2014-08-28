from django.conf.urls import patterns, include, url
from vijiapp.views import *

urlpatterns = patterns('',
	url(
		regex=r'^student_detail/create/$',
		view = Student_Detail_CreateView.as_view(),
		name = 'students_detail_create'
	),
	url(
		regex=r'^student_detail/(?P<pk>\d+?)/update/$',
		view = Student_Detail_UpdateView.as_view(),
		name = 'students_detail_update'
	),
)

