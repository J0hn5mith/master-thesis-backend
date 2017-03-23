# Settings for live deployed environments: vagrant, staging, production, etc
from .base import *  # noqa

os.environ.setdefault('CACHE_HOST', '127.0.0.1:11211')
os.environ.setdefault('BROKER_HOST', '127.0.0.1:5672')

#: deploy environment - e.g. "staging" or "production"
ENVIRONMENT = os.environ['ENVIRONMENT']
ALLOWED_HOSTS = (os.environ.get('HOST'),)
ALLOWED_HOSTS = (os.environ['DOMAIN'],)
PAGE_URL = os.environ.get('PAGE_URL')

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]

WEBSERVER_ROOT = '/var/www/master_thesis_backend/'

PUBLIC_ROOT = os.path.join(WEBSERVER_ROOT, 'public')

STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')

MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '%(CACHE_HOST)s' % os.environ,
    }
}

EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', False)
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', False)
# use TLS or SSL, not both:
assert not (EMAIL_USE_TLS and EMAIL_USE_SSL)
if EMAIL_USE_TLS:
    default_smtp_port = 587
elif EMAIL_USE_SSL:
    default_smtp_port = 465
else:
    default_smtp_port = 25
EMAIL_PORT = os.environ.get('EMAIL_PORT', default_smtp_port)
EMAIL_SUBJECT_PREFIX = '[Master_Thesis_Backend %s] ' % ENVIRONMENT.title()
DEFAULT_FROM_EMAIL = 'noreply@%(DOMAIN)s' % os.environ
SERVER_EMAIL = DEFAULT_FROM_EMAIL

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True


# Use template caching on deployed servers
for backend in TEMPLATES:
    if backend['BACKEND'] == 'django.template.backends.django.DjangoTemplates':
        default_loaders = ['django.template.loaders.filesystem.Loader']
        if backend.get('APP_DIRS', False):
            default_loaders.append(
                'django.template.loaders.app_directories.Loader'
            )
            # Django gets annoyed if you
            # both set APP_DIRS True and specify your own loaders
            backend['APP_DIRS'] = False
        loaders = backend['OPTIONS'].get('loaders', default_loaders)
        for loader in loaders:
            if len(loader) == 2 \
                    and loader[0] == 'django.template.loaders.cached.Loader':
                # We're already caching our templates
                break
        else:
            backend['OPTIONS']['loaders'] = [
                ('django.template.loaders.cached.Loader', loaders)
            ]

# Uncomment if using celery worker configuration
# CELERY_SEND_TASK_ERROR_EMAILS = True
# BROKER_URL = 'amqp://master_thesis_backend_%(ENVIRONMENT)s:%(BROKER_PASSWORD)s@%(BROKER_HOST)s/master_thesis_backend_%(ENVIRONMENT)s' % os.environ  # noqa

# Environment overrides
# These should be kept to an absolute minimum
if ENVIRONMENT.upper() == 'LOCAL':
    # Don't send emails from the Vagrant boxes
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

##################################################
# Third Party
##################################################

# Django Registration
TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'
TWILIO_CALLER_ID = os.environ.get('TWILIO_PHONE_NUMBER')
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

# Django SendSMS
SENDSMS_BACKEND = 'sendsms.backends.twiliorest.SmsBackend'
SENDSMS_FROM_NUMBER = TWILIO_CALLER_ID
SENDSMS_TWILIO_ACCOUNT_SID = TWILIO_ACCOUNT_SID
SENDSMS_TWILIO_AUTH_TOKEN = TWILIO_AUTH_TOKEN

# Sentry & Raven
RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_URL'),
    # 'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
    'release': 'dev',
}
