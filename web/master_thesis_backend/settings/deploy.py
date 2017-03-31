from .base import *  # noqa

DEBUG = False

INTERNAL_IPS = ('127.0.0.1', )
ALLOWED_HOSTS = (os.environ.get('HOST'),)
PAGE_URL = os.environ.get('PAGE_URL')

EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', False)
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', False)

SECRET_KEY = os.environ.get('SECRET_KEY')


INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]

WEBSERVER_ROOT = '/var/www/master_thesis_backend/'

PUBLIC_ROOT = os.path.join(WEBSERVER_ROOT, 'public')
STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')
MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


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
    'release': 'production',
}
