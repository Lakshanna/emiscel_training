from django.contrib import admin
from bapp.models import Userprofile
admin.site.register(Userprofile)
admin.autodiscover()

# Register your models here.
