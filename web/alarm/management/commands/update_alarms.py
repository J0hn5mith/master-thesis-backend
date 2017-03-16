from django.core.management.base import BaseCommand
from alarm.utils import update_alarms


class Command(BaseCommand):
    help = 'Util method to test the alarm triggering'

    def handle(self, *args, **options):
        update_alarms()


