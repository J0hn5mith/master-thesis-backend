from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from ...notifications import notify

User = get_user_model()


class Command(BaseCommand):
    help = 'Util method to test the alarm triggering'

    def handle(self, *args, **options):
        user = User.objects.all().first()
        notify(user, "Test Subject", "Test Email", "Test SMS")
