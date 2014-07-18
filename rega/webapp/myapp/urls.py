from django.conf.urls import patterns, include, url
from myapp.views import *


urlpatterns = patterns('',
    url(
        regex=r'^student_detail/create/$',
        view=Student_detailCreateView.as_view(),
        name='students_detail_create'
    ),
    url(
        regex=r'^student_detail/(?P<pk>\d+?)/update/$',
        view=Student_detailUpdateView.as_view(),
        name='students_detail_update'
    ),
)
