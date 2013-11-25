import mongoengine
mongoengine.connect('miniwave')

import os
ROOT_PATH = os.path.dirname(__file__)
# Django settings for miniwave project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
domain = 'http://miniwave.net'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
APPEND_SLASH = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'framework',                      # Or path to database file if using sqlite3.
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

TWITTER_KEY    = ''
TWITTER_SECRET = ''

MEDIA_ROOT = os.path.join(ROOT_PATH,'media')
MEDIA_URL = domain + '/media/'

LOGIN_REDIRECT_URL = '/'
STATIC_ROOT = os.path.join(ROOT_PATH,'static')
STATIC_URL =  '/static/'
JINJA_CONFIG = {'autoescape': True}

TEMPLATE_DEBUG = DEBUG


STATICFILES_DIRS = (
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^tb*57_k+2)7a9q3q*r6637_-l1h!o3!=lr#8dsps(scu#)2i3'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'framework.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'framework.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH,'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap_toolkit',
)

SESSION_ENGINE = 'mongoengine.django.sessions'
AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
