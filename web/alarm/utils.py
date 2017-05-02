from datetime import timedelta
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.template.loader import render_to_string
from alarm.models import Alarm
from user.notifications import notify


def detect_alarms(tag):
    """
    Checks if a alarm has to be triggered for a specific tag.
    """
    if not tag.active:
        return False

    if hasattr(tag, 'alarm'):
        return False

    alarm_config = tag.alarm_config
    circle = alarm_config.area.center.buffer(alarm_config.area.radius*0.01)
    disjoint = circle.disjoint(alarm_config.tag.current_position().position)
    return disjoint


def create_alarm(alarm_config):
    """
    Creates an alarm instance for alarm_config associated tag.
    """
    return Alarm.objects.get_or_create(
        tag=alarm_config.tag,
        start_position=(alarm_config.tag.current_position().position),
        activate_time=timezone.now() +
        timedelta(seconds=alarm_config.tag.alarm_config.time_to_deactivate)
    )[0]


def update_alarms():
    """
    Checks if a pending alarm has reached it's activation time and in case sets
    the alarm to active.
    """
    for alarm in Alarm.objects.all():
        # Triggered
        if alarm.state == Alarm.states.TRIGGERED:
            alarm.state = Alarm.states.PENDEING
            alarm.save()
            send_alarm_notification(alarm)
        elif alarm.state == Alarm.states.PENDING and\
                alarm.activate_time <= timezone.now():
            alarm.state = 2
            alarm.save()


def send_alarm_notification(alarm):
    """
    Sends a notification to inform the user that one of his/her
    tags has triggered an alarm
    """
    context = {}
    context["tag"] = alarm.tag
    context['url_confirm'] = ''.join(
        [
            settings.PAGE_URL,
            reverse(
                'confirm-alarm', kwargs={'random_token': alarm.random_token}
            ),
        ]
    )
    context['url_cancel'] = ''.join(
        [
            settings.PAGE_URL, reverse(
                'cancel-alarm', kwargs={'random_token': alarm.random_token}
            )
        ]
    )

    mail_content = None
    mail_subject = None
    sms_content = None
    try:
        mail_content = render_to_string('mail.html', context=context)
        mail_subject = render_to_string('mail_subject.txt', context=context)
        sms_content = render_to_string('sms.txt', context=context)
    except:
        print("Failed to render template")

    notify(alarm.tag.user, mail_subject, mail_content, sms_content)
