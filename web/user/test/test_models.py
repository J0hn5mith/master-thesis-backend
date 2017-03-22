from unittest.mock import MagicMock
from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class UserConfigurationSignalsTestCase(TestCase):
    """
    Test signals related to the UserConfiguration model.
    """

    def test_auto_creation_email(self):
        """
        Test if user config is created correctly on instance creation of User
        model
        """
        self.user, created = User.objects.get_or_create(
            username='test2',
            password='test2',
        )
        self.assertIsNotNone(
            self.user.conf,
            "User should have conf instance set.",
        )


class UserConfigurationTestCase(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(
            username='test',
            password='test',
        )
        self.user_conf = self.user.conf

    def test_set_notify_by_email(self):
        """
        Test if `notify_by_email` only can be set if there is valid mail.
        """
        self.user_conf.notify_by_email = True
        self.user_conf.save()
        self.assertFalse(
            self.user_conf.notify_by_email,
            "Should be false because mail was not set."
        )

        self.user.email = 'john.doe@example.com'
        self.user.save()

        self.user_conf.notify_by_email = True
        self.user_conf.save()
        self.assertTrue(
            self.user_conf.notify_by_email,
            "Should be true because email has been set."
        )

    def test_set_notify_by_sms(self):
        """
        Test if `notify_by_sms` only can be set if there is valid mail.
        """
        self.user_conf.notify_by_sms = True
        self.user_conf.has_active_phone = MagicMock(return_value=False)
        self.user_conf.save()
        self.assertFalse(
            self.user_conf.notify_by_sms,
            "Should be false because sms was not set."
        )

        self.user_conf.notify_by_sms = True
        self.user_conf.has_active_phone = MagicMock(return_value=True)
        self.user_conf.save()
        self.assertTrue(
            self.user_conf.notify_by_sms,
            "Should be true because sms has been set."
        )
