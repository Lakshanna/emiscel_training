from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from work.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
      url(r'^$', home.as_view(), name='home'),
      url(r'^std$', stdentry.as_view()),
      # url(r'^edit$', 'helloapp.views.edit', name='edit'),
      # url(r'^view$', 'helloapp.views.view', name='view'),
      url(r'^view$',new_view.as_view()),
      url(r'^entry$',new_entry.as_view()),
      url(r'^edit/(?P<sid>\d+)/$',new_edit.as_view()),
      url(r'^delete/(?P<bid>\d+)/$',new_delete.as_view()),
    # # url(r'^blog/', include('blog.urls')),
      url(r'^admin/', include(admin.site.urls)),
    #   url(r'^grappelli/', include('grappelli.urls')),
)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns +=staticfiles_urlpatterns()