from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myapp.views.home', name='home'),
    url(r'^studview$', 'myapp.views.stud_view', name='stud_view'),
    url(r'^entry$', 'myapp.views.stud_entry', name='stud_entry'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
