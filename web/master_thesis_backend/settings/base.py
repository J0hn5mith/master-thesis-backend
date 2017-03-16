"""
Django settings for master_thesis_backend project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

# TODO: Update with https://github.com/jpadilla/
# django-project-template/blob/master/project_name/settings.py
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ADMINS = (  # ('Your Name', 'your_email@example.com'),
)

# Application definition

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.gis',
]

THIRD_PARTY_APPS = [
    # Local but has to stand before registration.
    # Otherwise templates are not found.
    'login_registration',
    'registration',
    'widget_tweaks',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',
    'rest_framework',
    'rest_framework_gis',  # Has to be after rest_framework
]

LOCAL_APPS = [
    'utils',
    'home',
    'dashboard',
    'user',
    'tags',
    'sensor_data',
    'alarm',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_otp.middleware.OTPMiddleware',
]

ROOT_URLCONF = 'master_thesis_backend.urls'

TEMPLATES = [
    {
        'BACKEND':
        'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(PROJECT_ROOT, 'templates'),
            os.path.join(PROJECT_ROOT, '*/templates'),
        ],
        'APP_DIRS':
        True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'dealer.contrib.django.context_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'master_thesis_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    # 'default': {
    # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
    # 'NAME': os.environ['DB_NAME'],
    # 'USER': os.environ['DB_USER'],
    # 'PASSWORD': os.environ['DB_PASS'],
    # 'HOST': os.environ['DB_SERVICE'],
    # 'PORT': os.environ['DB_PORT']
    # },
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': os.environ.get('DB_SERVICE'),
        'PORT': os.environ.get('DB_PORT'),
    },
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'basic': {
            'format': '%(asctime)s %(name)-20s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'basic',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'two_factor': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    },
    'root': {
        'handlers': [
            'console',
        ],
        'level': 'INFO',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'
LOCALE_PATHS = (os.path.join(PROJECT_ROOT, 'locale'), )

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Zurich'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'), )

# If using Celery, tell it to obey our logging configuration.
CELERYD_HIJACK_ROOT_LOGGER = False

# https://docs.djangoproject.com/
# en/1.9/topics/auth/passwords/#password-validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation\
                .UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Make things more secure by default. Run "python manage.py check --deploy" for
# even more suggestions that you might want to add to the settings, depending
# on how the site uses SSL.
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

##################################################
# Third Party
##################################################

# Django Registration
ACCOUNT_ACTIVATION_DAYS = 1
REGISTRATION_DEFAULT_FROM_EMAIL = "john-doe@example.com"  # TODO
REGISTRATION_EMAIL_HTML = True
REGISTRATION_AUTO_LOGIN = True

# Django Registration
LOGIN_URL = 'two_factor:login'
TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.fake.Fake'
TWO_FACTOR_CALL_GATEWAY = 'two_factor.gateways.fake.Fake'
LOGIN_REDIRECT_URL = 'http://localhost:8000/dashboard'

# Django REST framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
    ('rest_framework.authentication.SessionAuthentication', ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # TODO: Change that!!
    ],
    'DEFAULT_FILTER_BACKENDS':
    ('django_filters.rest_framework.DjangoFilterBackend', ),
    'PAGE_SIZE':
    200
}

# Celery
BROKER_URL = 'redis://{url}:{port}'.format(
    url=os.environ.get('REDIS_SERVICE'),
    port=os.environ.get('REDIS_PORT'),
)
BROKER_TRANSPORT = BROKER_URL
CELERY_BROKER_URL = BROKER_URL
CELERY_RESULT_BACKEND = BROKER_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
