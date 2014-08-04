"""
Django settings for bharathi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z@jmid^3#ph8i(o6c&g)2uz$mh^6#h#b=nmrin7-n2vd1df0ti'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#SESSION_EXPIRES_AT_BROWSER_CLOSE=True
#SESSION_EXPIRE_AT_BROWSER_CLOSE = True
#SESSION_EXPIRE_AT_BROWSER_CLOSE = False

#SESSION_COOKIE_AGE=30*60
# Application definition

INSTALLED_APPS = (
    # 'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'thamarainew.middlewares.StatsMiddleware',
)

ROOT_URLCONF = 'bharathi.urls'

WSGI_APPLICATION = 'bharathi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mugildb',
        'USER' : 'mugil',
        'PASSWORD':'mugil',
        'HOST':'',
        'PORT':''
            }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_LOADERS =['django.template.loaders.filesystem.Loader',
'django.template.loaders.app_directories.Loader',] #'django.template.loaders.cached.Loader', (
       
        
    

TEMPLATE_DIRS=[os.path.join(BASE_DIR,"templates"),]

TEMPLATE_CONTEXT_PROCESSORS=("django.core.context_processors.request",
"django.contrib.auth.context_processors.auth",)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/site_media/media/'
MEDIA_ROOT= os.path.join(BASE_DIR,'site_media','media')
STATIC_ROOT= os.path.join(BASE_DIR,'site_media','static')

#STATICFILES_DIRS=[os.path.join(BASE_DIR,'static'),]
STATICFILES_FINDERS=["django.contrib.staticfiles.finders.AppDirectoriesFinder",
"django.contrib.staticfiles.finders.FileSystemFinder",]
                     

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}
