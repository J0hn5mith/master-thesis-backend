import sys

from master_thesis_backend.settings.base import *  # noqa

DEBUG = True

INSTALLED_APPS += ('debug_toolbar', 'django_extensions', )

INTERNAL_IPS = ('127.0.0.1', )

#: Don't send emails, just print them on stdout
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
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
SENDSMS_BACKEND = 'sendsms.backends.twiliorest.SmsBackend'
SENDSMS_FROM_NUMBER = '+41798074786'
SENDSMS_TWILIO_ACCOUNT_SID = 'AC8c157f3981c2d3c3d9cd8f8dcbd3fb2c'
SENDSMS_TWILIO_AUTH_TOKEN = '6925d887df65c472217021a657ab912f'
