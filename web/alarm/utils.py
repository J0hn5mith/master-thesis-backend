from datetime import timedelta
from django.utils import timezone
from alarm.models import Alarm


def check_trigger_alarm(alarm_config):
    """
    Checks if a alarm should be triggered for specified tag.
    """
    circle = alarm_config.area.center.buffer(alarm_config.area.radius)
    return circle.disjoint(alarm_config.tag.current_position().position)


def create_alarm(alarm_config):
    """
    Creates an alarm instance for alarm_config associated tag.
    """
    Alarm.objects.get_or_create(
        tag=alarm_config.tag,
        start_position=(alarm_config.tag.current_position().position),
        activate_time=timezone.now() +
        timedelta(seconds=alarm_config.tag.alarm_config.time_to_deactivate)
    )


def update_alarms():
    """
    Checks if a pending alarm has reached it's activation time and in case sets
    the alarm to active.
    """
    for alarm in Alarm.objects.all():
        # Triggered
        if alarm.state == 0:
            alarm.state = 1
            alarm.save()
            print("Changed alarm state to pending")
        # Pending
        elif alarm.state == 1 and alarm.activate_time <= timezone.now():
            alarm.state = 2
            alarm.save()
            print("Changed alarm state to active")
