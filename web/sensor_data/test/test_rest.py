from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from rest_framework.test import APIClient
from django.contrib.gis.geos import Point
from sensor_data.models import PositionMeasurement
from rest_framework import status

client = APIClient()


class SensorDataRESTTrestCase(TestCase):
    def setUp(self):
        self.sensor_data = PositionMeasurement.objects.create(
            uid='uid',
            time_stamp=timezone.now(),
            position=Point(0, 0),
        )
        self.url_list = reverse('positionmeasurement-list')
        self.url_detail = reverse_lazy(
            'positionmeasurement-detail', kwargs={'pk': self.sensor_data.pk}
        )

    def test_get(self):
        response = client.get(self.url_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = client.get(self.url_detail, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = client.delete(self.url_detail, response.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
