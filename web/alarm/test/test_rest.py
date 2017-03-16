from datetime import timedelta
from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from tags.models import Tag
from alarm.models import Alarm
from django.contrib.gis.geos import Point


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
        self.assertEqual(response.status_code, 200)

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
        self.assertEqual(response.status_code, 200)
