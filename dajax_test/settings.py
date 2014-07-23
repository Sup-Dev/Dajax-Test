import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'v_lro%5a8^(m8!zw#-633*g-=)$8v^z9wcy+6kbevpbezzeos='
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'dajaxice',
    'dajax',
    'examples',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'dajax_test.urls'
WSGI_APPLICATION = 'dajax_test.wsgi.application'

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
)
