"""
Settings file for running unit tests.
"""
# Settings for live deployed environments: vagrant, staging, production, etc
from master_thesis_backend.settings.base import *

os.environ.setdefault('CACHE_HOST', '127.0.0.1:11211')
os.environ.setdefault('BROKER_HOST', '127.0.0.1:5672')

#: deploy environment - e.g. "staging" or "production"
ENVIRONMENT = os.environ['ENVIRONMENT']

SECRET_KEY = 'SECRET_KEY'
PAGE_URL = 'example.com'

DEBUG = False

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

ALLOWED_HOSTS = [os.environ['DOMAIN']]

DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'

# Use template caching on deployed servers
for backend in TEMPLATES:
    if backend['BACKEND'] == 'django.template.backends.django.DjangoTemplates':
        default_loaders = ['django.template.loaders.filesystem.Loader']
        if backend.get('APP_DIRS', False):
            default_loaders.append('django.template.loaders.app_directories.Loader')
            # Django gets annoyed if you both set APP_DIRS True and specify your own loaders
            backend['APP_DIRS'] = False
        loaders = backend['OPTIONS'].get('loaders', default_loaders)
        for loader in loaders:
            if len(loader) == 2 and loader[0] == 'django.template.loaders.cached.Loader':
                # We're already caching our templates
                break
        else:
            backend['OPTIONS']['loaders'] = [('django.template.loaders.cached.Loader', loaders)]


# Environment overrides
# These should be kept to an absolute minimum
if ENVIRONMENT.upper() == 'LOCAL':
    # Don't send emails from the Vagrant boxes
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Django SendSMS
SENDSMS_FROM_NUMBER = '+15005550006'  # Magic number that passes everything
SENDSMS_BACKEND = 'sendsms.backends.twiliorest.SmsBackend'
SENDSMS_TWILIO_ACCOUNT_SID = 'AC1a1b980ad0faa5bd2f08ac7427a89159'
SENDSMS_TWILIO_AUTH_TOKEN = '6e18ecb8e71d3bb723a1031bc729f901'
