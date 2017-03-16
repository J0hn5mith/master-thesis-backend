from django.test import TestCase
from django.contrib.auth import get_user_model
from user.notifications import notify_user


User = get_user_model()


class NotificationsTrestCase(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(
            username='test',
            password='test',
        )
        print(self.user.conf.notify_by_email)
        print(self.user.conf.notify_by_sms)

    def test_all(self):
        notify_user(self.user)
