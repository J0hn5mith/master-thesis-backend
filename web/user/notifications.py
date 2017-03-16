from django.conf import settings
from django.core.mail import send_mail
from sendsms.api import send_sms


def notify_user(user):
    pass


def notify_user_mail():
    send_mail(
        'Subject here',
        'Here is the message.',
        'pharos@jan-meier.ch',
        ['test@jan-meier.ch'],
        fail_silently=False,
    )


def notify_user_sms():
    send_sms(
        body='I can haz txt',
        from_phone=settings.SENDSMS_FROM_NUMBER,
        to=['+41793742352'],
        fail_silently=False,
    )
