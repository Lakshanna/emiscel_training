from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from helloapp.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
      url(r'^$', 'helloapp.views.home', name='home'),
      url(r'^new_stu$', 'helloapp.views.new_stu', name='new_stu'),
      url(r'^edit$', 'helloapp.views.edit', name='edit'),
      url(r'^view$', 'helloapp.views.view', name='view'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns +=staticfiles_urlpatterns()
