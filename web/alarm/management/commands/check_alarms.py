from django.core.management.base import BaseCommand
from alarm.models import AlarmConfig, Alarm
from alarm.utils import check_trigger_alarm, create_alarm


class Command(BaseCommand):
    help = 'Util method to test the alarm triggering'

    def handle(self, *args, **options):
        """
        * Check existence of all object
        * Check if alarm is activated
        * Check if tag not already has alarm
        """

        self.delete_alarms()
        for alarm_config in AlarmConfig.objects.all():
            if check_trigger_alarm(alarm_config):
                print("Trigger alarm")
                create_alarm(alarm_config)

    def delete_alarms(self):
        for alarm in Alarm.objects.all():
            alarm.delete()
