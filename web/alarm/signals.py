from django.db.models.signals import post_save
from sensor_data.models import PositionMeasurement
from tags.models import Tag
from alarm.utils import detect_alarms, create_alarm, send_alarm_notification


def check_tag_for_alarm(sender, instance, created, **kwargs):
    """
    Checks if a new position instance triggers a tags alarm. If yes, a alarm
    object for the tag is created.
    """
    tag = None
    try:
        tag = Tag.objects.get(uid=instance.uid)
        if detect_alarms(tag):
            send_alarm_notification(create_alarm(tag.alarm_config))
    except Tag.DoesNotExist:
        pass


post_save.connect(check_tag_for_alarm, PositionMeasurement)
