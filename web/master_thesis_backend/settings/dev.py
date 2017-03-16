import sys

from master_thesis_backend.settings.base import *  # noqa

DEBUG = True

INSTALLED_APPS += ('debug_toolbar', 'django_extensions',)

INTERNAL_IPS = ('127.0.0.1', )

#: Don't send emails, just print them on stdout
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

#: Run celery tasks synchronously
CELERY_ALWAYS_EAGER = True

#: Tell us when a synchronous celery task fails
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    '3vdexi69&m+lus9b0#wx57m%@6qz8rb^t=oogxt&6wcw$z*!zn',
)

# Special test settings
if 'test' in sys.argv:
    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.SHA1PasswordHasher',
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )

    LOGGING['root']['handlers'] = []

# Django SendSMS
SENDSMS_BACKEND = 'sendsms.backends.console.SmsBackend'
SENDSMS_FROM_NUMBER = '+15005550006' # Magic number that passes everything
