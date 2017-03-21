from django.core.management.base import BaseCommand
from alarm.utils import send_alarm_notification
from ...models import Alarm


class Command(BaseCommand):
    help = 'Util method to test the alarm triggering'

    def handle(self, *args, **options):
        alarm = Alarm.objects.all().first()
        send_alarm_notification(alarm)
