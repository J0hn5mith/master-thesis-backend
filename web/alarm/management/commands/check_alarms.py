from django.core.management.base import BaseCommand
from alarm.models import AlarmConfig, Alarm
from datetime import timedelta, datetime
from django.utils import timezone

from django.contrib.gis import geos


class Command(BaseCommand):
    help = 'Util method to test the alarm triggering'

    def handle(self, *args, **options):
        """
        * Check existence of all object
        * Check if alarm is activated
        * Check if tag not already has alarm
        """

        self.delete_alarms()
        for a in AlarmConfig.objects.all():
            circle = a.area.center.buffer(a.area.radius)
            if circle.disjoint(a.tag.current_position().position):
                self.create_alert(a)

    def delete_alarms(self):
        for alarm in Alarm.objects.all():
            alarm.delete()

    def create_alert(self, a):
        alarm = Alarm.objects.get_or_create(
                tag=a.tag,
                start_position=(a.tag.current_position().position),
                activate_time=timezone.now() +
                timedelta(seconds=a.tag.alarm_config.time_to_deactivate)
                )
