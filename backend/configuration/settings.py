import sys
import os
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    msg = "Set the %s environment variable"
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = msg % var_name
        raise ImproperlyConfigured(error_msg)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = get_env_variable('DEBUG')

SECRET_KEY = os.environ.get('SECRET_KEY', 'kr%c(bvk1!w0*lr2fpq2+7e(67b-p&3)nxb_$#6_s1$j1bu49!')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split()

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # extensions
    'django_extensions',
    'rest_framework',
    'allauth',
    'allauth.account',
    'rest_auth',
    'rest_auth.registration',

    # apps
    'users',
    'locations',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

REST_USE_JWT = True

ROOT_URLCONF = 'configuration.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'configuration.wsgi.application'

DOMAIN = os.environ.get('DOMAIN', 'http://0.0.0.0:8000')


# Email settings
EMAILS = {
    'registration': 'registration@domain.com',
    'notifications': 'notifications@domain.com',
}
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")


# Database settings
if os.environ.get('DATABASE', None) == 'POSTGRESQL':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': get_env_variable('DB_NAME'),
            'USER': get_env_variable('DB_USER'),
            'PASSWORD': get_env_variable('DB_PASS'),
            'HOST': 'localhost',
            'PORT': '',
        },
    }
else:  # used when running tests
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('STATIC_ROOT')


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


# Celery settings
BROKER_URL = 'redis://127.0.0.1:6379/0'
BROKER_TRANSPORT = 'redis'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

if 'test' in sys.argv[1:]:
    raise ImproperlyConfigured("use py.test to run tests")
