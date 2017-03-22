import sys
from master_thesis_backend.settings.base import *

DEBUG = True

INSTALLED_APPS += ('debug_toolbar', 'django_extensions', )

INTERNAL_IPS = ('127.0.0.1', )
PAGE_URL = os.environ.get('PAGE_URL')

#: Don't send emails, just print them on stdout
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


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

##################################################
# Third Party
##################################################

# Django Registration
# TODO: Move Twilio credentials to env file
TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'
TWILIO_CALLER_ID = os.environ.get('TWILIO_PHONE_NUMBER')
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

# Django SendSMS
SENDSMS_BACKEND = 'sendsms.backends.twiliorest.SmsBackend'
SENDSMS_FROM_NUMBER = TWILIO_CALLER_ID
SENDSMS_TWILIO_ACCOUNT_SID = TWILIO_ACCOUNT_SID
SENDSMS_TWILIO_AUTH_TOKEN = TWILIO_AUTH_TOKEN

# Celery
CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
