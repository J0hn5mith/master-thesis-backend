from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.contrib.auth import get_user_model
from user.notifications import notify

User = get_user_model()


class NotificationsTestCase(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(
            username='test', password='test', email='test@test.com'
        )
        self.user.conf.has_active_email = MagicMock(return_value=True)
        self.user.conf.has_active_phone = MagicMock(return_value=True)

    @patch('user.notifications.notify_by_sms')
    @patch('user.notifications.notify_by_email')
    def test_all(self, notify_by_email, notify_by_sms):
        self.user.conf.notify_by_email = True
        self.user.conf.notify_by_sms = True
        self.user.save()

        notify(
            self.user,
            'body',
            'subject',
            'sms',
        )

        self.assertTrue(notify_by_email.called)
        self.assertTrue(notify_by_sms.called)

    @patch('user.notifications.notify_by_sms')
    @patch('user.notifications.notify_by_email')
    def test_mail_only(self, notify_by_email, notify_by_sms):
        self.user.conf.notify_by_email = True
        self.user.conf.notify_by_sms = False
        self.user.save()

        notify(
            self.user,
            'body',
            'subject',
            'sms',
        )

        self.assertTrue(notify_by_email.called)
        self.assertFalse(notify_by_sms.called)

    @patch('user.notifications.notify_by_sms')
    @patch('user.notifications.notify_by_email')
    def test_sms_only(self, notify_by_email, notify_by_sms):
        self.user.conf.notify_by_email = False
        self.user.conf.notify_by_sms = True
        self.user.save()

        notify(
            self.user,
            'body',
            'subject',
            'sms',
        )

        self.assertFalse(notify_by_email.called)
        self.assertTrue(notify_by_sms.called)
