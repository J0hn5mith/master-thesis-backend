from datetime import timedelta
from django.contrib.gis.geos import Point
from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient
from tags.models import Tag
from alarm.models import Alarm

client = APIClient()


class AlarmConfigRESTTrestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create()  # Creates alarm config by signal
        self.url_list = reverse('alarmconfig-list')
        self.url_detail = reverse_lazy(
            'alarmconfig-detail', kwargs={'pk': self.tag.pk}
        )

    def test_get(self):
        response = client.get(self.url_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        response = client.get(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response.data['time_to_deactivate'] = 30
        response = client.put(self.url_detail, response.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AlarmConfigAreaRESTTrestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create()  # Creates alarm config by signal
        self.tag.save()
        self.url_list = reverse('alarmconfigarea-list')
        self.url_detail = reverse_lazy(
            'alarmconfigarea-detail', kwargs={'pk': self.tag.pk}
        )

    def test_get(self):
        response = client.get(self.url_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        response = client.get(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response.data['radius'] = 30
        response = client.put(self.url_detail, response.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AlarmSerializeRESTTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create()  # Creates alarm config by signal
        self.tag.save()
        self.alarm = Alarm.objects.get_or_create(
            tag=self.tag,
            start_position=Point(0, 0),
            activate_time=timezone.now() +
            timedelta(seconds=self.tag.alarm_config.time_to_deactivate)
        )
        self.url_list = reverse('alarm-list')
        self.url_detail = reverse_lazy(
            'alarm-detail', kwargs={'pk': self.tag.pk}
        )

    def test_get(self):
        response = client.get(self.url_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        response = client.get(self.url_detail, format='json')
        self.assertEqual(response.status_code, 200)
        response.data['state'] = 1
        response = client.put(self.url_detail, response.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AlarmManagementRESTTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create()  # Creates alarm config by signal
        self.tag.save()
        self.alarm, cerated = Alarm.objects.get_or_create(
            tag=self.tag,
            start_position=Point(0, 0),
            activate_time=timezone.now() +
            timedelta(seconds=self.tag.alarm_config.time_to_deactivate)
        )

    def test_cancel_alarm(self):
        self.alarm.state = Alarm.states.PENDING
        self.alarm.save()
        url = reverse(
            'cancel-alarm', kwargs={'random_token': self.alarm.random_token}
        )

        response = client.get(url, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_200_OK, "Alarm failed to cancel."
        )
        self.alarm.refresh_from_db()
        self.assertEqual(
            self.alarm.state, Alarm.states.CANCELED,
            "State has been set incorrect"
        )

        response = client.get(url, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_404_NOT_FOUND,
            "Alarm could be canceled in wrong state."
        )
        self.alarm.refresh_from_db()
        self.assertEqual(
            self.alarm.state, Alarm.states.CANCELED,
            "Stat has been changed but it should not."
        )

    def test_confirm_alarm(self):

        self.alarm.state = Alarm.states.PENDING
        self.alarm.save()
        url = reverse(
            'confirm-alarm', kwargs={'random_token': self.alarm.random_token}
        )

        response = client.get(url, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_200_OK, "Alarm failed to cancel."
        )
        self.alarm.refresh_from_db()
        self.assertEqual(
            self.alarm.state, Alarm.states.ACTIVE,
            "State has been set incorrect"
        )

        response = client.get(url, format='json')
        self.assertEqual(
            response.status_code, status.HTTP_404_NOT_FOUND,
            "Alarm could be canceled in wrong state."
        )

        self.alarm.refresh_from_db()
        self.assertEqual(
            self.alarm.state, Alarm.states.ACTIVE,
            "State has been changed but should have not."
        )
