from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from sivaapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from sivaapp.views import UserView
from sivaapp.views import *

urlpatterns = patterns('',
	url(r'^$', 'sivaapp.views.loginauth', name='loginmain'),
	url(r'^add/$', UserView.as_view()),
	url(r'^list/$', 'sivaapp.views.list', name='list'),
	url(r'^signup/', 'sivaapp.views.signup', name='signup'),
	url(r'^home/', 'sivaapp.views.home', name='home'),
	url(r'^loginout/', 'sivaapp.views.loginout', name='loginout'),

	url(r'^delete/', 'sivaapp.views.delete', name='delete'),

	url(r'^edit/(?P<pk>\d+?)/update/$',UpdateView.as_view(),name='update'),

	url(r'^admin/', include(admin.site.urls)),
)
