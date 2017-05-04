from django.conf import settings
from django.core.mail import send_mail
from sendsms.api import send_sms
from celery.decorators import task
from django.contrib.auth import get_user_model

User = get_user_model()


def notify_by_email(user, subject, message):
    send_mail(
        subject,
        message,
        settings.NOTIFICATION_FROM_EMAIL,
        [user.email],
        fail_silently=False,
        html_message=message,
    )


def notify_by_sms(user, message):
    phone_number = str(user.phonedevice_set.all().first().number)
    send_sms(
        body=message,
        from_phone=settings.SENDSMS_FROM_NUMBER,
        to=[phone_number],
        fail_silently=False,
    )


from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)


@task(name="test")
def test():
    logger.info("Test")


@task(name="notify")
def notify(user_id, subject=None, email=None, sms=None):
    """
    Sends a notification to a user. The notifications are only
    sent if the channel content is provided and the user as activated
    the channel in the settings. So far the channels 'SMS' and 'Email'
    are available.
    """
    user = None
    try:
        user = User.objects.get(id=user_id)
    except:
        print(
            "Can't send message to user with id {0}. User does not exist".
            format(user_id)
        )

    if email and subject and user.conf.notify_by_email:
        notify_by_email(user, subject, email)

    if sms and user.conf.notify_by_sms:
        notify_by_sms(user, sms)
