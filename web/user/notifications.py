from django.conf import settings
from django.core.mail import send_mail
from sendsms.api import send_sms


def notify(user):
    if user.notify_by_email:
        notify_by_email()

    if user.notify_by_sms:
        notify_by_sms()


def notify_by_email(user):
    send_mail(
        'Subject here',
        'Here is the message.',
        'pharos@jan-meier.ch',
        ['test@jan-meier.ch'],
        fail_silently=False,
    )


def notify_by_sms(user):
    send_sms(
        body='I can haz txt',
        from_phone=settings.SENDSMS_FROM_NUMBER,
        to=['+41793742352'],
        fail_silently=False,
    )
