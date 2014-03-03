"""
Django settings for libya tally project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'el7%8*2=m()uxvg%ebet#o81y(qi%yi-k&&4iz^z=sces+i9lt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['localhost']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_nose',
    'djangojs',
    'eztables',
    'guardian',
    'reversion',
    'tally_system.apps.tally',
    'south',
    'tracking',
)

MIDDLEWARE_CLASSES = (
    'tracking.middleware.VisitorTrackingMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
    'tally_system.libs.middleware.idle_timeout.IdleTimeout',
    'tally_system.libs.middleware.user_restrict.UserRestrictMiddleware',
    'tally_system.libs.middleware.disable_clientside_caching.'
    'DisableClientsideCachingMiddleware',
    'tally_system.libs.middleware.exception_logging.ExceptionLoggingMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'tally_system.libs.utils.context_processors.debug',
    'tally_system.libs.utils.context_processors.is_superadmin',
    'tally_system.libs.utils.context_processors.locale',
    'tally_system.libs.utils.context_processors.site_name',
)


ROOT_URLCONF = 'tally_system.urls'

WSGI_APPLICATION = 'tally_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tally',
        'USER': 'postgres',
        'PASSWORD': 'tally',
        'HOST': '127.0.0.1',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # this is default
    'guardian.backends.ObjectPermissionBackend',
)

ANONYMOUS_USER_ID = -1

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'libs', 'templates'),
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_PLUGINS = [
    'tally_system.libs.nose_plugins.SilenceSouth'
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

SITE_ID = 1

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=tally_system'
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

LOGIN_REDIRECT_URL = '/'

# Switch to True on production
SESSION_COOKIE_SECURE = False

# In minutes
IDLE_TIMEOUT = 60

# Individual pageviews will be tracked
TRACK_PAGEVIEWS = True

LOCALE_PATHS = (os.path.realpath(os.path.join(BASE_DIR, '..', 'locale')),)

LOGGING = {
    'version': 1,
    'root': {'level': 'DEBUG' if DEBUG else 'INFO'},
}
