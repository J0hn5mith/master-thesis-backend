import sys
from .base import *

DEBUG = True

INTERNAL_IPS = ('127.0.0.1', )
# 'localhos' makes sure that non docker setup works
ALLOWED_HOSTS = (os.environ.get('DOMAIN'), 'localhost', '127.0.0.1')
PAGE_URL = os.environ.get('DOMAIN')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS = True

SECRET_KEY = os.environ.get('SECRET_KEY')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS += ('debug_toolbar', 'django_extensions', )
STATIC_ROOT = static
STATIC_URL = '/static/'


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

# Celery
CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

# REST
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].append(
        'rest_framework.authentication.BasicAuthentication'
        )

